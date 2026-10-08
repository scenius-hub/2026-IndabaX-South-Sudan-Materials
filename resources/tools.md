# Tools and Platforms

These are the tools used during IndabaX South Sudan 2026, plus a few more you'll need as you build your own projects. All are free.

---

## Google Colab: run notebooks in the browser

**What it is:** A free Jupyter notebook environment that runs on Google's computers. You don't install anything, and you get access to free GPUs for heavier models.

**Used at IndabaX for:** The hands-on ML workshop notebook and the Inside AI demo.

**Link:** [colab.research.google.com](https://colab.research.google.com/)

**Getting started:**
1. Sign in with a Google (Gmail) account.
2. Open the workshop notebook from this repository: on GitHub, open the `.ipynb` file and use **File → Upload notebook** in Colab, or open it directly from GitHub via **File → Open notebook → GitHub**.
3. Run each cell with **Shift + Enter**, from top to bottom.
4. Save your own copy with **File → Save a copy in Drive** so your changes aren't lost.

**Tips:**
- Free sessions disconnect after a period of inactivity. Save often.
- Turn on a GPU when training neural networks: **Runtime → Change runtime type → T4 GPU**. You don't need it for the workshop's random forest model.
- To use your own data, upload a CSV with the folder icon on the left, or mount Google Drive.

---

## Python libraries

All of these come pre-installed in Google Colab.

| Library | What it does | Docs |
| --- | --- | --- |
| **pandas** | Load, clean, filter and summarise tables of data | [pandas.pydata.org/docs](https://pandas.pydata.org/docs/) |
| **NumPy** | Fast maths on arrays of numbers; used under the hood by most ML libraries | [numpy.org/doc](https://numpy.org/doc/) |
| **scikit-learn** | Classic machine learning: train/test splits, random forests, regression, evaluation | [scikit-learn.org](https://scikit-learn.org/stable/) |
| **Matplotlib** / **Seaborn** | Charts and visualisations | [matplotlib.org](https://matplotlib.org/) · [seaborn.pydata.org](https://seaborn.pydata.org/) |
| **TensorFlow** / **PyTorch** | Deep learning and neural networks | [tensorflow.org](https://www.tensorflow.org/) · [pytorch.org](https://pytorch.org/) |

**The basic workflow from the workshop:**

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

data = pd.read_csv("your_data.csv")

X = data[["rainfall_mm", "temperature_c", "fertiliser_kg"]]
y = data["yield_tonnes"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestRegressor(random_state=42)
model.fit(X_train, y_train)            # learning happens here

predictions = model.predict(X_test)    # test on unseen farms
print("Mean absolute error:", mean_absolute_error(y_test, predictions))
```

---

## Gemini API and Google AI Studio: build with AI models

**What it is:** Google's API for its Gemini models. Google AI Studio is the web interface where you can try prompts and get an API key.

**Used at IndabaX for:** The "Outsmart the AI" guessing game (Flask + Gemini API).

**Links:** [aistudio.google.com](https://aistudio.google.com/) · [ai.google.dev](https://ai.google.dev/)

**Getting started:**
1. Sign in to Google AI Studio with a Google account.
2. Experiment with prompts in the browser first, with no code needed.
3. Create an API key when you're ready to call the model from Python.
4. Install the SDK and follow the quickstart at [ai.google.dev](https://ai.google.dev/).

**Important:**
- **Never put your API key in a notebook or file you share or upload to GitHub.** Store it in an environment variable or Colab's **Secrets** (key icon on the left).
- Free-tier limits and available models change over time; check the docs for current limits.

---

## Flask: turn your Python code into a web app

**What it is:** A lightweight Python web framework. Good for wrapping a model or an AI feature in a simple web page.

**Used at IndabaX for:** The "Outsmart the AI" game.

**Docs:** [flask.palletsprojects.com](https://flask.palletsprojects.com/)

---

## GitHub: save, share and show your work

**What it is:** A platform for storing code and tracking changes. Your GitHub profile acts as your portfolio.

**Link:** [github.com](https://github.com/) · Beginner guide: [docs.github.com/en/get-started](https://docs.github.com/en/get-started)

**What to do first:**
1. Create an account with a professional username.
2. Make a repository for each project, with a `README.md` explaining what it does, the data used and the results.
3. Upload notebooks directly through the website if you don't know Git yet; learn Git commands later.
4. **Star** and **fork** this repository so you can find the IndabaX materials again.

---

## Zindi and Kaggle: competitions and datasets

| Platform | Why use it | Link |
| --- | --- | --- |
| **Zindi** | Africa's data science competition platform; hosted the IndabaX South Sudan 2026 hackathon | [zindi.africa](https://zindi.africa/) |
| **Kaggle** | The largest global data science community; free notebooks, datasets and courses | [kaggle.com](https://www.kaggle.com/) |

See [communities.md](communities.md) for how to get started with competitions.

---

## Working with low bandwidth or a basic device

- **Colab does the heavy lifting.** Your device only needs to run a browser.
- **Download course videos** in advance on Wi-Fi where the course allows it.
- **Install Anaconda or Miniconda** ([anaconda.com](https://www.anaconda.com/)) if you want to work fully offline. It includes Python, Jupyter, pandas and scikit-learn in one install.
- **Use small datasets** while learning. You don't need millions of rows to understand how a model works.
- **Use Scenius Hub's space** for reliable internet and power when you need to download or train something big.
