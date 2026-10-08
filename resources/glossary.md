# Glossary: AI and ML Terms in Plain Language

Terms you heard during IndabaX South Sudan 2026 sessions, explained simply. Where possible, examples use the crop yield model from the hands-on workshop.

---

## Core ideas

**Artificial Intelligence (AI)**
Computer systems that perform tasks that normally need human intelligence, such as recognising speech, translating languages, making predictions or answering questions.

**Machine Learning (ML)**
A type of AI where computers learn patterns from data instead of following rules written by a programmer. Instead of telling the computer "if rainfall is high, yield is high," you show it many examples and it works out the pattern itself.

**Deep Learning**
A type of machine learning that uses neural networks with many layers. It powers image recognition, speech recognition and large language models.

**Algorithm**
A step-by-step method for solving a problem. In ML, the algorithm is the method used to learn from data (for example, a random forest).

**Model**
What you get after an algorithm learns from data. It takes inputs and produces predictions. In the workshop, the model takes rainfall, temperature and fertiliser and predicts crop yield.

---

## Data

**Dataset**
A collection of data, usually organised as a table where each row is one example (a farm) and each column is a piece of information about it (rainfall, temperature).

**Features (X)**
The inputs the model uses to make a prediction. In the workshop: `rainfall_mm`, `temperature_c` and `fertiliser_kg`.

**Target / Label (y)**
What the model is trying to predict. In the workshop: `yield_tonnes`.

**Training set**
The part of the data the model learns from, usually about 80%.

**Test set**
Data held back and never shown to the model during training, usually about 20%. It checks how well the model performs on examples it hasn't seen, like testing on new farms.

**Data cleaning**
Fixing problems in data before using it: filling or removing missing values, correcting errors and making formats consistent. Often the most time-consuming part of any project.

**Feature engineering**
Creating new, more useful inputs from existing data. For example, turning daily rainfall into "total rainfall during the planting season."

---

## Training and learning

**Training**
The process of a model learning patterns from data. In code, this happens at `model.fit(X_train, y_train)`.

**Parameters (θ, theta)**
The internal values a model adjusts as it learns. Training means finding the parameter values that make the best predictions.

**Loss function (L)**
A way of measuring how wrong the model's predictions are. Smaller loss means better predictions. Training tries to make the total loss as small as possible:

$$
\min_{\theta} \sum_{(x,y) \in X} L\big(f(x;\theta),\, y\big)
$$

In words: find the parameters θ that make the total error between the model's predictions f(x; θ) and the true answers y as small as possible, across all examples in the dataset.

**Prediction / Inference**
Using a trained model to produce an output for new input. In code: `model.predict(X_test)`.

**Overfitting**
When a model memorises the training data instead of learning general patterns. It scores very well on training data but badly on new data, like a student who memorises past exam answers but can't solve new questions.

**Underfitting**
When a model is too simple to capture the pattern, so it performs badly on both training and test data.

---

## Types of machine learning

**Supervised learning**
Learning from examples that include the correct answer (label). The workshop model is supervised: each farm in the data includes its actual yield.

**Unsupervised learning**
Finding patterns in data without labels, for example grouping markets with similar price patterns.

**Regression**
Predicting a number, such as crop yield in tonnes or tomorrow's food price.

**Classification**
Predicting a category, such as "drought risk: high / medium / low" or "spam / not spam."

---

## Models and algorithms

**Decision tree**
A model that makes predictions by asking a series of yes/no questions, like a flowchart: "Is rainfall above 600 mm? Is fertiliser above 50 kg?"

**Random forest**
A model that builds many decision trees on different samples of the data and averages their answers. Usually more accurate and less likely to overfit than a single tree. Used in the workshop.

**Neural network**
A model loosely inspired by the brain, made of layers of connected "neurons" that each do a small calculation. Many layers together can learn very complex patterns.

---

## Evaluation

**Accuracy**
For classification, the percentage of predictions that are correct.

**Mean Absolute Error (MAE)**
For regression, the average size of the errors. An MAE of 0.5 means predictions are off by 0.5 tonnes on average.

**Root Mean Squared Error (RMSE)**
Like MAE, but it punishes large errors more. Commonly used to score Zindi competitions.

**Cross-validation**
Testing a model several times on different splits of the data to get a more reliable measure of performance.

---

## Large language models and generative AI

**Large Language Model (LLM)**
A very large neural network trained on huge amounts of text to predict the next word. This simple task lets it write, summarise, translate and answer questions. Examples include Gemini and Claude.

**Generative AI**
AI that creates new content (text, images, audio or code) rather than only making predictions or classifications.

**Token**
A small piece of text (a word or part of a word) that a language model reads and writes. Model limits and costs are usually counted in tokens.

**Prompt**
The instruction or question you give an AI model. Clear, specific prompts with examples usually get better answers.

**Hallucination**
When an AI model produces information that sounds confident but is false or made up. A key reason to verify AI output, as discussed in the "Inside AI" session.

**Bias**
When a model's outputs are systematically unfair or inaccurate for certain groups, often because of gaps or imbalances in its training data. Models trained mostly on data from other countries may perform worse on South Sudanese contexts.

**API (Application Programming Interface)**
A way for one program to talk to another. The "Outsmart the AI" game uses the Gemini API to send questions to Google's model and get answers back.

---

## Tools

**Python**
The most widely used programming language for AI and ML.

**Jupyter Notebook**
A document that mixes code, results, charts and explanations. The workshop materials are notebooks (`.ipynb` files).

**Google Colab**
A free, browser-based service for running Jupyter notebooks on Google's computers.

**Library**
A collection of ready-made code you can reuse. Examples: pandas (data), scikit-learn (machine learning).

**GPU (Graphics Processing Unit)**
A processor that can do many calculations at once, which makes training neural networks much faster. Colab offers free GPU access.
