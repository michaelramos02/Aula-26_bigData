import polars as pl 
import os 
from datetime import datetime 
import numpy as np
import matplotlib.pyplot as plt
os.system('cls')

ENDERECO_DADOS = r'./../dados/'

try:
    print('Lendo arquivo parquet...')
    inicio = datetime.now()

    # Leitura Preguiçosa 
    df_plano_execucao = (
        pl.scan_parquet(
            ENDERECO_DADOS + 'bolsa_familia.parquet')) 
            # DADOS
            # Delimitar as Séries
            # ... Técnica
            # Agrupar 
            # Soma 
            # Ordenar 


    
    df_bolsa_familia = df_plano_execucao.collect()
    print(df_bolsa_familia.head(10))


    # ORDENANDO E MOSTRANDO 20 PRIMEIROS 
    # print(df_bolsa_familia.sort('VALOR PARCELA', descending=True).head(20))


except Exception as e:
    print(f'Erro ao ler arquivo parquet {e}')
