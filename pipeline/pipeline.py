from src.vector_store import VectorStoreBuilder
from src.recommender import AnimeRecommender, MovieRecommender
from config.config import GROQ_API_KEY, MODEL_NAME
from utils.logger import get_logger
from utils.custom_exception import CustomException

logger = get_logger(__name__)

class AnimeRecommendationPipeline:
    def __init__(self, persist_dir="chroma_db/anime"):
        try:
            logger.info("Initializing Anime Recommendation Pipeline")

            vector_builder = VectorStoreBuilder(csv_path="", persist_dir=persist_dir)
            retriever = vector_builder.load_vector_store().as_retriever()

            self.recommender = AnimeRecommender(retriever, GROQ_API_KEY, MODEL_NAME)

            logger.info("Anime Pipeline initialized successfully...")

        except Exception as e:
            logger.error(f"Failed to initialize Anime pipeline {str(e)}")
            raise CustomException("Error during Anime pipeline initialization", e)

    def recommend(self, query: str) -> str:
        try:
            logger.info(f"Received Anime query: {query}")

            recommendation = self.recommender.get_recommendation(query)

            logger.info("Anime recommendation generated successfully...")
            return recommendation
        except Exception as e:
            logger.error(f"Failed to get Anime recommendation {str(e)}")
            raise CustomException("Error during Anime recommendation", e)


class MovieRecommendationPipeline:
    def __init__(self, persist_dir="chroma_db/movies"):
        try:
            logger.info("Initializing Movie Recommendation Pipeline")

            vector_builder = VectorStoreBuilder(csv_path="", persist_dir=persist_dir)
            retriever = vector_builder.load_vector_store().as_retriever()

            self.recommender = MovieRecommender(retriever, GROQ_API_KEY, MODEL_NAME)

            logger.info("Movie Pipeline initialized successfully...")

        except Exception as e:
            logger.error(f"Failed to initialize Movie pipeline {str(e)}")
            raise CustomException("Error during Movie pipeline initialization", e)

    def recommend(self, query: str) -> str:
        try:
            logger.info(f"Received Movie query: {query}")

            recommendation = self.recommender.get_recommendation(query)

            logger.info("Movie recommendation generated successfully...")
            return recommendation
        except Exception as e:
            logger.error(f"Failed to get Movie recommendation {str(e)}")
            raise CustomException("Error during Movie recommendation", e)
