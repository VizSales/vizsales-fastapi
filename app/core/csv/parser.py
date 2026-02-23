import pandas as pd
import io
from app.utils.exceptions import AppException

class CSVParser:
    @staticmethod
    def parse(contents: bytes, preview_rows: int = 5) -> dict:
        try:
            df = pd.read_csv(io.BytesIO(contents))
        except Exception:
            raise AppException(status_code=400, message="Invalid or corrupted CSV file")

        if df.empty:
            raise AppException(status_code=400, message="CSV file is empty")

        return {
            "rows": len(df),
            "columns": df.columns.tolist(),
            "dtypes": {col: str(dtype) for col, dtype in df.dtypes.items()},
            "preview": df.head(preview_rows).fillna("").to_dict(orient="records"),
        }