from pathlib import Path 
from unittest.mock import patch #simmulacion mock
import pandas as pd
from pipeline.ingest import ingest_data

def test_ingest_data_creates_file(tmp_path):# carpeta temporal vacia
    fake_df=pd.DataFrame({
        "Name":["PIKACHU","CHARMANDER"],
        "Type 1":["electric","fire"]
    })
    test_file=tmp_path/"pokemon_test.csv"
    with patch("pipeline.ingest.pd.read_csv",return_value=fake_df):
        result=ingest_data(output_path=test_file)
    
    assert isinstance(result, Path)
    assert result.exists()
    assert result.name=="pokemon_test.csv"

    df_result=pd.read_csv(result)

    assert len(df_result)==2
    assert "Name" in df_result.columns

