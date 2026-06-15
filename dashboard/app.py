import streamlit as st
import pandas as pd
import os


# Page title
st.title("🏏 IPL Data Analysis Dashboard")

# Load data
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

matches = pd.read_csv(
    os.path.join(BASE_DIR, "data", "matches.csv")
)

deliveries = pd.read_csv(
    os.path.join(BASE_DIR, "data", "deliveries.csv")
)
# Dataset preview
st.header("Dataset Preview")

st.subheader("Matches Dataset")
st.dataframe(matches.head())

st.subheader("Deliveries Dataset")
st.dataframe(deliveries.head())
st.header("Top IPL Teams")

team_wins = matches['winner'].value_counts()

st.bar_chart(team_wins)
st.header("Top Player of the Match Winners")

top_players = matches['player_of_match'].value_counts().head(10)

st.bar_chart(top_players)
st.header("Top Run Scorers")

top_batsmen = deliveries.groupby(
    'batter'
)['batsman_runs'].sum().sort_values(
    ascending=False
).head(10)

st.bar_chart(top_batsmen)
st.header("Top Wicket Takers")

top_bowlers = deliveries[
    deliveries['player_dismissed'].notna()
]['bowler'].value_counts().head(10)

st.bar_chart(top_bowlers)
st.header("Top IPL Venues")

venues = matches['venue'].value_counts().head(10)

st.bar_chart(venues)