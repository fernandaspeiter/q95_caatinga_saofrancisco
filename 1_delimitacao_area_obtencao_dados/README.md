# 🗺️ Delimitação da Área de Estudo e Obtenção dos Dados

## 📌 Definição da Área de Estudo
A primeira etapa consiste na escolha da área a ser estudada. Aqui, escolhi a porção do bioma Caatinga localizada na Região Hidrográfica do São Francisco.  
Utilizei o software **QGIS** para fazer a interseção entre os vetores das áreas referentes ao **bioma Caatinga** e da **Região Hidrográfica do São Francisco**.  

🎥 **Tutorial:** O vídeo do canal *Geoaplicada* no YouTube explica rapidamente como fazer esse processo:  
🔗 [Assista aqui](https://www.youtube.com/watch?v=xCaDnaDI3zw)  

🖼️ **Figura:**
![Área de estudo](visuals/area_estudo.png)

---

## 📊 Obtenção dos Dados
Foram obtidos dados referentes a:
- **5 variáveis explicativas numéricas**: precipitação, temperatura, radiação, umidade do ar e velocidade do vento.
- **1 variável explicativa categórica**: tipo de uso e cobertura do solo.
- **1 variável resposta numérica**: vazão.

🖼️ **Figura:**
![Bases de obtenção de dados](visuals/bases_obtencao_dados.png)

### 🔹 Fontes de Dados:
- **Precipitação e Vazão**: Obtidos de estações pluviométricas e fluviométricas pelo **plugin ANA Data Acquisition (QGIS)**.  
🎥 **Tutorial:** O canal *Prof. Águas* no YouTube ensina como realizar esse processo:  
🔗 [Assista aqui](https://www.youtube.com/watch?v=G-KgiA3Bk8Y)

- **Demais dados:**
  - 🌍 **Shapefile das Regiões Hidrográficas** - [Agência Nacional de Águas](https://metadados.snirh.gov.br/geonetwork/srv/api/records/0574947a-2c5b-48d2-96a4-b07c4702bbab) *(acessado em 09/01/2024)*.
  - 🌱 **Shapefile do Bioma Caatinga** - [IBGE](https://www.ibge.gov.br/geociencias/cartas-e-mapas/informacoes-ambientais/15842-biomas.html?edicao=25799&t=acesso-ao-produto) *(acessado em 09/01/2024)*.
  - 🏞️ **Shapefile das Subregiões do São Francisco** - [Comitê da Bacia Hidrográfica do São Francisco](https://siga.cbhsaofrancisco.org.br/sfmap/#) *(acessado em 09/01/2024)*.
  - 🌦️ **Dados climáticos** - [INMET](https://portal.inmet.gov.br/dadoshistoricos) *(acessado em 11/04/2024)*.
  - 🗺️ **Dados de uso e cobertura do solo** - [MapBiomas](https://brasil.mapbiomas.org/) *(acessado em 10/01/2024)*.

---
Agora que os dados foram coletados, seguimos para a próxima etapa! 🚀


