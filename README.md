# 🏏 IPL Ball-by-Ball Data Analytics & Interactive Dashboard

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.56%2B-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Plotly](https://img.shields.io/badge/Plotly-Interactive%20Charts-3F4F75?logo=plotly&logoColor=white)](https://plotly.com/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Project](https://img.shields.io/badge/IBM%20Internship-Data%20Analytics-052FAD?logo=ibm&logoColor=white)](https://www.ibm.com/)

A comprehensive, end-to-end Python data analytics project that cleans, models, and visualizes IPL delivery-level cricket data through an interactive, executive-grade Streamlit analytics dashboard.

---

## 📌 Project Overview

This project transforms raw delivery-level IPL data into actionable cricket performance insights using Python. It follows a structured end-to-end data analytics pipeline:

$$\text{Raw Dataset} \longrightarrow \text{Data Cleaning} \longrightarrow \text{Feature Engineering} \longrightarrow \text{EDA} \longrightarrow \text{Interactive Dashboard}$$

### Key Highlights:
- **Interactive Web Dashboard:** Real-time filtering by Batting Team and Innings ID with instant KPI calculations and dynamic charts.
- **Executive Styling:** Polished dark-slate aesthetic with customized KPI metrics, smooth hover micro-animations, and unified Plotly visualizations.
- **Delivery-Level Exploration:** In-depth breakdown of dot balls, boundaries (4s & 6s), dismissal types, extra runs, and over-by-over run rates.
- **Comprehensive Project Documentation:** Includes full Jupyter notebook analysis and an official project report document.

> 📝 **Dataset Note:** The official dataset records entities via numeric IDs (`Team_Batting_Id`, `Striker_Id`, `Bowler_Id`, etc.). To maintain data integrity without unverified third-party assumptions, analyses are displayed using verified dataset IDs.

---

## 📂 Project Structure

```text
IPL_Ball_by_Ball_IBM_Project/
│
├── .gitignore                                       # Specifies files and folders untracked by Git
├── Ball_by_Ball.csv                                 # Official IPL ball-by-ball delivery-level dataset
├── Harshavardhn_Patil_IPL_IBM_ProjectReport.docx   # Official IBM Internship project report with documentation
├── IPL_Ball_by_Ball_IBM_Project.ipynb              # Jupyter Notebook with end-to-end data exploration & EDA
├── README.md                                        # Complete project documentation and run instructions
├── app.py                                           # Streamlit interactive analytics web application
├── requirements.txt                                 # List of project dependencies for one-command install
└── run.bat                                          # One-click Windows batch launcher for setup and execution
```

### File Details:

| File Name | Description |
|---|---|
| **`app.py`** | Main application script hosting the interactive Streamlit dashboard, custom KPI cards, and Plotly charts. |
| **`Ball_by_Ball.csv`** | Raw delivery-by-delivery dataset covering match deliveries, runs, extras, and wickets across IPL matches. |
| **`Harshavardhn_Patil_IPL_IBM_ProjectReport.docx`** | Detailed academic/internship project report with executive summary, methodology, and dashboard visuals. |
| **`IPL_Ball_by_Ball_IBM_Project.ipynb`** | Step-by-step Jupyter Notebook detailing exploratory data analysis, data pre-processing, and aggregations. |
| **`requirements.txt`** | Dependency manifest specifying library packages (`streamlit`, `pandas`, `numpy`, `plotly`). |
| **`run.bat`** | Windows automation script to install dependencies and run the dashboard in one click. |
| **`.gitignore`** | Configures Git to ignore temporary files, virtual environments, and system caches. |
| **`README.md`** | Central guide containing project background, features, setup, and key findings. |

---

## 📊 Dashboard Key Metrics (KPIs)

The dashboard computes and displays the following core metrics across all 577 matches:

| Metric | Total Count | Analytical Significance |
|---|---|---|
| 🏟️ **Matches** | **577** | Total individual match records processed |
| 📊 **Total Runs** | **173,965** | Aggregate runs scored across all matches |
| 🎯 **Wickets** | **5,532** | Total recorded bowler dismissals and outs |
| 4️⃣ **Fours** | **15,413** | Total boundary fours struck |
| 6️⃣ **Sixes** | **5,813** | Total maximum sixes struck |
| ⚫ **Dot Balls** | **49,915** | Non-scoring deliveries bowled |

---

## 📈 Dashboard Features & Analytics

1. **Dynamic Sidebar Filters:** Filter instantly by Batting Team ID and Innings ID. All metrics, charts, and tables update in real time.
2. **Team Performance Overview:** Dual comparison of total runs accumulated versus overall team run rates.
3. **Top Batting Performers:** Identifies the top 15 batsmen (Striker IDs) with total runs, balls faced, strike rates, and boundary counts.
4. **Bowling Performance:** Ranks leading wicket-takers and displays economy rates for bowlers meeting the qualification threshold (60+ deliveries).
5. **Over-by-Over Scoring Trends:** Spline-smoothed run-rate trend line highlighting powerplay, middle, and death overs scoring intensity.
6. **Extras & Dismissal Breakdown:** Donut chart illustrating extras distribution (wides, no-balls, leg byes) and bar breakdown of dismissal modes.
7. **Innings Score Distribution:** Histogram displaying frequency of final team totals per innings.
8. **Filtered Data Table & CSV Export:** Searchable delivery-level data table with a dedicated button to export filtered subsets.

---

## 🛠️ Technology Stack

| Technology | Role |
|---|---|
| **Python** | Core analytical programming language |
| **Streamlit** | Modern web application framework for interactive analytics |
| **Pandas** | Data cleaning, manipulation, transformation, and aggregations |
| **NumPy** | High-performance vectorized numerical operations |
| **Plotly Express & Graph Objects** | Interactive, publication-ready data visualizations |
| **Jupyter Notebook** | Exploratory data analysis, validation, and documentation |

---

## 🚀 Quick Setup & Installation

### Option 1: One-Click Launch (Windows)
Double-click **`run.bat`** in the project folder. It will automatically install requirements and launch the dashboard in your default browser.

---

### Option 2: Manual Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/HarshPatil0804/IPL_Ball_by_Ball_IBM_Project.git
   cd IPL_Ball_by_Ball_IBM_Project
   ```

2. **Install required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Launch the Streamlit Dashboard:**
   ```bash
   streamlit run app.py
   ```

4. **Access the Application:**
   Open your browser and navigate to:
   ```text
   http://localhost:8501
   ```

---

## ▶️ Running the Jupyter Notebook

To explore the raw data analysis and code development step-by-step:

```bash
jupyter notebook IPL_Ball_by_Ball_IBM_Project.ipynb
```

---

## 🔎 Data Processing Logic

- **Total Runs:** `Total_Runs = Batsman_Scored + Extra_Runs`
- **Dot Ball Definition:** `Batsman_Scored == 0` and `Extra_Runs == 0`
- **Boundary Detection:** `Is_Four = Batsman_Scored == 4` and `Is_Six = Batsman_Scored == 6`
- **Wickets:** Filtered where `Dissimal_Type != 'None'`
- **Run Rate Calculation:** $\text{Run Rate} = \frac{\text{Runs}}{\text{Balls}} \times 6$
- **Batting Strike Rate:** $\text{Strike Rate} = \frac{\text{Runs}}{\text{Balls Faced}} \times 100$

---

## 👨‍💻 Author

**Harshavardhan Patil**  
- **Project Title:** IPL Ball-by-Ball Data Analysis & Interactive Dashboard  
- **Context:** IBM Internship Data Analytics Project  
- **Repository:** [HarshPatil0804/IPL_Ball_by_Ball_IBM_Project](https://github.com/HarshPatil0804/IPL_Ball_by_Ball_IBM_Project)
