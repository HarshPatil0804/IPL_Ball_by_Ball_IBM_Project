# 🏏 IPL Ball-by-Ball Data Analysis & Interactive Dashboard

## IBM Internship Data Analytics Project

A complete Python-based data analytics project that analyzes IPL
ball-by-ball cricket data and presents the results through an
interactive Streamlit dashboard.

The project covers data cleaning, feature engineering, exploratory data
analysis, KPI development, team analysis, batting analysis, bowling
analysis, scoring trends, extras, dismissals, innings-score
distribution, and filtered ball-by-ball exploration.

------------------------------------------------------------------------

## 📌 Project Overview

The objective of this project is to convert raw IPL delivery-level data
into meaningful analytical insights using Python.

The project follows an end-to-end analytics workflow:

**Raw Dataset → Data Cleaning → Feature Engineering → EDA → Aggregation
→ Visualization → Interactive Dashboard**

The final solution contains:

-   A Jupyter Notebook with the complete analysis
-   A Streamlit dashboard
-   A professional project report
-   The original ball-by-ball dataset

> **Dataset note:** The supplied dataset contains numeric team and
> player IDs rather than readable team/player names. The project
> therefore uses the available IDs directly instead of introducing
> unverified name mappings.

------------------------------------------------------------------------

## 🎯 Project Objectives

-   Load and understand the IPL ball-by-ball dataset.
-   Clean and preprocess the raw data.
-   Handle missing and inconsistent values.
-   Create analytical features such as total runs, dot balls, fours,
    sixes, and wickets.
-   Analyze team batting performance.
-   Analyze individual batting performance using striker IDs.
-   Analyze bowling performance using bowler IDs.
-   Study run-rate progression across overs.
-   Analyze extra runs by extra type.
-   Analyze dismissal types.
-   Study the distribution of innings scores.
-   Build an interactive Streamlit dashboard.
-   Provide a reproducible Python notebook for the complete workflow.

------------------------------------------------------------------------

## 📊 Dashboard KPIs

The dashboard provides the following high-level KPIs:

  KPI              Value
  ------------ ---------
  Matches            577
  Total Runs     173,965
  Wickets          5,532
  Fours           15,413
  Sixes            5,813
  Dot Balls       49,915

These values are displayed directly in the project dashboard.

------------------------------------------------------------------------

## 📈 Dashboard Features

### 1. Team Performance Overview

Provides:

-   Total runs by batting team ID
-   Run rate by batting team ID
-   Team-level comparison

### 2. Top Batting Performers

Displays:

-   Top 15 striker IDs by runs scored
-   Comparative batting performance

### 3. Bowling Performance

Displays:

-   Top bowlers by recorded wickets
-   Economy comparison
-   Qualification threshold of at least 60 recorded balls for the
    economy comparison

### 4. Scoring Trends by Over

Shows:

-   Run-rate progression across over numbers
-   Changes in scoring intensity throughout an innings

### 5. Extras & Dismissals

Analyzes:

-   Wides
-   Leg byes
-   Byes
-   No-balls
-   Penalties
-   Caught
-   Bowled
-   Run out
-   LBW
-   Stumped
-   Caught and bowled
-   Retired hurt
-   Hit wicket
-   Obstructing the field

### 6. Innings Score Distribution

Shows the distribution of innings totals using a histogram.

### 7. Filtered Ball-by-Ball Data

Provides detailed delivery-level information including:

-   Match ID
-   Innings ID
-   Over ID
-   Ball ID
-   Batting team ID
-   Bowling team ID
-   Striker ID
-   Bowler ID
-   Batsman runs
-   Extra type
-   Extra runs
-   Total runs
-   Dismissal type

------------------------------------------------------------------------

## 🛠️ Technology Stack

  Technology         Purpose
  ------------------ ----------------------------------------
  Python             Core programming and analysis
  Pandas             Data loading, cleaning and aggregation
  NumPy              Numerical calculations
  Matplotlib         Static visualization
  Plotly             Interactive charts
  Streamlit          Interactive dashboard
  Jupyter Notebook   Analysis documentation

------------------------------------------------------------------------

## 📂 Project Structure

``` text
IPL_Ball_by_Ball_IBM_Project/
│
├── Ball_by_Ball.csv
│
├── IPL_Ball_by_Ball_IBM_Project.ipynb
│
├── app.py
│
├── IPL_IBM_Project_Report_Exact_Dashboard_Screenshots.docx
│
└── README.md
```

### File Description

**`Ball_by_Ball.csv`**

Original IPL ball-by-ball dataset used for the project.

**`IPL_Ball_by_Ball_IBM_Project.ipynb`**

Complete Python notebook containing:

-   Data loading
-   Data cleaning
-   Feature engineering
-   Exploratory analysis
-   KPI calculations
-   Team analysis
-   Player analysis
-   Bowling analysis
-   Visualization
-   Dashboard generation code

**`app.py`**

Streamlit application containing the interactive dashboard.

**`IPL_IBM_Project_Report_Exact_Dashboard_Screenshots.docx`**

Professional project report containing project documentation and the
exact dashboard screenshots.

**`README.md`**

Project documentation and setup instructions.

------------------------------------------------------------------------

## 🚀 Installation

### Step 1 --- Clone or download the project

Place all project files in the same folder.

### Step 2 --- Install Python

Python 3.9 or later is recommended.

### Step 3 --- Install required libraries

Open a terminal in the project folder and run:

``` bash
pip install pandas numpy matplotlib plotly streamlit jupyter
```

------------------------------------------------------------------------

## ▶️ Run the Jupyter Notebook

Start Jupyter Notebook:

``` bash
jupyter notebook
```

Open:

``` text
IPL_Ball_by_Ball_IBM_Project.ipynb
```

Run the cells sequentially.

------------------------------------------------------------------------

## 🌐 Run the Streamlit Dashboard

Make sure `Ball_by_Ball.csv` and `app.py` are in the same folder.

Run:

``` bash
streamlit run app.py
```

Streamlit will provide a local URL similar to:

``` text
http://localhost:8501
```

Open that URL in your browser.

------------------------------------------------------------------------

## 🔎 Data Processing

The project creates several analytical features from the raw columns.

### Total Runs

``` text
Total_Runs = Batsman_Scored + Extra_Runs
```

### Dot Ball

A delivery is treated as a dot ball when:

``` text
Batsman_Scored = 0
AND
Extra_Runs = 0
```

### Four

``` text
Batsman_Scored = 4
```

### Six

``` text
Batsman_Scored = 6
```

### Wicket

A delivery is treated as a recorded wicket when the dismissal type is
not empty/`None`.

### Run Rate

The dashboard calculates run rate approximately as:

``` text
Run Rate = Runs / Balls × 6
```

------------------------------------------------------------------------

## 📊 Key Findings

Based on the dashboard:

-   The dataset contains **577 matches**.
-   The dashboard reports **173,965 total runs**.
-   **5,532 wickets** are recorded.
-   The dataset contains **15,413 fours**.
-   The dataset contains **5,813 sixes**.
-   The dashboard reports **49,915 dot balls**.
-   Team performance varies considerably across team IDs.
-   The batting dashboard highlights major differences in aggregate runs
    among striker IDs.
-   Bowling performance is presented through both wicket totals and
    economy.
-   The scoring trend generally increases toward the later overs in the
    displayed aggregate analysis.
-   Wides and leg byes represent major portions of the displayed extras
    distribution.
-   Caught dismissals form the largest displayed dismissal category.

------------------------------------------------------------------------

## 💡 Future Improvements

The project can be extended with:

-   Verified player-name mapping
-   Verified team-name mapping
-   Season-wise analysis
-   Venue analysis
-   Toss analysis
-   Match-result analysis
-   Player ranking systems
-   Powerplay / middle-over / death-over analysis
-   Player clustering
-   Predictive analytics
-   Match outcome prediction
-   Win-probability modeling
-   Advanced Power BI integration
-   Deployment to Streamlit Cloud or another hosting platform

------------------------------------------------------------------------

## ⚠️ Limitations

1.  The dataset contains numeric player/team IDs rather than names.
2.  The analysis does not infer names from external sources.
3.  The available columns limit some advanced cricket analytics.
4.  Match-result and season-level analysis requires the corresponding
    fields or verified supplementary datasets.
5.  The dashboard is primarily descriptive and does not currently
    perform predictive modeling.

------------------------------------------------------------------------

## 📄 Project Report

The detailed project report contains:

-   Executive summary
-   Project objectives
-   Dataset description
-   Methodology
-   KPI summary
-   Analytical findings
-   Dashboard features
-   Technical stack
-   Limitations
-   Future scope
-   Conclusion
-   Exact screenshots of the completed dashboard

------------------------------------------------------------------------

## 👨‍💻 Project

**Project Title:** IPL Ball-by-Ball Data Analysis and Interactive
Dashboard

**Project Type:** Data Analytics / Python / Dashboard

**Purpose:** IBM Internship Project Submission

------------------------------------------------------------------------

## ⭐ Conclusion

This project demonstrates an end-to-end data analytics workflow using
Python and IPL ball-by-ball data. It combines data preprocessing,
feature engineering, exploratory data analysis, aggregation,
visualization, and interactive dashboard development.

The final solution provides a practical analytical interface for
exploring team, batting, bowling, scoring, extras, dismissal, and
innings-level patterns from the underlying dataset.
