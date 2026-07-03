import polars as pl 
import os 
from datetime import datetime

os.system('cls')

ENDERECO_DADOS = r'./../dados_atividades/'

try:
    print('Obtendo os dados...')
    inicio =  datetime.now()
    
    lista_csv = []

    df_auxilio_brasil = None 

    arquivos = os.listdir(ENDERECO_DADOS)

    for i in arquivos:
        if i.endswith('.csv'):
            lista_csv.append(i)


    for i in lista_csv:
        df = pl.read_csv(ENDERECO_DADOS + i, separator=';', encoding='iso-8859-1')

        print(df.head())

        if df_auxilio_brasil is None:
            df_auxilio_brasil = df 
        else:
            df_auxilio_brasil = pl.concat([df_auxilio_brasil, df])

        del df 

        print(f'\nArquivo {i} processado com sucesso!')
        print(df_auxilio_brasil.shape)

    df_auxilio_brasil = df_auxilio_brasil.with_columns(pl.col('VALOR PARCELA').str.replace(',', '.').cast(pl.Float64))


    print('\nIniciando a gravação do arquivo parquet...')

    df_auxilio_brasil.write_parquet(ENDERECO_DADOS + 'auxilio_brasil.parquet')

    print('\nArquivo salvo com sucesso!')

    final = datetime.now()

    print(f'\nTotal de tempo gasto {final - inicio}')

except Exception as e:
    print(f'Erro ao obter os dados {e}')