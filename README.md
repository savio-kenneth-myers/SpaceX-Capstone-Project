# 🚀 SpaceX Falcon 9 - First Stage Landing Prediction
### IBM Applied Data Science Capstone Project

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat-square&logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=flat-square&logo=jupyter&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=flat-square&logo=pandas&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-F7931E?style=flat-square&logo=scikit-learn&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-Dashboard-3F4F75?style=flat-square&logo=plotly&logoColor=white)

---

## 📌 Project Overview

SpaceX advertises Falcon 9 rocket launches at **$62 million**, significantly undercutting competitors who charge upwards of **$165 million** per launch. The key to this cost advantage is the **reuse of the Falcon 9 first stage booster**.

> **Goal:** Predict whether the Falcon 9 first stage will successfully land after launch - enabling competitors to estimate SpaceX's launch cost and make informed bidding decisions.

---

## 🗂️ Project Structure

```
SpaceX-Capstone-Project/
│
├── 📓 SpaceX_API_Data_Collection.ipynb       # Lab 1 - Data Collection via REST API
├── 📓 SpaceX_Web_Scrapping.ipynb             # Lab 2 - Web Scraping with BeautifulSoup
├── 📓 SpaceX_Data_Wrangling.ipynb            # Lab 3 - Data Wrangling & Cleaning
├── 📓 SpaceX_EDA_DataViz.ipynb               # Lab 4 - Exploratory Data Analysis
├── 📓 SpaceX_EDA_SQL.ipynb                   # Lab 5 - EDA with SQL Queries
├── 📓 SpaceX_Folium_Map.ipynb                # Lab 6 - Interactive Maps with Folium
├── 🐍 SpaceX_Dash_App.py                     # Lab 7 - Interactive Dashboard (Plotly Dash)
├── 📓 SpaceX_Machine_Learning_Prediction.ipynb # Lab 8 - Predictive Modeling (ML)
│
├── 📄 dataset_part_1.csv                     # Cleaned API dataset
└── 📄 spacex_web_scraped.csv                 # Cleaned web scraped dataset
```

---

## 🔬 Methodology

### 1. 📡 Data Collection
- **REST API** - Called the SpaceX API (`api.spacexdata.com/v4/launches/past`) to collect 90+ past launch records including rocket type, payload, launch site, and landing outcome
- **Web Scraping** - Used `BeautifulSoup` to scrape Falcon 9 launch history tables from Wikipedia

### 2. 🧹 Data Wrangling
- Filtered out Falcon 1 launches - kept only Falcon 9
- Replaced missing `PayloadMass` values with the column mean
- Applied One Hot Encoding for categorical variables
- Created binary `Class` column: `1 = landed`, `0 = did not land`

### 3. 📊 Exploratory Data Analysis
- Visualized launch success trends over time
- Analysed relationships between payload mass, orbit type, and landing success
- Used SQL queries to extract insights on launch sites, payload ranges, and booster versions

### 4. 🗺️ Interactive Visual Analytics
- Built **Folium maps** showing launch site locations, proximities to coastlines, railways, and highways
- Built a **Plotly Dash dashboard** with:
  - Dropdown to filter by launch site
  - Pie chart showing success/failure counts
  - Range slider to filter by payload mass
  - Scatter plot showing payload vs. landing outcome by booster version

### 5. 🤖 Predictive Modeling
Trained and tuned **4 classification models** using GridSearchCV:

| Model | Description |
|---|---|
| Logistic Regression | Baseline linear classifier |
| Support Vector Machine (SVM) | Maximum margin classifier |
| Decision Tree | Rule-based tree classifier |
| K-Nearest Neighbors (KNN) | Distance-based classifier |

---

## 📈 Key Findings

| Question | Finding |
|---|---|
| Site with most successful launches | **KSC LC-39A** |
| Site with highest success rate | **KSC LC-39A (76.9%)** |
| Best payload range for success | **2,000 - 4,000 kg** |
| Worst payload range | **0 - 2,000 kg (early launches)** |
| Best booster version | **FT (Full Thrust)** |

---

## 🛠️ Technologies Used

| Category | Tools |
|---|---|
| Language | Python 3.8+ |
| Data Collection | `requests`, `BeautifulSoup4` |
| Data Analysis | `pandas`, `numpy` |
| Visualization | `matplotlib`, `seaborn`, `plotly` |
| Interactive Maps | `folium` |
| Dashboard | `Plotly Dash` |
| Machine Learning | `scikit-learn` |
| Database | `SQLite`, `SQL Magic` |
| Environment | Jupyter Notebook, VS Code |

---

## ⚙️ How to Run

### 1. Clone the repository
```bash
git clone https://github.com/savio-kenneth-myers/SpaceX-Capstone-Project.git
cd SpaceX-Capstone-Project
```

### 2. Install required packages
```bash
pip install pandas numpy matplotlib seaborn plotly dash folium scikit-learn beautifulsoup4 requests
```

### 3. Run the Jupyter notebooks
```bash
jupyter notebook
```
Open each `.ipynb` file in order (Lab 1 through Lab 8).

### 4. Run the interactive dashboard
```bash
python SpaceX_Dash_App.py
```
Then open your browser at: `http://127.0.0.1:8050`

---

## 📊 Dashboard Preview

The interactive dashboard allows users to:
- **Filter by launch site** using a searchable dropdown
- **View success rates** as a pie chart per site or all sites combined
- **Adjust payload range** using a slider (0 - 10,000 kg)
- **Explore correlations** between payload mass and launch success coloured by booster version

---

## 🎓 Course Information

| Detail | Info |
|---|---|
| Course | IBM Applied Data Science Capstone |
| Platform | Coursera |
| Instructors | Joseph Santarcangelo, Yan Luo, Azim Hirjani |
| Certificate | IBM Data Science Professional Certificate |

---

## 👤 Author

**Savio Kenneth Myers**
- GitHub: [@savio-kenneth-myers](https://github.com/savio-kenneth-myers)

---

## 📄 License

This project is for educational purposes as part of the IBM Data Science Professional Certificate on Coursera.

---

*Built with ❤️ as part of the IBM Applied Data Science Capstone*
