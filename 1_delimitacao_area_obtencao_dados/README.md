# 🗺️ Delimitação da Área de Estudo e Obtenção dos Dados

## 📌 Definição da Área de Estudo
A primeira etapa consiste na escolha da área a ser estudada. Aqui, escolhi a porção do bioma Caatinga localizada na Região Hidrográfica do São Francisco.  
Utilizei o software **QGIS** para fazer a interseção entre os vetores das áreas referentes ao **bioma Caatinga** e à **Região Hidrográfica do São Francisco**.  

🎥 **Tutorial:** O vídeo do canal *Geoaplicada* no YouTube explica rapidamente como fazer esse processo:  
🔗 [Assista aqui](https://www.youtube.com/watch?v=xCaDnaDI3zw)  

🖼️ **Mapa da região de estudo:**
<img src="[https://user-images.githubusercontent.com/123456789/abcdefg.png](https://github.com/user-attachments/assets/e4d712bc-703b-4fef-8189-8655eb899c00)" alt="Minha Figura" width="600px">

---

## 📊 Obtenção dos Dados
Foram obtidos dados referentes a:
- **5 variáveis explicativas numéricas**: precipitação, temperatura, radiação, umidade do ar e velocidade do vento.
- **1 variável explicativa categórica**: tipo de uso e cobertura do solo.
- **1 variável resposta numérica**: vazão.

🖼️ **Fontes dos dados:**
![bases_obtencao_dados](https://github.com/user-attachments/assets/1b88953a-3c47-4766-b049-c7c2538bb691)

### 🔹 Fontes de Dados:
- **Precipitação e Vazão**: Obtidos de estações pluviométricas e fluviométricas pelo **plugin ANA Data Acquisition (QGIS)**.  
🎥 **Tutorial:** O canal *Prof. Águas* no YouTube ensina como realizar esse processo:  
🔗 [Assista aqui](https://www.youtube.com/watch?v=G-KgiA3Bk8Y)

- **Uso e cobertura do solo**: Obtidos por meio dos Toolkits preparados no Google Earth Engine (GEE) pelo projeto **MAPBIOMAS**.
🎥 **Tutorial:** O canal *MapBiomas Brasil* no YouTube mostra como ter acesso aos dados:
🔗 [Assista aqui](https://www.youtube.com/watch?v=OBqaoSuLGbk&t=343s)

- **Demais dados:**
  - 🌍 **Shapefile das Regiões Hidrográficas** - [Agência Nacional de Águas](https://metadados.snirh.gov.br/geonetwork/srv/api/records/0574947a-2c5b-48d2-96a4-b07c4702bbab) *(acessado em 09/01/2024)*.
  - 🌱 **Shapefile do Bioma Caatinga** - [IBGE](https://www.ibge.gov.br/geociencias/cartas-e-mapas/informacoes-ambientais/15842-biomas.html?edicao=25799&t=acesso-ao-produto) *(acessado em 09/01/2024)*.
  - 🏞️ **Shapefile das Subregiões do São Francisco** - [Comitê da Bacia Hidrográfica do São Francisco](https://siga.cbhsaofrancisco.org.br/sfmap/#) *(acessado em 09/01/2024)*.
  - 🌦️ **Dados climáticos** - [INMET](https://portal.inmet.gov.br/dadoshistoricos) *(acessado em 11/04/2024)*.
  - 🗺️ **Dados de uso e cobertura do solo** - [MapBiomas](https://brasil.mapbiomas.org/) *(acessado em 10/01/2024)*.

---
Agora que os dados foram coletados, seguimos para a próxima etapa! 🚀


