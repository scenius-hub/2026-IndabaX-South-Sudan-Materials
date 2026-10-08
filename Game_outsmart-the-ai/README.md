# Outsmart the AI (free Gemini version)

The AI secretly picks something from a category. Players have 20 yes/no questions to guess it. A hint costs 2 questions.

## Get a free API key
1. Go to https://aistudio.google.com and sign in with a Google account.
2. Click "Get API key" -> "Create API key". No credit card needed.

## Run it in VS Code
1. File -> Open Folder -> choose this folder.
2. Open the terminal: Ctrl + ` (backtick).
3. Install: `pip install -r requirements.txt`
4. Set your key (PowerShell): `$env:GEMINI_API_KEY="your_key_here"`
   (Mac/Linux: `export GEMINI_API_KEY=your_key_here`)
5. Start: `python app.py`
6. Open http://localhost:5000

## Playing at an event
Players on the same Wi-Fi can join at `http://<your-laptop-IP>:5000`.
The free tier limits requests per minute, so with a big group, project ONE screen and let teams take turns.
If you see "The AI is busy", wait a minute and try again.

## Troubleshooting
- Model not found error: set a current model name from AI Studio, e.g.
  `$env:GEMINI_MODEL="gemini-2.5-flash"` then run `python app.py` again.
- Note: on the free tier, Google may use prompts to improve its models, so don't type personal info into the game.

## Customising
- Categories: edit the `CATS` list in `index.html`.
- Number of questions: change `20` in `app.py`.
