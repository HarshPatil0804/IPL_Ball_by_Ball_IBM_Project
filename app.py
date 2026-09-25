
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio

# ==================== PAGE CONFIG ====================
st.set_page_config(
    page_title="IPL Ball-by-Ball Analytics",
    page_icon="🏏",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==================== PROFESSIONAL COLOR PALETTE ====================
COLORS = {
    "bg_dark":       "#0E1117",
    "bg_card":       "#1A1F2E",
    "bg_sidebar":    "#141926",
    "accent_blue":   "#3B82F6",
    "accent_teal":   "#14B8A6",
    "accent_indigo": "#6366F1",
    "accent_amber":  "#F59E0B",
    "accent_rose":   "#F43F5E",
    "accent_emerald":"#10B981",
    "text_primary":  "#F1F5F9",
    "text_secondary":"#94A3B8",
    "text_muted":    "#64748B",
    "border":        "#1E293B",
    "surface":       "#1E293B",
}

# Chart color sequence — professional, muted, distinguishable
CHART_COLORS = [
    "#3B82F6",  # Blue
    "#14B8A6",  # Teal
    "#6366F1",  # Indigo
    "#F59E0B",  # Amber
    "#F43F5E",  # Rose
    "#10B981",  # Emerald
    "#8B5CF6",  # Violet
    "#EC4899",  # Pink
    "#06B6D4",  # Cyan
    "#EF4444",  # Red
    "#84CC16",  # Lime
    "#F97316",  # Orange
]

# ==================== CUSTOM PLOTLY TEMPLATE ====================
custom_template = go.layout.Template(
    layout=go.Layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(family="Inter, -apple-system, sans-serif", color="#CBD5E1", size=13),
        title=dict(font=dict(size=18, color="#F1F5F9"), x=0, xanchor="left"),
        xaxis=dict(
            gridcolor="rgba(51,65,85,0.4)",
            linecolor="rgba(51,65,85,0.6)",
            tickfont=dict(color="#94A3B8"),
            title_font=dict(color="#94A3B8"),
        ),
        yaxis=dict(
            gridcolor="rgba(51,65,85,0.4)",
            linecolor="rgba(51,65,85,0.6)",
            tickfont=dict(color="#94A3B8"),
            title_font=dict(color="#94A3B8"),
        ),
        colorway=CHART_COLORS,
        margin=dict(l=40, r=20, t=50, b=40),
        hoverlabel=dict(
            bgcolor="#1E293B",
            bordercolor="#334155",
            font_color="#F1F5F9",
            font_size=13,
        ),
        bargap=0.25,
    )
)
pio.templates["professional_dark"] = custom_template
pio.templates.default = "professional_dark"

# ==================== CUSTOM CSS ====================
st.markdown("""
<style>
    /* ---- Import Google Font ---- */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

    /* ---- Root & Global ---- */
    html, body, [class*="st-"] {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }

    .stApp {
        background: linear-gradient(180deg, #0B0F19 0%, #0E1117 50%, #111827 100%);
    }

    /* ---- Header Banner ---- */
    .dashboard-header {
        background: linear-gradient(135deg, #1E293B 0%, #0F172A 50%, #1E293B 100%);
        border: 1px solid rgba(59,130,246,0.15);
        border-radius: 16px;
        padding: 2rem 2.5rem;
        margin-bottom: 1.5rem;
        position: relative;
        overflow: hidden;
    }
    .dashboard-header::before {
        content: '';
        position: absolute;
        top: 0; left: 0; right: 0;
        height: 3px;
        background: linear-gradient(90deg, #3B82F6, #14B8A6, #6366F1);
    }
    .dashboard-header h1 {
        color: #F1F5F9;
        font-size: 2rem;
        font-weight: 800;
        margin: 0 0 0.3rem 0;
        letter-spacing: -0.02em;
    }
    .dashboard-header p {
        color: #94A3B8;
        font-size: 0.95rem;
        margin: 0;
    }

    /* ---- Metric Cards ---- */
    .metric-card {
        background: linear-gradient(145deg, #1A1F2E, #151A28);
        border: 1px solid #1E293B;
        border-radius: 14px;
        padding: 1.4rem 1.5rem;
        text-align: center;
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }
    .metric-card:hover {
        border-color: rgba(59,130,246,0.3);
        transform: translateY(-2px);
        box-shadow: 0 8px 24px rgba(0,0,0,0.3);
    }
    .metric-card .metric-icon {
        font-size: 1.6rem;
        margin-bottom: 0.5rem;
        display: block;
    }
    .metric-card .metric-value {
        font-size: 1.9rem;
        font-weight: 800;
        letter-spacing: -0.03em;
        margin: 0;
        line-height: 1.2;
    }
    .metric-card .metric-label {
        color: #64748B;
        font-size: 0.78rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        margin-top: 0.4rem;
    }
    .metric-card.blue   .metric-value { color: #60A5FA; }
    .metric-card.teal   .metric-value { color: #2DD4BF; }
    .metric-card.indigo .metric-value { color: #818CF8; }
    .metric-card.amber  .metric-value { color: #FBBF24; }
    .metric-card.rose   .metric-value { color: #FB7185; }
    .metric-card.emerald .metric-value { color: #34D399; }

    .metric-card.blue::after,
    .metric-card.teal::after,
    .metric-card.indigo::after,
    .metric-card.amber::after,
    .metric-card.rose::after,
    .metric-card.emerald::after {
        content: '';
        position: absolute;
        bottom: 0; left: 10%; right: 10%;
        height: 2px;
        border-radius: 2px;
    }
    .metric-card.blue::after   { background: linear-gradient(90deg, transparent, #3B82F6, transparent); }
    .metric-card.teal::after   { background: linear-gradient(90deg, transparent, #14B8A6, transparent); }
    .metric-card.indigo::after { background: linear-gradient(90deg, transparent, #6366F1, transparent); }
    .metric-card.amber::after  { background: linear-gradient(90deg, transparent, #F59E0B, transparent); }
    .metric-card.rose::after   { background: linear-gradient(90deg, transparent, #F43F5E, transparent); }
    .metric-card.emerald::after{ background: linear-gradient(90deg, transparent, #10B981, transparent); }

    /* ---- Section Titles ---- */
    .section-title {
        color: #F1F5F9;
        font-size: 1.25rem;
        font-weight: 700;
        margin: 2rem 0 1rem 0;
        padding-bottom: 0.6rem;
        border-bottom: 2px solid #1E293B;
        display: flex;
        align-items: center;
        gap: 0.6rem;
    }

    /* ---- Chart Containers ---- */
    .chart-container {
        background: linear-gradient(145deg, #1A1F2E, #151A28);
        border: 1px solid #1E293B;
        border-radius: 14px;
        padding: 1.2rem 1rem 0.5rem 1rem;
        margin-bottom: 1rem;
        transition: border-color 0.3s ease;
    }
    .chart-container:hover {
        border-color: rgba(59,130,246,0.2);
    }

    /* ---- Sidebar ---- */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0F172A, #0B0F19) !important;
        border-right: 1px solid #1E293B !important;
    }

    /* Sidebar heading (Dashboard Filters) */
    section[data-testid="stSidebar"] .stMarkdown h2,
    section[data-testid="stSidebar"] .stMarkdown h3 {
        color: #E2E8F0 !important;
        font-size: 1.15rem;
        font-weight: 700;
    }

    /* Sidebar widget labels (Batting Team ID, Innings ID) */
    section[data-testid="stSidebar"] .stMultiSelect label,
    section[data-testid="stSidebar"] .stSelectbox label,
    section[data-testid="stSidebar"] label {
        color: #CBD5E1 !important;
        font-weight: 600 !important;
        font-size: 0.9rem !important;
    }

    /* Multiselect pill / tag chips */
    section[data-testid="stSidebar"] span[data-baseweb="tag"] {
        background: rgba(59,130,246,0.2) !important;
        border: 1px solid rgba(59,130,246,0.35) !important;
        color: #93C5FD !important;
        border-radius: 6px !important;
    }
    section[data-testid="stSidebar"] span[data-baseweb="tag"] span {
        color: #93C5FD !important;
    }
    /* Tag close (x) button */
    section[data-testid="stSidebar"] span[data-baseweb="tag"] svg {
        fill: #93C5FD !important;
    }

    /* Multiselect input area */
    section[data-testid="stSidebar"] [data-baseweb="select"] {
        background-color: #1E293B !important;
        border-color: #334155 !important;
        border-radius: 8px !important;
    }
    section[data-testid="stSidebar"] [data-baseweb="select"]:hover {
        border-color: #3B82F6 !important;
    }

    /* Sidebar divider */
    section[data-testid="stSidebar"] hr {
        border-color: #1E293B !important;
    }

    /* ---- DataFrames ---- */
    .stDataFrame {
        border: 1px solid #1E293B;
        border-radius: 12px;
        overflow: hidden;
    }

    /* ---- Download Button ---- */
    .stDownloadButton > button {
        background: linear-gradient(135deg, #3B82F6, #2563EB) !important;
        color: white !important;
        border: none !important;
        border-radius: 10px !important;
        padding: 0.6rem 2rem !important;
        font-weight: 600 !important;
        letter-spacing: 0.02em;
        transition: all 0.3s ease !important;
    }
    .stDownloadButton > button:hover {
        background: linear-gradient(135deg, #2563EB, #1D4ED8) !important;
        box-shadow: 0 4px 16px rgba(59,130,246,0.35) !important;
        transform: translateY(-1px) !important;
    }

    /* ---- Divider ---- */
    hr {
        border-color: #1E293B !important;
        margin: 1.5rem 0 !important;
    }

    /* ---- Hide default streamlit metric ---- */
    [data-testid="stMetric"] { display: none; }

    /* ---- Footer ---- */
    .footer-text {
        text-align: center;
        color: #475569;
        font-size: 0.8rem;
        padding: 2rem 0 1rem 0;
        border-top: 1px solid #1E293B;
        margin-top: 2rem;
    }
</style>
""", unsafe_allow_html=True)

# ==================== DATA LOADING ====================
@st.cache_data
def load_data():
    path = "Ball_by_Ball.csv"
    data = pd.read_csv(path)

    data.columns = data.columns.str.strip()

    for col in data.select_dtypes(include="object").columns:
        data[col] = data[col].astype(str).str.strip()

    numeric_cols = [
        "Match_Id", "Innings_Id", "Over_Id", "Ball_Id",
        "Team_Batting_Id", "Team_Bowling_Id", "Striker_Id",
        "Striker_Batting_Position", "Non_Striker_Id", "Bowler_Id",
        "Batsman_Scored", "Extra_Runs", "Player_dissimal_Id", "Fielder_Id"
    ]

    for col in numeric_cols:
        data[col] = pd.to_numeric(data[col], errors="coerce")

    data["Batsman_Scored"] = data["Batsman_Scored"].fillna(0)
    data["Extra_Runs"] = data["Extra_Runs"].fillna(0)

    for col in ["Extra_Type", "Dissimal_Type"]:
        data[col] = data[col].replace(
            {"": "None", "nan": "None", " ": "None"}
        ).fillna("None")

    data["Total_Runs"] = data["Batsman_Scored"] + data["Extra_Runs"]
    data["Is_Dot_Ball"] = (
        (data["Batsman_Scored"] == 0) &
        (data["Extra_Runs"] == 0)
    )
    data["Is_Four"] = data["Batsman_Scored"] == 4
    data["Is_Six"] = data["Batsman_Scored"] == 6
    data["Is_Wicket"] = data["Dissimal_Type"].ne("None")

    data["Ball_Key"] = (
        data["Match_Id"].astype("Int64").astype(str) + "_" +
        data["Innings_Id"].astype("Int64").astype(str) + "_" +
        data["Over_Id"].astype("Int64").astype(str) + "_" +
        data["Ball_Id"].astype("Int64").astype(str)
    )

    return data

df = load_data()

# ==================== HEADER ====================
st.markdown("""
<div class="dashboard-header">
    <h1>🏏 IPL Ball-by-Ball Analytics</h1>
    <p>IBM Internship Data Analytics Project &nbsp;·&nbsp; Python &nbsp;·&nbsp; Pandas &nbsp;·&nbsp; Plotly &nbsp;·&nbsp; Streamlit</p>
</div>
""", unsafe_allow_html=True)

# ==================== SIDEBAR FILTERS ====================
st.sidebar.markdown("### 🎛️ Dashboard Filters")
st.sidebar.markdown("---")

team_options = sorted(df["Team_Batting_Id"].dropna().unique().tolist())
team_filter = st.sidebar.multiselect(
    "🏟️ Batting Team ID",
    options=team_options,
    default=team_options
)

innings_options = sorted(df["Innings_Id"].dropna().unique().tolist())
innings_filter = st.sidebar.multiselect(
    "🏏 Innings ID",
    options=innings_options,
    default=innings_options
)

st.sidebar.markdown("---")
st.sidebar.markdown(
    "<p style='color:#475569; font-size:0.75rem; text-align:center;'>"
    "Use filters to drill down into specific teams and innings</p>",
    unsafe_allow_html=True
)

filtered = df[
    df["Team_Batting_Id"].isin(team_filter) &
    df["Innings_Id"].isin(innings_filter)
].copy()

# ==================== KPI METRICS ====================
total_runs  = int(filtered["Total_Runs"].sum())
matches     = int(filtered["Match_Id"].nunique())
wickets     = int(filtered["Is_Wicket"].sum())
fours       = int(filtered["Is_Four"].sum())
sixes       = int(filtered["Is_Six"].sum())
dot_balls   = int(filtered["Is_Dot_Ball"].sum())

metrics = [
    ("🏟️", "Matches",    f"{matches:,}",    "blue"),
    ("📊", "Total Runs",  f"{total_runs:,}",  "teal"),
    ("🎯", "Wickets",     f"{wickets:,}",     "rose"),
    ("4️⃣",  "Fours",      f"{fours:,}",       "amber"),
    ("6️⃣",  "Sixes",      f"{sixes:,}",       "indigo"),
    ("⚫", "Dot Balls",   f"{dot_balls:,}",   "emerald"),
]

cols = st.columns(6, gap="medium")
for col, (icon, label, value, style) in zip(cols, metrics):
    col.markdown(f"""
    <div class="metric-card {style}">
        <span class="metric-icon">{icon}</span>
        <p class="metric-value">{value}</p>
        <p class="metric-label">{label}</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

if filtered.empty:
    st.warning("No data matches the selected filters.")
    st.stop()

# ==================== TEAM ANALYSIS ====================
st.markdown('<div class="section-title">📊 Team Performance Overview</div>', unsafe_allow_html=True)

team_stats = (
    filtered.groupby("Team_Batting_Id")
    .agg(
        Runs=("Total_Runs", "sum"),
        Balls=("Ball_Key", "nunique"),
        Fours=("Is_Four", "sum"),
        Sixes=("Is_Six", "sum")
    )
    .reset_index()
)

team_stats["Run_Rate"] = np.where(
    team_stats["Balls"] > 0,
    team_stats["Runs"] / team_stats["Balls"] * 6,
    0
)

left, right = st.columns(2)

with left:
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    fig = px.bar(
        team_stats.sort_values("Runs", ascending=False),
        x="Team_Batting_Id",
        y="Runs",
        text="Runs",
        title="Total Runs by Team",
        color="Runs",
        color_continuous_scale=["#1E3A5F", "#3B82F6", "#93C5FD"],
    )
    fig.update_traces(
        textposition="outside",
        textfont=dict(color="#CBD5E1", size=11),
        marker_line=dict(width=0),
    )
    fig.update_layout(coloraxis_showscale=False, showlegend=False)
    st.plotly_chart(fig, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

with right:
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    fig = px.bar(
        team_stats.sort_values("Run_Rate", ascending=False),
        x="Team_Batting_Id",
        y="Run_Rate",
        text="Run_Rate",
        title="Run Rate by Team",
        color="Run_Rate",
        color_continuous_scale=["#134E4A", "#14B8A6", "#5EEAD4"],
    )
    fig.update_traces(
        texttemplate="%{text:.2f}",
        textposition="outside",
        textfont=dict(color="#CBD5E1", size=11),
        marker_line=dict(width=0),
    )
    fig.update_layout(coloraxis_showscale=False, showlegend=False)
    st.plotly_chart(fig, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ==================== BATTING PERFORMANCE ====================
st.markdown('<div class="section-title">🏏 Top Batting Performers</div>', unsafe_allow_html=True)

player_stats = (
    filtered.groupby("Striker_Id")
    .agg(
        Runs=("Batsman_Scored", "sum"),
        Balls=("Ball_Key", "nunique"),
        Fours=("Is_Four", "sum"),
        Sixes=("Is_Six", "sum")
    )
    .reset_index()
)

player_stats["Strike_Rate"] = np.where(
    player_stats["Balls"] > 0,
    player_stats["Runs"] / player_stats["Balls"] * 100,
    0
)

top_players = player_stats.sort_values(
    ["Runs", "Strike_Rate"], ascending=False
).head(15)

st.markdown('<div class="chart-container">', unsafe_allow_html=True)
fig = px.bar(
    top_players,
    x="Striker_Id",
    y="Runs",
    text="Runs",
    hover_data=["Balls", "Fours", "Sixes", "Strike_Rate"],
    title="Top 15 Batters by Runs Scored",
    color="Runs",
    color_continuous_scale=["#312E81", "#6366F1", "#A5B4FC"],
)
fig.update_traces(
    textposition="outside",
    textfont=dict(color="#CBD5E1", size=11),
    marker_line=dict(width=0),
)
fig.update_layout(coloraxis_showscale=False)
st.plotly_chart(fig, use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)

# ==================== BOWLING PERFORMANCE ====================
st.markdown('<div class="section-title">🎯 Bowling Performance</div>', unsafe_allow_html=True)

bowler_stats = (
    filtered.groupby("Bowler_Id")
    .agg(
        Balls=("Ball_Key", "nunique"),
        Runs_Conceded=("Total_Runs", "sum"),
        Wickets=("Is_Wicket", "sum"),
        Dot_Balls=("Is_Dot_Ball", "sum")
    )
    .reset_index()
)

bowler_stats["Economy"] = np.where(
    bowler_stats["Balls"] > 0,
    bowler_stats["Runs_Conceded"] / bowler_stats["Balls"] * 6,
    0
)

bowler_stats["Dot_Ball_Percentage"] = np.where(
    bowler_stats["Balls"] > 0,
    bowler_stats["Dot_Balls"] / bowler_stats["Balls"] * 100,
    0
)

qualified = bowler_stats[bowler_stats["Balls"] >= 60].copy()

if not qualified.empty:
    left, right = st.columns(2)

    with left:
        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
        top_wickets = qualified.sort_values("Wickets", ascending=False).head(15)
        fig = px.bar(
            top_wickets,
            x="Bowler_Id",
            y="Wickets",
            text="Wickets",
            title="Top Bowlers by Wickets",
            color="Wickets",
            color_continuous_scale=["#4C1D95", "#8B5CF6", "#C4B5FD"],
        )
        fig.update_traces(
            textposition="outside",
            textfont=dict(color="#CBD5E1", size=11),
            marker_line=dict(width=0),
        )
        fig.update_layout(coloraxis_showscale=False)
        st.plotly_chart(fig, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with right:
        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
        economy_chart = qualified.sort_values("Economy").head(15)
        fig = px.bar(
            economy_chart,
            x="Bowler_Id",
            y="Economy",
            text="Economy",
            title="Best Economy (60+ Balls Bowled)",
            color="Economy",
            color_continuous_scale=["#34D399", "#10B981", "#064E3B"],
        )
        fig.update_traces(
            texttemplate="%{text:.2f}",
            textposition="outside",
            textfont=dict(color="#CBD5E1", size=11),
            marker_line=dict(width=0),
        )
        fig.update_layout(coloraxis_showscale=False)
        st.plotly_chart(fig, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

# ==================== OVER-BY-OVER ANALYSIS ====================
st.markdown('<div class="section-title">📈 Scoring Trends by Over</div>', unsafe_allow_html=True)

over_stats = (
    filtered.groupby("Over_Id")
    .agg(
        Runs=("Total_Runs", "sum"),
        Balls=("Ball_Key", "nunique"),
        Wickets=("Is_Wicket", "sum")
    )
    .reset_index()
)

over_stats["Run_Rate"] = np.where(
    over_stats["Balls"] > 0,
    over_stats["Runs"] / over_stats["Balls"] * 6,
    0
)

st.markdown('<div class="chart-container">', unsafe_allow_html=True)
fig = go.Figure()

fig.add_trace(go.Scatter(
    x=over_stats.sort_values("Over_Id")["Over_Id"],
    y=over_stats.sort_values("Over_Id")["Run_Rate"],
    mode="lines+markers",
    name="Run Rate",
    line=dict(color="#3B82F6", width=3, shape="spline"),
    marker=dict(size=8, color="#3B82F6", line=dict(width=2, color="#1E293B")),
    fill="tozeroy",
    fillcolor="rgba(59,130,246,0.08)",
    hovertemplate="Over %{x}<br>Run Rate: %{y:.2f}<extra></extra>"
))

fig.update_layout(
    title="Run Rate Progression Across Overs",
    xaxis_title="Over Number",
    yaxis_title="Run Rate",
    hovermode="x unified",
)
st.plotly_chart(fig, use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)

# ==================== EXTRAS & DISMISSALS ====================
st.markdown('<div class="section-title">📋 Extras & Dismissals Breakdown</div>', unsafe_allow_html=True)

left, right = st.columns(2)

with left:
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    extras = (
        filtered[filtered["Extra_Type"] != "None"]
        .groupby("Extra_Type")["Extra_Runs"]
        .sum()
        .reset_index()
        .sort_values("Extra_Runs", ascending=False)
    )

    fig = px.pie(
        extras,
        names="Extra_Type",
        values="Extra_Runs",
        title="Extra Runs Distribution",
        color_discrete_sequence=CHART_COLORS,
        hole=0.45,
    )
    fig.update_traces(
        textposition="inside",
        textinfo="percent+label",
        textfont=dict(size=12, color="white"),
        marker=dict(line=dict(color="#0E1117", width=2)),
        pull=[0.03] * len(extras),
    )
    fig.update_layout(
        legend=dict(
            font=dict(color="#94A3B8", size=12),
            bgcolor="rgba(0,0,0,0)",
        )
    )
    st.plotly_chart(fig, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

with right:
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    dismissals = (
        filtered[filtered["Dissimal_Type"] != "None"]
        .groupby("Dissimal_Type")
        .size()
        .reset_index(name="Wickets")
        .sort_values("Wickets", ascending=False)
    )

    fig = px.bar(
        dismissals,
        x="Dissimal_Type",
        y="Wickets",
        text="Wickets",
        title="Dismissal Types",
        color="Dissimal_Type",
        color_discrete_sequence=CHART_COLORS,
    )
    fig.update_traces(
        textposition="outside",
        textfont=dict(color="#CBD5E1", size=11),
        marker_line=dict(width=0),
    )
    fig.update_layout(showlegend=False)
    st.plotly_chart(fig, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ==================== SCORE DISTRIBUTION ====================
st.markdown('<div class="section-title">📊 Innings Score Distribution</div>', unsafe_allow_html=True)

innings_scores = (
    filtered.groupby(["Match_Id", "Innings_Id", "Team_Batting_Id"])
    .agg(Runs=("Total_Runs", "sum"))
    .reset_index()
)

st.markdown('<div class="chart-container">', unsafe_allow_html=True)
fig = px.histogram(
    innings_scores,
    x="Runs",
    nbins=30,
    title="Distribution of Innings Totals",
    color_discrete_sequence=["#3B82F6"],
)
fig.update_traces(
    marker_line=dict(color="#1E293B", width=1),
    opacity=0.85,
)
fig.update_layout(
    xaxis_title="Innings Total",
    yaxis_title="Frequency",
    bargap=0.05,
)
st.plotly_chart(fig, use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)

# ==================== DATA TABLE ====================
st.markdown('<div class="section-title">🔎 Filtered Ball-by-Ball Data</div>', unsafe_allow_html=True)

display_cols = [
    "Match_Id", "Innings_Id", "Over_Id", "Ball_Id",
    "Team_Batting_Id", "Team_Bowling_Id", "Striker_Id",
    "Bowler_Id", "Batsman_Scored", "Extra_Type",
    "Extra_Runs", "Total_Runs", "Dissimal_Type"
]

st.dataframe(
    filtered[display_cols].sort_values(
        ["Match_Id", "Innings_Id", "Over_Id", "Ball_Id"]
    ),
    use_container_width=True,
    height=420,
)

# ==================== DOWNLOAD ====================
st.markdown("<br>", unsafe_allow_html=True)

csv = filtered.to_csv(index=False).encode("utf-8")

st.download_button(
    label="⬇️  Download Filtered Data as CSV",
    data=csv,
    file_name="filtered_ball_by_ball.csv",
    mime="text/csv"
)

# ==================== FOOTER ====================
st.markdown("""
<div class="footer-text">
    Built for IBM Internship Data Analytics Project &nbsp;·&nbsp;
    Player/team names are not inferred — dataset contains IDs only &nbsp;·&nbsp;
    Powered by Streamlit + Plotly
</div>
""", unsafe_allow_html=True)
