import streamlit as st
import pandas as pd
import os


# Sidebar Navigation
page = st.sidebar.selectbox(
    "Navigation",
    [
        "Overview",
        "Teams Analysis",
        "Players Analysis",
        "Venue Analysis",
        "Endorsement Recommendations",
        "IPL Storyboard",
        "Conclusion"
    ]
)

# Load data
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

matches = pd.read_csv(
    os.path.join(BASE_DIR, "data", "matches.csv")
)

deliveries = pd.read_csv(
    os.path.join(BASE_DIR, "data", "deliveries.csv")
)
if page == "Overview":

    st.title("🏏 IPL Data Analysis Dashboard")

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Matches", len(matches))

    col2.metric(
        "Total Teams",
        len(set(matches['team1']).union(set(matches['team2'])))
    )

    col3.metric(
        "Venues",
        matches['venue'].nunique()
    )

    st.header("Dataset Preview")

    st.subheader("Matches Dataset")
    st.dataframe(matches.head())

    st.subheader("Deliveries Dataset")
    st.dataframe(deliveries.head())

elif page == "Teams Analysis":

    st.header("🏆 Most Successful IPL Teams")

    team_wins = matches['winner'].value_counts()

    st.bar_chart(team_wins)

    st.info(
        "Mumbai Indians are the most successful IPL franchise."
    )
elif page == "Players Analysis":

    st.header("⭐ Top Player of the Match Winners")

    top_players = (
        matches['player_of_match']
        .value_counts()
        .head(10)
    )

    st.bar_chart(top_players)

    st.header("🏏 Top Run Scorers")

    top_batsmen = (
        deliveries.groupby('batter')['batsman_runs']
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    st.bar_chart(top_batsmen)

    st.header("🎯 Top Wicket Takers")

    top_bowlers = (
        deliveries[
            deliveries['player_dismissed'].notna()
        ]['bowler']
        .value_counts()
        .head(10)
    )

    st.bar_chart(top_bowlers)
elif page == "Venue Analysis":

    st.header("🏟 Top IPL Venues")

    venues = matches['venue'].value_counts().head(10)

    st.bar_chart(venues)

    st.info(
        "These venues hosted the highest number of IPL matches."
    )
elif page == "Endorsement Recommendations":

    st.title("🏆 Endorsement Recommendations")

    top_players = (
        matches['player_of_match']
        .value_counts()
        .head(5)
    )

    st.write(
        "Based on Player of the Match awards, the following players are recommended for endorsements:"
    )

    for player in top_players.index:

        st.success(
            f"{player} is recommended for brand endorsements."
        )
elif page == "IPL Storyboard":

    st.title("📖 IPL Storyboard")

    st.subheader("Chapter 1: The Kings of IPL")

    st.info("""
    Mumbai Indians emerged as the most successful IPL franchise
    with the highest number of wins.
    """)

    team_wins = matches['winner'].value_counts().head(10)

    st.bar_chart(team_wins)

    st.subheader("Chapter 2: Match Winners")

    top_players = (
        matches['player_of_match']
        .value_counts()
        .head(10)
    )

    st.bar_chart(top_players)

    st.info("""
    These players consistently delivered match-winning performances.
    """)

    st.subheader("Chapter 3: IPL Venues")

    venues = matches['venue'].value_counts().head(10)

    st.bar_chart(venues)

    st.info("""
    Certain venues hosted significantly more matches and became
    important IPL battlegrounds.
    """)
elif page == "Conclusion":

    st.title("📌 Project Conclusion")

    st.markdown("""
### Key Findings

- Mumbai Indians are the most successful IPL team.
- Top players consistently influence match outcomes.
- Venue plays an important role in match dynamics.
- Player performance can be used for endorsement recommendations.

### Business Impact

- Helps brands identify potential ambassadors.
- Supports sports analytics decision making.
- Provides insights into IPL performance trends.
""")