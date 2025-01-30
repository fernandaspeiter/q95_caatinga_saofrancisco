import os
import pandas as pd
import numpy as np

# Caminho para a pasta contendo os arquivos TXT
caminho_gauge_vazao = 'caminho da pasta gauges_vazao'

# Lista para armazenar os DataFrames de cada arquivo
dfs_vazao = []

# Itera sobre todos os arquivos na pasta
for arquivo_vazao in os.listdir(caminho_gauge_vazao):
    if arquivo_vazao.endswith('.txt'):
        # Lê o arquivo e cria um DataFrame
        caminho_arquivo_vazao = os.path.join(caminho_gauge_vazao, arquivo_vazao)
        DF_vazao = pd.read_csv(
           caminho_arquivo_vazao, delim_whitespace=True, header=None, encoding='latin-1')  
        # Use encoding='latin-1' para lidar com possíveis problemas de codificação
        
        # Adiciona uma coluna com o nome do arquivo
        DF_vazao['CD_estacao'] = arquivo_vazao
        # Adiciona o DataFrame à lista
        dfs_vazao.append(DF_vazao)

# Concatena os DataFrames em partes menores
tamanho_parte = 30  # ajuste conforme necessário
partes = [pd.concat(dfs_vazao[i:i+tamanho_parte], 
                    ignore_index=True) for i in range(0, len(dfs_vazao), tamanho_parte)]
# Concatena as partes para obter o DataFrame final
DF_final_vazao = pd.concat(partes, ignore_index=True)

#Renomear as colunas
DF_final_vazao = DF_final_vazao.rename(columns={0: 'dia', 1: 'mes', 2:'ano', 3:'vazao_diaria'})
coluna_a_atualizar = 'CD_estacao'

# Remove o termo específico de todas as linhas da coluna
termo_a_remover = '.txt'
DF_final_vazao['CD_estacao'] = DF_final_vazao['CD_estacao'].str.replace('.txt', '')

# Converte a coluna 'vazao' para numérica, caso ainda não seja
DF_final_vazao['vazao_diaria'] = pd.to_numeric(DF_final_vazao['vazao_diaria'], errors='coerce')

#Transforma valores negativos em NaN
DF_final_vazao['vazao_diaria'] = np.where(DF_final_vazao['vazao_diaria'] < 0, np.nan, 
   DF_final_vazao['vazao_diaria'])
#Remove linhas com NaN
DF_final_vazao = DF_final_vazao.dropna()

#salvar em csv
DF_final_vazao.to_csv('DF_vazao.csv', index=False)