from pathlib import Path 
from unittest.mock import patch #simmulacion mock

import pandas as pd
import pytest

from pipeline.ingest import ingest_data

def test_ingest_data_creates_file(tmp_path):# carpeta temporal vacia
    fake_df=pd.DataFrame({
        "Transaction ID": [' TXN_1961373 ' , ' TXN_4977031 '],
        "Item":[' Coffee ' , ' Cake '],
        "Quantity":[ 2,4 ],
        "Price Per Unit":[ 2.0,3.0 ],
        "Total Spent":[4,12],
        "Payment Method":[' Credit Card ' , ' Cash '],
        "Location":[' Takeaway ' , ' In-store '],
        "Transaction Date":[' 2023-09-08 ' , ' 2023-05-16 ']
    })
    test_file=tmp_path/"dirty_cafe_sales_test.csv"
    with patch("pipeline.ingest.pd.read_csv",return_value=fake_df):
        result=ingest_data(output_path=test_file)#aqui prueba ingest_data()
    
    assert isinstance(result, Path)
    assert result.exists()
    assert result.name=="dirty_cafe_sales_test.csv"

    df_result=pd.read_csv(result)

    assert len(df_result)==2
    assert "Payment Method" in df_result.columns

@pytest.mark.integration #test de integracion
def test_ingest_data_downloads_from_github(tmp_path):
    test_file=tmp_path/"dirty_cafe_sales_test.csv" #ruta temporal
    result=ingest_data(output_path=test_file)#ejecuta la funcion de ingest_data() con la ruta temporal como argumento
    assert isinstance(result,Path) #verifica que el resultado sea una instancia de Path
    assert result==test_file #verifica que el resultado sea el mismo archivo de salida
    assert result.is_file() #verifica que el archivo exista
    assert result.stat().st_size>0 #verifica que el archivo tenga un tamaño mayor a 0

    df_result=pd.read_csv(result) #lee el archivo result en un DataFrame de pandas
    expectecd_columns=[ 
        "Transaction ID",
        "Item",
        "Quantity",
        "Price Per Unit",
        "Total Spent",
        "Payment Method",
        "Location",
        "Transaction Date"] #lista de columnas esperadas eb el df_result
    assert not df_result.empty
    assert list(df_result.columns)==expectecd_columns #verifica que las columnas del df_result sean iguales a las columnas esperadas
    

    


