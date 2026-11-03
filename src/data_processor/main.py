
from pathlib import Path

from data_processor.ingestion.file_reader import FileReader
from data_processor.validation.data_validator import DataValidator

def main() -> None:

    reader = FileReader()
    validator = DataValidator()

    file_path = Path("data/input/production.csv")

    df = reader.read(file_path)

    validator.validate_types(df)
    validator.validate_columns(df)
    
    print("Data Validation Successful!")
    print(df)


if __name__ == "__main__":
    main()
