## 🛠️ Tratando os Dados

Na etapa anterior, foram obtidos dados de diferentes fontes. Agora, é necessário organizá-los e entender sua estrutura antes de utilizá-los nos modelos.

### 📌 1. Concatenando os Arquivos de Vazão
Os dados de vazão e precipitação, obtidos por meio do plugin da **ANA (Agência Nacional de Águas)**, vieram em **múltiplos arquivos `.txt`** — um para cada gauge. Para consolidar as informações em um único **arquivo `.csv`**, foi necessário concatenar os dados. Segue o exemplo do processo para os dados de vazão:

🔹 **Processo realizado:**
- Os arquivos `.txt` foram armazenados na pasta `gauges_vazao/`.
- Utilizamos **Python** com as bibliotecas `os`, `pandas` e `numpy` para criar um DataFrame consolidado chamado **`DF_final_vazao`**.
- Durante o processo, **valores ausentes foram removidos** para evitar inconsistências.

### **📝 Código (Clique para Expandir)**
<details>
  <summary>🔍 Ver Código Python</summary>

  ```python
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
          
          # Adiciona uma coluna com o nome do arquivo
          DF_vazao['CD_estacao'] = arquivo_vazao
          dfs_vazao.append(DF_vazao)

  # Concatena os DataFrames em partes menores
  tamanho_parte = 30  # ajuste conforme necessário
  partes = [pd.concat(dfs_vazao[i:i+tamanho_parte], ignore_index=True) 
            for i in range(0, len(dfs_vazao), tamanho_parte)]

  # Concatena as partes para obter o DataFrame final
  DF_final_vazao = pd.concat(partes, ignore_index=True)

  # Renomear as colunas
  DF_final_vazao = DF_final_vazao.rename(columns={0: 'dia', 1: 'mes', 2:'ano', 3:'vazao_diaria'})

  # Remove o termo ".txt" da coluna 'CD_estacao'
  DF_final_vazao['CD_estacao'] = DF_final_vazao['CD_estacao'].str.replace('.txt', '')

  # Converte a coluna 'vazao_diaria' para numérica e trata valores negativos como NaN
  DF_final_vazao['vazao_diaria'] = pd.to_numeric(DF_final_vazao['vazao_diaria'], errors='coerce')
  DF_final_vazao['vazao_diaria'] = np.where(DF_final_vazao['vazao_diaria'] < 0, np.nan, 
                                             DF_final_vazao['vazao_diaria'])

  # Remove linhas com valores NaN
  DF_final_vazao = DF_final_vazao.dropna()

  # Salva em CSV
  DF_final_vazao.to_csv('DF_vazao.csv', index=False)
  ```

</details>


📊 **Recorte do resultado gerado:**
![resultado_concatenado](https://github.com/user-attachments/assets/98895d11-6874-405a-8073-f5f01b8429ff)

---

### 🌍 2. Distribuição Espacial das Variáveis Numéricas
Após o tratamento inicial, foi realizada uma **distribuição espacial** dos dados de cada variável numérica por ano.

🔹 **Técnica utilizada:**
- **Método IDW (Inverse Distance Weighting)**, disponível no **QGIS**.
- O IDW gera **mapas interpolados**, atribuindo pesos às medições com base na proximidade dos pontos.
- Tutorial: VasGeo - Soluções em Geotecnologias
🔗 [Assista aqui](https://www.youtube.com/watch?v=_4K5pK2On1Y)

---

### 📌 3. Amostragem Espacial dos Dados
Com os mapas interpolados das variáveis numéricas e os mapas classificados da variável categórica, foi realizada a **amostragem de dados**.

🔹 **Processo realizado:**
- Utilizou-se a ferramenta **"Criação de Pontos Regulares"** do **QGIS** para definir os pontos de amostragem.
- Os valores das variáveis foram extraídos das camadas raster geradas pela interpolação.
- Tutorial: TecnoGIS 
🔗 [Assista aqui](https://www.youtube.com/watch?v=KjjYAOZZqHM)
---

### 📊 4. Estatísticas Descritivas
A análise estatística descritiva foi realizada utilizando **Pandas**.

🔹 **Funções utilizadas:**
- `describe()` → Para variáveis **numéricas**.
- `value_counts()` → Para variáveis **categóricas**.

📈 **Resultados das estatísticas descritivas:**
- **Variáveis numéricas:**
 ![stat_numericos](https://github.com/user-attachments/assets/58a338a3-3ca4-49c8-929a-ed726518043f)
- **Variáveis categóricas:**
![stat_categoricos](https://github.com/user-attachments/assets/5bb39556-5a77-4217-b6d7-175f3a50f2be)

---

### 🎯 Resumo do Processo
👉 **Concatenamos os arquivos de vazão em um único `.csv`** usando Python.
👉 **Interpolamos espacialmente os dados numéricos** com IDW no QGIS.
👉 **Criamos pontos de amostragem e extraímos valores das variáveis rasterizadas.**
👉 **Realizamos estatísticas descritivas para entender a distribuição dos dados.**

---

- Para maiores detalhes, consultar o pdf do trabalho.
