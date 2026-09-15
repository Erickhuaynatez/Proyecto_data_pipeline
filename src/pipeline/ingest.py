from pathlib import Path
import pandas as pd

URL="https://raw.githubusercontent.com/shaadyalii/Dirty-Cafe-Sales-Dataset/main/dirty_cafe_sales.csv" 

PROJECT_ROOT=Path(__file__).resolve().parents[2]
RAW_DIR=PROJECT_ROOT/"data"/"raw"
DEFAULT_RAW_FILE=RAW_DIR/"dirty_cafe_sales.csv"

def ingest_data(output_path: Path=DEFAULT_RAW_FILE) -> Path:

    print("Inciando ingesta de datos...")
    output_path.parent.mkdir(parents=True,exist_ok=True)
    df=pd.read_csv(URL)

    df.to_csv(output_path,index=False)
    
    print(f"Filas descargadas: {len(df)}")
    print(f"Columnas descargadas: {len(df.columns)}")
    print(f"archivo guardado en: {output_path}")

    return output_path





