import pandas as pd

class AnimeDataLoader:
    def __init__(self,original_csv:str,processed_csv:str):
        self.original_csv = original_csv
        self.processed_csv = processed_csv

    def load_and_process(self):
        df = pd.read_csv(self.original_csv , encoding='utf-8' , on_bad_lines='skip').dropna()

        required_cols = {'Name' , 'Genres','sypnopsis'}

        missing = required_cols - set(df.columns)
        if missing:
            raise ValueError("Missing column  in CSV File")
        
        df['combined_info'] = (
            "Title: " + df["Name"] + " Overview: " +df["sypnopsis"] + "Genres : " + df["Genres"]
        )

        df[['combined_info']].to_csv(self.processed_csv , index=False,encoding='utf-8')

        return self.processed_csv

class MovieDataLoader:
    def __init__(self, original_csv: str, processed_csv: str):
        self.original_csv = original_csv
        self.processed_csv = processed_csv

    def load_and_process(self):
        # Load dataset
        df = pd.read_csv(self.original_csv, encoding='utf-8', on_bad_lines='skip').dropna()

        # Required columns
        required_cols = {'title', 'plot_synopsis', 'tags'}
        missing = required_cols - set(df.columns)
        if missing:
            raise ValueError(f"Missing columns in CSV File: {missing}")

        # Create combined_info
        df['combined_info'] = (
            "Title: " + df["title"] +
            " Overview: " + df["plot_synopsis"] +
            " Tags: " + df["tags"]
        )

        # Save only the combined_info column
        df[['combined_info']].to_csv(self.processed_csv, index=False, encoding='utf-8')

        return self.processed_csv