
from pathlib import Path

from data_processor.ingestion.file_reader import FileReader
from data_processor.validation.data_validator import DataValidator
from data_processor.cleaning.data_cleaner import DataCleaner
from data_processor.analysis.data_analyzer import DataAnalyzer

def main() -> None:

    reader = FileReader()
    validator = DataValidator()
    cleaner = DataCleaner()
    analizer = DataAnalyzer()

    file_path = Path("data/input/production.csv")

    df = reader.read(file_path)

    
    validator.validate_types(df)
    validator.validate_columns(df)
    validator.validate_business_rules(df)
    print("Original Data")
    print(df)
    df = cleaner.clean_data(df)
    print("Data Validation Successful!")
    print("Data clean")
    print(df)
    metrics = analizer.calculate_metrics(df)
    print(metrics)


if __name__ == "__main__":
    main()
