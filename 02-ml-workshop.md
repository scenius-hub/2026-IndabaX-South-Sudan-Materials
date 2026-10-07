# From First Code to First Model: Inside the IndabaX South Sudan 2026 Machine Learning Workshop

*Poni Henry · 5 October 2026*

On Thursday, 24 September 2026, a room full of young South Sudanese, most of them writing machine learning code for the first time, left having trained their own models. The one-day, in-person *Introduction to Machine Learning* workshop at Twenty11 Hub in Juba was the first hands-on step of **IndabaX South Sudan 2026**, organised by Scenius Hub.

The goal was simple: take participants from "What is machine learning?" to a working model in one morning. That way, they would be ready to compete in the IndabaX hackathon on **Zindi**, which focused on agriculture and food security forecasting.

## Who came

Interest was strong: **96 people registered** in just nine days, and **79 were confirmed** for the limited seats.

Most were new to the field. Of those who registered:

| Group | Share of registrants |
| --- | --- |
| Students | 71% (67 of 95) |
| Complete beginners in ML | 68% (65 of 95) |
| Developers, researchers and tech professionals | 26% (25 of 95) |
| Women | 25% (22 of 88) |

Their goals were practical. Many said they wanted to learn the basics, build their first model, and use ML to solve real problems in agriculture, health and development in South Sudan.

## What they learned and built

The whole workshop ran in **Google Colab**, so participants only needed a browser, with no software to install. Facilitators guided the room through the full machine learning workflow, one step at a time:

1. **Define the problem.** What are we predicting, and why does it matter?
2. **Explore the data.** Charts showing how rainfall, fertiliser and soil quality relate to crop yield.
3. **Clean and prepare it.** Filling in missing values and turning text categories like region and crop into numbers.
4. **Split it.** Keeping 20% of the data hidden so the model is tested honestly.
5. **Train and evaluate.** Building models and checking how good their predictions are.

The dataset was designed to feel local: farm plots across all ten states of South Sudan, growing sorghum, maize, groundnuts and cassava. Participants built two kinds of models:

- **Regression:** predicting crop yield (kg per hectare) using Linear Regression and Random Forest.
- **Classification:** predicting whether a household's food security risk is Low, Medium or High.

In the last part, participants took over. They tried a Decision Tree, created new features, and saw how changing the data split affects results. These are the same skills they used in the hackathon.

The full notebook is in this repository: [workshop/](https://colab.research.google.com/drive/13gnA9mJ4fD6cMCwo6cUmvEiTdsUsHqcK?usp=sharing).

## Getting ready for Zindi

Building a model is only half the challenge. To compete, participants also need to know how to submit their work. The workshop introduced **Zindi**, Africa's largest data science competition platform, where the IndabaX South Sudan hackathon was hosted.

Participants walked through the platform together:

- Creating a Zindi account and finding the competition
- Downloading the competition data
- Making a submission file from their model's predictions
- Uploading it and seeing their score on the leaderboard

## What participants said

**7 of 8** participants who completed the feedback form said they now feel confident, or more confident, about machine learning. Facilitation scored **4.4 out of 5**, and the workshop overall scored **3.9 out of 5**.

> "From beginner to being able to build a mini model." — Alek Madut Malual

> "Machine learning was a rumour to me. I left the training rich in knowledge and practical skills." — Gabriel Garang Garang

> "The presenters effectively demystified the complex concepts of ML." — Mohamed Musa

> "Practical, relevant to South Sudan, and well organised." — Deng John Aguin

Participants were also honest about what could be better. They asked for **more time for hands-on practice**, a **slower pace** for complete beginners, **more facilitators** to support groups, and **stronger internet** for Colab.

## What's next

The workshop was the **Learn** stage of IndabaX South Sudan 2026's journey: **Learn → Engage → Build → Showcase**. Participants went on to the hackathon on Zindi (24–30 September 2026), using the same steps they practised in the workshop. Read the full event story: [IndabaX South Sudan 2026 recap](01-event-recap.md).

Want to keep learning? Free resources include the [scikit-learn documentation](https://scikit-learn.org/stable/) and [Kaggle Learn](https://www.kaggle.com/learn). More in [resources/](../resources/).

Thank you to everyone who took part, to our facilitators, to Twenty11 Hub, and to our partners at Zindi.
