import pandas as pd
from fastapi import UploadFile
from typing import List, Dict

async def parse_file(file: UploadFile) -> List[Dict]:
    try:
        # Read the file
        if file.filename.endswith(".csv"):
            df = pd.read_csv(file.file)
        elif file.filename.endswith(".xlsx"):
            df = pd.read_excel(file.file, engine="openpyxl")
        else:
            raise ValueError("Only CSV or XLSX files are supported.")

        # DEBUG PRINT actual raw column names
        print("Raw columns from Excel/CSV:", df.columns.tolist())

        # Clean column headers
        df.columns = [str(col).strip().lower().replace(" ", "_") for col in df.columns]

        # DEBUG PRINT after normalization
        print("Normalized columns:", df.columns.tolist())

        # Required columns check
        required_columns = ["part_number", "year", "category", "model", "vehicle_type", "color", "price", "stock"]
        missing = [col for col in required_columns if col not in df.columns]
        if missing:
            raise ValueError(f"Missing required columns in Excel/CSV: {missing}")

        # Data type conversion
        df["price"] = df["price"].replace(r"[\$,]", "", regex=True).astype(float)
        df["stock"] = df["stock"].astype(int)
        df["year"] = df["year"].astype(int)
        df["part_number"] = df["part_number"].astype(str)

        return df.to_dict(orient="records")

    except Exception as e:
        raise ValueError(f"Failed to parse file: {e}")
