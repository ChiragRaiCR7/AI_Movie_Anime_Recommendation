from src.data_loader import AnimeDataLoader, MovieDataLoader
from src.vector_store import VectorStoreBuilder
from dotenv import load_dotenv
from utils.logger import get_logger
from utils.custom_exception import CustomException

load_dotenv()
logger = get_logger(__name__)

def main():
    try:
        logger.info("Starting to build pipelines...")

        # ---------------- ANIME ----------------
        anime_loader = AnimeDataLoader("data/anime_with_synopsis.csv", "data/anime_updated.csv")
        processed_anime_csv = anime_loader.load_and_process()
        logger.info("Anime data loaded and processed...")

        anime_vector_builder = VectorStoreBuilder(processed_anime_csv, persist_dir="chroma_db/anime")
        anime_vector_builder.build_and_save_vectorstore()
        logger.info("Anime vector store built successfully...")

        # ---------------- MOVIES ----------------
        movie_loader = MovieDataLoader("data/mpst_full_data.csv", "data/movie_updated.csv")
        processed_movie_csv = movie_loader.load_and_process()
        logger.info("Movie data loaded and processed...")

        movie_vector_builder = VectorStoreBuilder(processed_movie_csv, persist_dir="chroma_db/movies")
        movie_vector_builder.build_and_save_vectorstore()
        logger.info("Movie vector store built successfully...")

        logger.info("All pipelines built successfully....")

    except Exception as e:
        logger.error(f"Failed to execute pipeline {str(e)}")
        raise CustomException("Error during pipeline execution", e)

if __name__ == "__main__":
    main()
