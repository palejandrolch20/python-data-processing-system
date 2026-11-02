
from pathlib import Path

from data_processor.ingestion.file_reader import FileReader


def main() -> None:

    reader = FileReader()

    file_path = Path("data/input/text.txt")

    df = reader.read(file_path)

    print(df)


if __name__ == "__main__":
    main()
