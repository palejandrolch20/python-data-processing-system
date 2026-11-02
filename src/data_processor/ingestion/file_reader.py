from pathlib import Path
import pandas as pd

class FileReader:
    def read(self,file_path: str | Path) -> pd.DataFrame:

        """
        Read a file and returns its content as a Pandas DataFrame
        """
        path = Path(file_path)

        # Validate file existence

        if not path.exists():
            raise FileNotFoundError(
                f"File not Found: {path}"
            )

        #Determinate Extension
        extension = path.suffix.lower()
        #Read CSV

        if extension ==".csv":
            return pd.read_csv(path)

        #Read Excel

        if extension ==".xlsx":
            return pd.read_excel(path)

        # Read Json

        elif extension == ".json":
            return pd.read_json(path)

        # Wrong Format

        else :
            raise ValueError(
                f"Unsuppported file format: {extension}"
            )