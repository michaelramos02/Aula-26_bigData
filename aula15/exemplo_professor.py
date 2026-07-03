# import pandas as pd 
import polars as pl  
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

# Tirar a notação científica do valor no terminal
pl.Config.set_fmt_float("full")

ENDERECO_DADOS = r'./../dados/'

try:
    print('Lendo arquivo Parquet')
    inicio = datetime.now()

    # with pl.StringCache():  # depreciado - ñ é mais usado

    # leitura preguiçosa
    df_plano_execucao = (
        pl.scan_parquet(ENDERECO_DADOS + 'bolsa_familia.parquet') # dados
            # Delimitar as Séries 
            .select(['NOME MUNICÍPIO', 'VALOR PARCELA']) 
            .with_columns([
                # Cria uma Tabela de números, substituindo os nomes das cidades
                pl.col('NOME MUNICÍPIO').cast(pl.Categorical)  
            ])
            .group_by('NOME MUNICÍPIO')  # Agrupar            
            .agg(pl.col('VALOR PARCELA').sum())  # Soma            
            .sort('VALOR PARCELA', descending=True)  # Ordenar
          )
    
    print('\nPlano de Execução')
    # print(df_plano_execucao)

    df_bolsa_familia = df_plano_execucao.collect()  # Os dados são carregados aqui
    print(df_bolsa_familia.head(10))
    # print(df_bolsa_familia.columns)  # Mostrar os nomes das séries

    final = datetime.now()
    print(f'Tempo de execução {final - inicio}')
except Exception as e:
    print(f'Erro ao ler arquivo parquert {e}')