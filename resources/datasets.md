# Datasets to Practise On

The best way to learn machine learning is to work on data you care about. This page lists sources of **South Sudanese**, **African** and **global** data, with project ideas for each.

> **Before you start:** Always check each dataset's licence and terms of use, cite the source in your project, and never share personal or sensitive data about individuals.

---

## South Sudan

| Source | What's available | Link |
| --- | --- | --- |
| **National Bureau of Statistics (NBS)** | The official statistics agency. Publishes data on agriculture, population, prices (CPI), education, health, poverty, trade and more, plus statistical yearbooks and survey reports. Source of the IndabaX 2026 hackathon data | [nbs.gov.ss](https://nbs.gov.ss/) |
| **Humanitarian Data Exchange (HDX): South Sudan** | Hundreds of datasets on food security, displacement, health facilities, markets, floods and administrative boundaries, from UN agencies and NGOs | [data.humdata.org/group/ssd](https://data.humdata.org/group/ssd) |
| **World Bank Open Data: South Sudan** | Economic and development indicators over time (GDP, population, health, education) | [data.worldbank.org/country/south-sudan](https://data.worldbank.org/country/south-sudan) |
| **FEWS NET: South Sudan** | Food security outlooks, price bulletins and seasonal monitoring | [fews.net/east-africa/south-sudan](https://fews.net/east-africa/south-sudan) |
| **WFP HungerMap LIVE** | Near real-time food security indicators by country and region | [hungermap.wfp.org](https://hungermap.wfp.org/) |
| **Bank of South Sudan: Statistical Bulletin** | Exchange rates, inflation and monetary statistics | [bankofsouthsudan.org](https://bankofsouthsudan.org/) |

**Requesting data from NBS:** Not everything is published online. NBS accepts data requests through its website contact form or by email; state which data you need and how you'll use it. Student and research requests are common.

**Tip:** Many NBS and agency reports are PDFs, not spreadsheets. Extracting tables from PDFs into a clean CSV is a valuable skill and a good first project in itself. Try the `pdfplumber` or `camelot` Python libraries.

---

## Agriculture, climate and food security

These match the IndabaX 2026 hackathon theme: **forecasting agriculture and food security**.

| Source | What's available | Link |
| --- | --- | --- |
| **FAOSTAT** | Crop production, yields, land use, food prices and trade for every country, including South Sudan | [fao.org/faostat](https://www.fao.org/faostat/) |
| **CHIRPS rainfall data** | Satellite-based rainfall estimates from 1981 to near present, covering all of Africa | [chc.ucsb.edu/data/chirps](https://www.chc.ucsb.edu/data/chirps) |
| **NASA POWER** | Daily temperature, rainfall, humidity and solar data for any coordinates; easy to download as CSV | [power.larc.nasa.gov](https://power.larc.nasa.gov/) |

---

## African datasets and challenges

| Source | What's available | Link |
| --- | --- | --- |
| **Zindi** | Competition datasets on African problems: agriculture, health, finance, language, climate | [zindi.africa/competitions](https://zindi.africa/competitions) |
| **Lacuna Fund** | Funded, openly licensed datasets for African agriculture, health, climate and language | [lacunafund.org](https://lacunafund.org/) |
| **Masakhane** | Datasets and research for African languages | [masakhane.io](https://www.masakhane.io/) |

---

## Global practice datasets

| Source | What's available | Link |
| --- | --- | --- |
| **Kaggle Datasets** | Thousands of free datasets on every topic, many with example notebooks | [kaggle.com/datasets](https://www.kaggle.com/datasets) |
| **UCI Machine Learning Repository** | Classic, clean datasets widely used in courses | [archive.ics.uci.edu](https://archive.ics.uci.edu/) |
| **Hugging Face Datasets** | Text, audio and image datasets, especially for language models | [huggingface.co/datasets](https://huggingface.co/datasets) |
| **Google Dataset Search** | A search engine for datasets across the web | [datasetsearch.research.google.com](https://datasetsearch.research.google.com/) |

---

## Project ideas using local data

| Project | Data you could use | Skills you'll practise |
| --- | --- | --- |
| Predict crop yield by state from rainfall and temperature | NBS agriculture data + CHIRPS or NASA POWER | Merging datasets, regression, random forests |
| Forecast monthly food prices in Juba markets | WFP/HDX market prices, FEWS NET | Time series, feature engineering |
| Map flood-affected areas and displacement | HDX flood and displacement data | Data cleaning, visualisation, maps |
| Track inflation and exchange rates | Bank of South Sudan, NBS CPI | Time series charts, trend analysis |
| Compare school enrolment across states | NBS education statistics, World Bank | Exploratory analysis, storytelling with charts |
| Continue the IndabaX food security forecasting work | Hackathon dataset, updated NBS data for all states | Full ML pipeline, open-source collaboration |

**Share your project:** Post it on GitHub with a clear README, and present it at a Scenius Hub Tech Community meetup.
