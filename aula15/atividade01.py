import polars as pl 
import os 
from datetime import datetime 
import numpy as np
import matplotlib.pyplot as plt
os.system('cls')

pl.Config.set_fmt_float('full')
ENDERECO_DADOS = r'./../dados_atividades/'

try:
    print('Lendo arquivo parquet...')
    inicio = datetime.now()
    
    df_plano_execucao = (
        pl.scan_parquet(ENDERECO_DADOS + 'auxilio_brasil.parquet')
        .select(['NOME MUNICÍPIO', 'VALOR PARCELA'])
        .with_columns([pl.col('NOME MUNICÍPIO').cast(pl.Categorical)])
        .group_by('NOME MUNICÍPIO')
        .agg(pl.col('VALOR PARCELA').sum())
        .sort('VALOR PARCELA', descending=True)

    )


    df_auxilio = df_plano_execucao.collect()
    print(df_auxilio.head(10))

    final = datetime.now()
    print(f'\nTotal de tempo gasto: {final - inicio}')


except Exception as e:
    print(f'Erro ao ler arquivo parquet {e}')
