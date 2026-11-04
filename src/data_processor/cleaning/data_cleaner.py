import pandas as pd


class DataCleaner:


    def handle_missing_values(self, df: pd.DataFrame) -> pd.DataFrame:
        #Pass works like a null operation, allow to keep coding without code the full function
        cleaned_df = df.dropna()

        return cleaned_df
          
        
    def remove_duplicates(self, df: pd.DataFrame) -> pd.DataFrame:
        #Find and remove duplicates
        cleaned_df = df.drop_duplicates()
        return cleaned_df


    def normalize_text(self, df: pd.DataFrame) -> pd.DataFrame:
        #Normalize text
        cleaned_df = df.copy()
        cleaned_df["machine"] = (
            cleaned_df["machine"]
            .str.strip()
            .str.title()
            )
        return cleaned_df
        

        

    def clean_data(self, df: pd.DataFrame) -> pd.DataFrame:
        #Orchest

        df = self.handle_missing_values(df)
        df = self.normalize_text(df)
        df = self.remove_duplicates(df)
        df = df.reset_index()

        return df
    