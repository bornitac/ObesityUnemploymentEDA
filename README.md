# Obesity and Unemployment Data Analysis

An exploratory data analysis (EDA) of U.S. state-level datasets on obesity, poverty, income, and unemployment from 2019–2023. The analysis merges two public datasets, cleans and aggregates the data by state, and generates visualizations to explore potential correlations between obesity and unemployment rates.

---

## 🔍 What It Does

- Loads and cleans two public datasets from Kaggle covering U.S. obesity/poverty/income and unemployment data
- Removes duplicates and handles missing values across both datasets
- Merges datasets by state using a join on the State index
- Groups and aggregates average obesity and unemployment rates by state
- Generates and exports bar chart visualizations as image files

---

## 📊 Key Findings

- Alabama had the highest obesity rate among the first 5 states at approximately 38%
- California had the lowest obesity rate among the first 5 states at approximately 27%
- Alaska had the highest unemployment rate among the first 5 states at approximately 7.8%
- Arizona and Arkansas had similar unemployment rates at approximately 6%
- The analysis explores whether higher unemployment correlates with higher obesity rates, given that junk food tends to be cheaper than fresh produce

---

## 🛠️ Built With

- **Python** – core scripting
- **Pandas** – data loading, cleaning, merging, and aggregation
- **Matplotlib** – data visualization and chart export

---

## 🚀 Getting Started

### Prerequisites
```bash
pip install pandas matplotlib
```

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/bornitac/ObesityUnemploymentEDA
   ```
2. Place the datasets in the same folder as `dataanalysis.py`
3. Run the script:
   ```bash
   python dataanalysis.py
   ```

---

## 📂 Data Sources

- **Obesity, Poverty, and Income in U.S. (2019–2023)** — Kaggle
  🔗 https://www.kaggle.com/datasets/geomontes/obesity-poverty-and-income-in-u-s-20192023

- **Unemployment in America, Per US State** — Kaggle
  🔗 https://www.kaggle.com/datasets/justin2028/unemployment-in-america-per-us-state
