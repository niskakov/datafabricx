import pandas as pd
import pdfplumber
from io import BytesIO

def parse_csv(file: BytesIO) -> pd.DataFrame:
    return pd.read_csv(file)

def parse_excel(file: BytesIO) -> pd.DataFrame:
    return pd.read_excel(file)

def parse_pdf(file: BytesIO) -> pd.DataFrame:
    with pdfplumber.open(file) as pdf:
        all_tables = []
        for page in pdf.pages:
            table = page.extract_table()
            if table:
                df = pd.DataFrame(table[1:], columns=table[0])
                all_tables.append(df)
        if not all_tables:
            return pd.DataFrame()
        return pd.concat(all_tables, ignore_index=True)
