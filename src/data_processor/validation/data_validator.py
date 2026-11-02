import pandas as pd


class DataValidator:

    REQUIERED_COLUMNS = [
        "machine",
        "production",
        "defects",
        "efficiency"
    ]

    def validate_columns(self, df = pd.DataFrame) -> bool :

        #List Comprehensions
        missing_columns = [
            column
            for column in self.REQUIERED_COLUMNS
            if column not in df.columns
        ]


        ## In case miss any column
        if missing_columns:
            raise ValueError(
                f"Missing requiered Columns: {missing_columns}"
            )

        
        

    



    