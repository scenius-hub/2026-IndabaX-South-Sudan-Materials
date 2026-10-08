import os
import json
import time
import uuid
from flask import Flask, request, jsonify, send_file
from google import genai
from google.genai import types

app = Flask(__name__)
client = genai.Client()  # reads GEMINI_API_KEY
MODELS = ["gemini-flash-lite-latest", "gemini-3.5-flash", "gemini-3.8-flash"]
MAX_Q = 10  # questions per puzzle

LEVELS = {
    1: {"name": "Beginner", "points": 10,
        "riddle": "Use very simple everyday words and give 2 clear, obvious clues."},
    2: {"name": "Intermediate", "points": 20,
        "riddle": "Use simple words and give 2 clear clues about what it does or where it's used."},
    3: {"name": "Advanced", "points": 30,
        "riddle": "Use simple words and give 2 helpful clues about what it does. A small playful twist is okay, but keep it fair."},
}

# What a good answer looks like for each category and level (examples guide the difficulty)
GUIDE = {
    "AI & ML Concepts": {
        1: "basic ideas like robot, chatbot, data, computer, internet",
        2: "core ideas like algorithm, training data, machine learning, neural network, prediction",
        3: "technical ideas like overfitting, gradient descent, transformer, reinforcement learning, computer vision"},
    "Famous Tech Tools": {
        1: "everyday apps like WhatsApp, Google Search, YouTube, Facebook",
        2: "tools like ChatGPT, Google Translate, Microsoft Excel, Zoom, GitHub",
        3: "developer tools like Python, TensorFlow, Jupyter Notebook, Linux, Git"},
    "Jobs & Careers": {
        1: "familiar jobs like teacher, doctor, farmer, engineer, journalist",
        2: "tech jobs like software developer, data analyst, graphic designer, IT support technician",
        3: "specialist tech roles like data scientist, machine learning engineer, cybersecurity analyst, cloud engineer"},
    "AI in Everyday Life": {
        1: "things like voice assistant, face unlock, autocorrect, online maps",
        2: "features like spam filter, video recommendations, translation app, photo filters",
        3: "applications like fraud detection, self-driving car, crop disease detection, weather forecasting"},
    "South Sudan": {
        1: "well-known things like Juba, the Nile, the national flag",
        2: "places and culture like the Sudd wetland, Boma National Park, Independence Day",
        3: "more specific things like the Imatong Mountains, Mount Kinyeti, Nimule National Park"},
    "Animals": {
        1: "common animals like lion, cow, elephant, chicken",
        2: "less common animals like giraffe, crocodile, hippo, ostrich",
        3: "harder animals like shoebill, pangolin, white-eared kob, aardvark"},
}

games = {}
used = []  # answers already used, to avoid repeats

def ai(system, user, as_json=False):
    config = types.GenerateContentConfig(system_instruction=system)
    if as_json:
        config.response_mime_type = "application/json"
    last_error = None
    for model in MODELS:
        for attempt in range(2):
            try:
                r = client.models.generate_content(model=model, contents=user, config=config)
                return (r.text or "").strip()
            except Exception as e:
                last_error = e
                if any(s in str(e) for s in ("503", "UNAVAILABLE", "429")):
                    time.sleep(2)
                    continue
                break  # other error: try next model
    raise last_error

def host_prompt(g):
    return (f"You are a witty, energetic game-show host. The secret answer is: {g['secret']} "
            f"(category: {g['category']}). Never reveal it unless the player guesses it.\n"
            "Rules:\n"
            "- Answer every yes/no question truthfully and accurately about the secret. "
            "Start with Yes, No, or Sometimes (use Sometimes only when it is partly true or depends), "
            "then add ONE short playful sentence that does not give away the answer.\n"
            "- If the player names the secret, a clear synonym, or a common short form (e.g. 'AI' for "
            "'artificial intelligence'), start with CORRECT! and celebrate in one sentence.\n"
            "- A wrong guess like 'Is it X?' gets No plus a playful line.\n"
            "- If it isn't a yes/no question, cheekily ask for one.\n"
            "- Keep every reply under 30 words and use simple words.")

def busy_error(e):
    print("AI ERROR:", e)
    msg = str(e)
    if any(s in msg for s in ("429", "RESOURCE_EXHAUSTED", "503", "UNAVAILABLE")):
        return jsonify(error="The AI is busy right now. Wait a minute and try again."), 429
    return jsonify(error="The AI didn't respond. Check your API key and internet connection."), 503

def explain(g):
    try:
        return ai("You explain things simply to people at an AI/ML workshop. Reply with only the explanation.",
                  f"In 2-3 short, simple sentences, explain what '{g['secret']}' (category: {g['category']}) is "
                  "and share one interesting, true fact about it. If it relates to AI or technology, mention how.")
    except Exception:
        return None

def make_puzzle(cat, level_num):
    level = LEVELS[level_num]
    guide = GUIDE.get(cat, {}).get(level_num, "well-known things in this category")
    avoid = ", ".join(used[-40:]) or "none"
    raw = ai(
        "You create puzzles for a team guessing game at IndabaX South Sudan, an AI/ML event. "
        "Reply with JSON only.",
        f"Category: {cat}\n"
        f"Level: {level['name']}\n"
        f"Difficulty guide for this level: {guide}. Use these to judge the difficulty; "
        "you may pick one of them or something similar at the same level.\n"
        f"Do not use any of these answers: {avoid}\n\n"
        "Pick ONE answer (a short name, 1-4 words), then write a riddle about it.\n"
        "Riddle rules: 2 lines, spoken as the thing itself starting with 'I'. "
        f"{level['riddle']} Every clue must be factually true and match only this answer. "
        "Do not use the answer's name or any word from it. A light rhyme is okay. "
        "End with a new line that says exactly: What am I?\n\n"
        'Return exactly: {"answer": "...", "riddle": "..."}',
        as_json=True)
    data = json.loads(raw.replace("```json", "").replace("```", "").strip())
    return data["answer"].strip(" .\"'\n"), data["riddle"].strip()

@app.route("/")
def index():
    return send_file("index.html")

@app.route("/logo.png")
def logo():
    if os.path.exists(os.path.join(app.root_path, "logo.png")):
        return send_file("logo.png")
    return "", 404

@app.post("/new")
def new_game():
    data = request.json or {}
    cat = data.get("category", "Animals")
    level_num = int(data.get("level", 1))
    if level_num not in LEVELS:
        level_num = 1
    try:
        secret, riddle = make_puzzle(cat, level_num)
    except Exception as e:
        return busy_error(e)
    used.append(secret)
    gid = uuid.uuid4().hex
    games[gid] = {"secret": secret, "category": cat, "left": MAX_Q,
                  "level": LEVELS[level_num], "done": False}
    return jsonify(id=gid, left=MAX_Q, riddle=riddle)

@app.post("/ask")
def ask():
    g = games.get(request.json.get("id"))
    if not g or g["done"]:
        return jsonify(error="No active game"), 400
    try:
        answer = ai(host_prompt(g), request.json["question"][:200])
    except Exception as e:
        return busy_error(e)
    g["left"] -= 1
    won = answer.upper().startswith("CORRECT")
    lost = not won and g["left"] <= 0
    result = dict(answer=answer, left=g["left"], won=won, lost=lost)
    if won or lost:
        g["done"] = True
        result.update(secret=g["secret"], explanation=explain(g),
                      points=(g["level"]["points"] + g["left"]) if won else 0)
    return jsonify(result)

@app.post("/hint")
def hint():
    g = games.get(request.json.get("id"))
    if not g or g["done"]:
        return jsonify(error="No active game"), 400
    if g["left"] <= 2:
        return jsonify(error="Not enough questions left for a hint"), 400
    try:
        h = ai("You give helpful hints in a guessing game. Reply with only the hint, nothing else.",
               f"The secret answer is '{g['secret']}' (category: {g['category']}). "
               "Give ONE short, true, helpful hint in simple words that brings the players closer to the answer. "
               "Do not say the answer or any part of its name.")
    except Exception as e:
        return busy_error(e)
    g["left"] -= 2
    return jsonify(answer="💡 " + h, left=g["left"])

@app.post("/giveup")
def give_up():
    g = games.get(request.json.get("id"))
    if not g or g["done"]:
        return jsonify(error="No active game"), 400
    g["done"] = True
    return jsonify(secret=g["secret"], explanation=explain(g), won=False, points=0)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)