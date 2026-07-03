import polars as pl 
import os 
from datetime import datetime 
import numpy as np
import matplotlib.pyplot as plt
os.system('cls')

pl.Config.set_fmt_float('full')
ENDERECO_DADOS = r'./../dados/'

try:
    print('Lendo arquivo parquet...')
    inicio = datetime.now()

    # Leitura Preguiçosa 
    df_plano_execucao = (
            pl.scan_parquet(ENDERECO_DADOS + 'bolsa_familia.parquet') # DADOS
            .select(['NOME MUNICÍPIO', 'VALOR PARCELA']) # Delimitar as Séries
            .with_columns([pl.col('NOME MUNICÍPIO').cast(pl.Categorical)]) # Cria uma tabela de numeros, subistituindo os nomes das cidades
            .group_by('NOME MUNICÍPIO') # Agrupar
            .agg(pl.col('VALOR PARCELA').sum()) # Soma 
            .sort('VALOR PARCELA', descending=True)# Ordenar 
    )

    
    df_bolsa_familia = df_plano_execucao.collect()
    print(df_bolsa_familia.head(10))


    # ORDENANDO E MOSTRANDO 20 PRIMEIROS 
    # print(df_bolsa_familia.sort('VALOR PARCELA', descending=True).head(20))
    final = datetime.now()
    print(f'\nTotal de tempo gasto {final-inicio}')

except Exception as e:
    print(f'Erro ao ler arquivo parquet {e}')
