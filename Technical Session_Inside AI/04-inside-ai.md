# Inside AI: How It Works, What It Can Do, and Where It Falls Short

## About the session

"Inside AI" was the technical session at IndabaX South Sudan 2026, held on Thursday, 1 October 2026 at Scenius Hub, Juba. In 45–60 minutes it took participants from a plain definition of AI to training a real model in Python, then to the limits and ethics of the technology.

The session followed seven parts: what AI is, how machines learn, neural networks and deep learning, how ChatGPT and other large language models (LLMs) work, a live coding demo, ethics and shortfalls, and where to start learning. Every concept was tied back to a South Sudanese example, from crop yields to flood warnings.

## What AI is, and what it could do here

AI is the science of making computers do tasks that normally need human intelligence: seeing, hearing, understanding language, learning and deciding. Everything in use today is narrow AI, excellent at one task. General AI, which would reason across any task like a person, remains an idea, not a product.

Most participants had already used AI that morning: Google Maps traffic, face unlock, WhatsApp auto-correct, spam filters, social media feeds and ChatGPT. AI itself is not new. Turing asked whether machines can think in 1950 and the term was coined at Dartmouth in 1956; what changed recently is more data, faster computers and better algorithms.

| AI can…            | How South Sudan could use it                                                                             | Sector                |
|--------------------|----------------------------------------------------------------------------------------------------------|-----------------------|
| See                | Spot crop and cattle disease from a phone photo; track floods from satellite images (Bentiu Flood Watch) | Farming, disasters    |
| Hear               | Voice assistants in Juba Arabic, Dinka or Nuer                                                           | Inclusion, services   |
| Understand & write | Translate health, legal and government information into local languages                                  | Health, justice       |
| Predict            | Forecast floods, dry spells, crop yields and cholera outbreaks                                           | Food security, health |
| Recommend          | Personalised lessons; match young people with jobs and training                                          | Education, jobs       |
| Create             | Learning materials and radio content in local languages                                                  | Education, media      |


## How machines learn

The big shift is from rules to learning. In traditional programming a person writes the rules and the computer applies them: rules + data → answers. In machine learning (ML) we give the computer examples with answers and it works out the rules: data + answers → rules. A spam filter that blocks every email with "lottery" is rules; one that learns from millions of emails people marked as spam is ML. Simple fixed tasks, like adding up a bill, stay with rules.

The session framed ML around three components:

- **Data** — examples turned into numbers. An image becomes a grid of pixel values from 0 (black) to 255 (white). Each example has an input (features) and a label (the answer we want to predict).

- **Models** — a function f(x) that maps an input to an output, controlled by parameters that act like adjustable knobs. For a farm, the input might be rainfall, temperature and fertiliser; the output, crop yield.

- **Learning** — tuning those knobs to shrink a loss function, L(f(x), y), which measures the gap between prediction and reality.

$$
\min_{\theta} \sum_{(x,y) \in X} L\big(f(x;\theta),\, y\big)
$$

In practice, training is a loop: guess, measure the error, adjust, repeat thousands of times. Some data is held back as "secret exam questions", because the real goal is generalisation: working on a farm or a season the model has never seen.

| Type              | How it learns                                           | Everyday examples                                                       |
|-------------------|---------------------------------------------------------|-------------------------------------------------------------------------|
| Supervised        | From labelled examples                                  | Face unlock, spam filters, spotting crop disease, predicting crop yield |
| Unsupervised      | Finds groups and patterns with no labels                | Grouping customers, flagging unusual mobile money transactions          |
| Reinforcement     | Trial, reward and penalty                               | Game AI for chess and Go, robots, ChatGPT improved with human feedback  |
| Semi-supervised   | A few labels plus many unlabelled examples              | Useful when labelling is costly                                         |
| Self-supervised   | Creates its own labels, e.g. hide a word and predict it | How ChatGPT-style models are pre-trained                                |
| Transfer learning | Fine-tunes a model already trained on big data          | Adapting global models to local languages                               |

Transfer learning got special emphasis: it lets South Sudan adapt large global models to local languages and data without starting from zero. Participants also toured common models, from linear regression and decision trees to random forests and XGBoost, the top choice in Zindi and Kaggle contests.

## Live demo: predicting a farm's crop yield

The theory became real in a few lines of Python in Google Colab. Participants watched a random forest learn to predict a farm's yield in tonnes from rainfall, temperature and fertiliser use, the same agriculture and food-security theme as the IndabaX hackathon.

import pandas as pd  
from sklearn.model_selection import train_test_split  
from sklearn.ensemble import RandomForestRegressor  
  
```python
X = data[["rainfall_mm", "temperature_c", "fertiliser_kg"]]
y = data["yield_tonnes"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = RandomForestRegressor()
model.fit(X_train, y_train)          # learning happens here
predictions = model.predict(X_test)  # test on unseen farms
```

The four steps map straight onto the theory: load data, split into train and test, train with fit, then test and predict on farms the model has never seen. The notebook is open to anyone: [crop yield demo in Colab](https://colab.research.google.com/drive/1XMYuu7cs6XB_zECGxzSbY4Movc78N_MM?usp=sharing).

## Neural networks, deep learning and LLMs

A neural network is many simple units connected in layers. Each neuron takes numbers in, weighs how important each one is, adds them up and passes the result on. Data enters at the input layer, learning happens in the hidden layers, and the answer comes out at the output. After every mistake each weight is nudged slightly, a process called backpropagation.

Deep learning means many such layers, and depth is why these networks can "see". Early layers spot edges and colours, middle layers combine them into shapes and textures, and later layers recognise the whole object. A farmer photographs a cassava or sorghum leaf and the app names the disease; similar models identify snake species from photos to guide treatment.

| Network           | What it does                                      | Example                                        |
|-------------------|---------------------------------------------------|------------------------------------------------|
| Feedforward (MLP) | Data flows straight from input to output          | Crop yield or loan risk from a table           |
| CNN               | Scans images in small patches                     | Face unlock, crop disease in leaf photos       |
| RNN / LSTM        | Reads data in order, remembers what came before   | Early speech recognition, rainfall forecasting |
| Transformer       | "Attention" weighs every word against every other | ChatGPT, Google Translate                      |
| GAN               | One network fakes, another spots fakes            | Realistic faces, deepfakes                     |
| Diffusion         | Turns random noise into an image step by step     | AI image generators                            |

Large language models like ChatGPT rest on one trick: predict the next word. Given "The capital of South Sudan is", the model predicts "Juba", building whole answers one token at a time. Pre-training on billions of pages teaches grammar, facts and patterns of reasoning; fine-tuning with human feedback makes it helpful and able to follow instructions.

LLMs can explain, summarise, translate, draft and brainstorm. They cannot reliably guarantee facts (they hallucinate), truly understand what they say, or work well in most South Sudanese languages.

## Where AI falls short, and the gaps at home

AI is powerful but imperfect. The session named five shortfalls, each with a local face:

| Shortfall             | What it means                        | Example                                                          |
|-----------------------|--------------------------------------|------------------------------------------------------------------|
| Bias                  | Repeats unfair patterns in its data  | A loan model trained on urban customers rejects rural applicants |
| Hallucinations        | States false information confidently | ChatGPT inventing a source or statistic                          |
| Poor local fit        | Models trained elsewhere fail here   | A crop app misreading South Sudanese varieties                   |
| Language exclusion    | Little data in local languages       | Voice tools that fail outside English and Arabic                 |
| No real understanding | Patterns without common sense        | Fooled by small image changes a human would ignore               |

Beyond accuracy sit wider risks: privacy and consent, deepfakes spreading fast in elections, accountability when AI causes harm, jobs and skills, honesty in using AI's work, and data sovereignty, meaning African data should benefit African communities.

South Sudan faces specific gaps: very little digitised local data and almost none in Dinka, Nuer, Bari or Juba Arabic; expensive, patchy internet and power cuts; few GPUs, with cloud tools often needing international cards; few AI courses or trainers; no national AI strategy yet; and little investment in local AI startups. The session's answer was that every gap is also an opportunity for the people in the room.

**For builders:** use local, representative data; always check outputs; protect data and ask for consent; keep humans in the loop for big decisions; build for South Sudanese languages.

**For students:** use AI to learn, not to copy; check facts before sharing; never put personal data or others' photos into AI tools; don't create or spread deepfakes; build projects that solve community problems.

## The community behind it: Deep Learning Indaba and Zindi

The session closed by pointing participants to the two African communities that made the day possible.

The [Deep Learning Indaba](https://deeplearningindaba.com/about/) is a movement to strengthen machine learning and AI in Africa, so that Africans are builders of AI, not just observers. "Indaba" means a gathering to discuss important matters in isiZulu. Its first annual meeting was in Johannesburg in 2017, and it has since moved across the continent, including Kenya, Tunisia, Ghana, Senegal and Rwanda. [IndabaX](https://deeplearningindaba.com/2025/indabax/) brings the same spirit to locally organised country events, growing from 13 events in 2018 to between 36 and 47 countries in 2023–2024. IndabaX South Sudan 2026 is part of that network. Its [awards](https://deeplearningindaba.com/2025/awards/), including the Kambule Doctoral Award and the Maathai Impact Award, celebrate African research and impact, and a [mentorship programme](https://deeplearningindaba.com/mentorship/) supports emerging researchers.

[Zindi](https://zindi.world/about), founded in 2018, is an AI challenge platform for data scientists in Africa and emerging markets, with members in more than 185 countries. Companies, NGOs and governments set real problems, often with prizes, and participants build a portfolio employers can see; Zindi reports that 1 in 5 users got a data science or AI job because of their profile. The IndabaX South Sudan hackathon on crop-yield and food-security forecasting ran on Zindi.

The session ended where it began: AI could shape South Sudan's future, so South Sudanese should help build it, starting today.

## Sources and references

- Poni Henry, "Inside AI: How it works, what it can do, and where it falls short", session slides, IndabaX South Sudan 2026, Scenius Hub, Juba, 1 October 2026.

- [Crop yield demo notebook](https://colab.research.google.com/drive/1XMYuu7cs6XB_zECGxzSbY4Movc78N_MM?usp=sharing), Google Colab.

- Deisenroth, Faisal and Ong, [Mathematics for Machine Learning](https://mml-book.github.io/), Cambridge University Press, 2020 — the data, models and learning framing.

- [Deep Learning Indaba: About](https://deeplearningindaba.com/about/)

- [Deep Learning Indaba: IndabaX](https://deeplearningindaba.com/2025/indabax/)

- [Deep Learning Indaba: Awards](https://deeplearningindaba.com/2025/awards/)

- [Zindi: About](https://zindi.world/about)

- [Masakhane](https://www.masakhane.io/)

## Learn more

| Resource             | What you get                                               | Link                                                                       |
|----------------------|------------------------------------------------------------|----------------------------------------------------------------------------|
| Deep Learning Indaba | Annual meeting, applications, news                         | [deeplearningindaba.com](https://deeplearningindaba.com/)                  |
| Indaba practicals    | Free deep learning notebooks from past Indabas (2017–2025) | [github.com/deep-learning-indaba](https://github.com/deep-learning-indaba) |
| Indaba mentorship    | Mentoring for African ML students and researchers          | [Mentorship programme](https://deeplearningindaba.com/mentorship/)         |
| Zindi                | African data science competitions and beginner challenges  | [zindi.africa](https://zindi.africa)                                       |
| Masakhane            | NLP research for African languages                         | [masakhane.io](https://www.masakhane.io/)                                  |
| Google Colab         | Free Python notebooks with GPU                             | [colab.research.google.com](https://colab.research.google.com/)            |
| Kaggle Learn         | Short hands-on ML courses                                  | [kaggle.com/learn](https://www.kaggle.com/learn)                           |
| MIT Learn            | Free MIT courses on AI and ML                              | [learn.mit.edu](https://learn.mit.edu/)                                    |
| Scenius Hub          | Local meetups and hackathons in Juba                       | Scenius Hub, Juba                                                          |
