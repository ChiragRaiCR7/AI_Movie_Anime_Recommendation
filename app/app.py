# app.py
import sys
import os
import streamlit as st
from dotenv import load_dotenv

# Add project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pipeline.pipeline import AnimeRecommendationPipeline, MovieRecommendationPipeline

st.set_page_config(page_title="Anime & Movie Recommender", layout="wide")
load_dotenv()

# ---------------- Cache pipelines ----------------
@st.cache_resource
def init_anime_pipeline():
    return AnimeRecommendationPipeline()

@st.cache_resource
def init_movie_pipeline():
    return MovieRecommendationPipeline()

# ---------------- UI ----------------
st.title("🎬 Anime & Movie Recommender System")

option = st.radio(
    "What would you like recommendations for?",
    ("Anime", "Movies"),
    horizontal=True
)

pipeline = None
query = None

# Load pipeline & input box
if option == "Anime":
    pipeline = init_anime_pipeline()
    st.subheader("Anime Recommender")
    query = st.text_input("Enter your anime preferences (e.g., light-hearted anime with school settings)")
elif option == "Movies":
    pipeline = init_movie_pipeline()
    st.subheader("Movie Recommender")
    query = st.text_input("Enter your movie preferences (e.g., sci-fi movies with AI themes)")

# Generate recommendations
if query:
    try:
        with st.spinner("Fetching recommendations for you..."):
            response = pipeline.recommend(query)

        st.markdown("### Recommendations")
        # Split response by numbered items for nicer formatting
        recommendations = response.split("\n")
        for line in recommendations:
            st.write(line)

    except Exception as e:
        st.error(f"❌ Failed to generate recommendations: {str(e)}")
