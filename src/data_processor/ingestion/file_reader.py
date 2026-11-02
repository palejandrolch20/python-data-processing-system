from pathlib import Path
import pandas as pd


class FileReader:

    def read(self, file_path: str | Path) -> pd.DataFrame:

        """
        Reads a file and returns its content as a Pandas DataFrame.
        """

        path = Path(file_path)

        # Validate file existence
        if not path.exists():
            raise FileNotFoundError(
                f"File not found: {path}"
            )

        # Validate that the path is a file
        if not path.is_file():
            raise IsADirectoryError(
                f"Path is not a file: {path}"
            )

        # Identify file extension
        extension = path.suffix.lower()

        # Read supported formats
        if extension == ".csv":
            return pd.read_csv(path)

        elif extension == ".xlsx":
            return pd.read_excel(path)

        elif extension == ".json":
            return pd.read_json(path)

        else:
            raise ValueError(
                f"Unsupported file format: {extension}"
            )