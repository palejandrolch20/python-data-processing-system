import pandas as pd


class DataValidator:

    REQUIERED_COLUMNS = [
        "machine",
        "production",
        "defects",
        "efficiency"
    ]

    NUMERIC_COLUMNS = [
        "production",
        "defects",
        "efficiency"
    ]


    def validate_columns(self, df : pd.DataFrame) -> bool :

        #List Comprehensions
        missing_columns = [
            column
            for column in self.REQUIERED_COLUMNS
            if column not in df.columns
        ]


        ## In case miss any column
        if missing_columns:
            raise ValueError(
                f"Missing required Columns: {missing_columns}"
            )

        return True
        
    def validate_types(self, df : pd.DataFrame) -> bool :

        self.validate_columns(df)

        invalid_columns = []

        machine_is_text = df["machine"].dropna().map(
            lambda value :isinstance(value,str) and not value.isdigit()
        ).all()

        if not machine_is_text:
            invalid_columns.append("machine")


        for column in self.NUMERIC_COLUMNS:
            if not pd.api.types.is_numeric_dtype(df[column]):
                invalid_columns.append(column)

        if invalid_columns:
            raise TypeError(
                f"Invalid data types in columnas: {invalid_columns}"
            )

        return True


    def validate_business_rules(self, df : pd.DataFrame) -> bool:
        business_errors = []

        #Determinate if any Machine is empty or null

        machine_is_empty = (df["machine"].isna().any() 
        | df["machine"].str.strip().eq("")).any()

        if machine_is_empty:
            business_errors.append("Machine cannot be empty or null")

        productions_out_of_range = []

        for value in df["production"]:
            if (value < 0) :
                business_errors.append(f"Production cannot be negative: {value}")

        defects_out_of_range = []
        for value in df["defects"]:
                    if (value <= 0) :
                        business_errors.append(f"Production cannot be negative: {value}")
        
        efficiency_out_of_range = []

        for value in df["efficiency"]:
             if (value < 0 or value > 100):
                  business_errors.append(f"Efficiency must be between 0 and 100: {value}")


        if business_errors:
                    raise ValueError(
                      f"Business Errors: {business_errors}"
                 )
                  
                  
                  
        

    



    