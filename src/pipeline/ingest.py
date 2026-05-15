from pathlib import Path
import pandas as pd

URL="https://raw.githubusercontent.com/AngelTintaya/datasets/main/pokemon.csv"

PROJECT_ROOT=Path(__file__).resolve().parents[2]
RAW_DIR=PROJECT_ROOT/"data"/"raw"
RAW_FILE=RAW_DIR/"pokemon_raw.csv"

def ingest_data() ->Path:
    """
    fgbfdescarga el dataset desde una url y lo guarda en data/raw
    retonar la ruta del archivo guardado
    """
    print("Inciando ingesta de datos...")
    RAW_DIR.mkdir(parents=True,exist_ok=True)
    df=pd.read_csv(URL)

    df.to_csv(RAW_FILE,index=False)
    
    print(f"Filas descargadas: {len(df)}")
    print(f"Columnas descargadas: {len(df.columns)}")
    print(f"archivo guardado en: {RAW_DIR}")

    return RAW_FILE





