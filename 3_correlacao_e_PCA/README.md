# Análise de Correlação de Spearman e PCA

Esta etapa apresenta a análise de correlação de Spearman e Análise por Componentes Principais (PCA) aplicada ao conjunto de dados ambientais,
utilizando o R-Studio.

## 1. Introdução
Após o tratamento dos dados brutos e a espacialização das variáveis, foi realizada a correlação de Spearman. Este método é mais adequado para avaliar relações não lineares entre as variáveis.

## 2. Instalação e Carregamento dos Pacotes no R
```r
install.packages(c("readr", "Hmisc", "ggplot2", "plotly", "reshape2", "dplyr", "psych", "PerformanceAnalytics", "kableExtra", "ggrepel"))

library(readr)
library(Hmisc)
library(ggplot2)
library(plotly)
library(reshape2)
library(dplyr)
library(psych)
library(PerformanceAnalytics)
library(kableExtra)
library(ggrepel)
```

## 3. Correlação de Spearman no R
```r
# Carregar a base de dados
df_amostra <- read_csv("q95_caatinga_RHSF_exemplo.csv")

# Removendo a coluna de dados categóricos
df_filtrado <- df_amostra[, -c(1,3,9)]  

# Calculando a matriz de correlação de Spearman
rho <- rcorr(as.matrix(df_filtrado[, 1:6]), type="spearman")  

# Criando um mapa de calor das correlações
ggplotly(
  df_filtrado[,1:6] %>%
    cor(method = "spearman") %>%
    melt() %>%
    rename(Correlação = value) %>%
    ggplot() +
    geom_tile(aes(x = Var1, y = Var2, fill = Correlação)) +
    geom_text(aes(x = Var1, y = Var2, label = format(round(Correlação, 4))), size = 4) +
    scale_fill_gradient2(low = "orangered4", mid = "white", high = "slateblue4", name = "Correlação") +
    labs(x = NULL, y = NULL) +
    theme_bw(base_size = 12)
)
```

![spearman](https://github.com/user-attachments/assets/3ba97653-8015-4592-b2e5-04ad634e5cad)

### Resultados
As variáveis analisadas não apresentaram altas correlações. Os pares mais correlacionados foram:
- **Velocidade do vento e precipitação** (-0,57)
- **Temperatura e umidade do ar** (-0,56)
- **Precipitação e umidade do ar** (0,54)

## 4. Análise por Componentes Principais (PCA) no R
A PCA é uma técnica de redução dimensional que busca identificar correlações entre variáveis originais e reduzir a complexidade dos dados.

```r
# Teste de Esfericidade de Bartlett
cortest.bartlett(df_filtrado[, 1:5])

# Realizando PCA
fatorial <- principal(df_filtrado[,1:5], nfactors = length(df_filtrado[,1:5]), rotate = "none", scores = TRUE)
print(fatorial)

# Obtendo os autovalores
eigenvalues <- round(fatorial$values, 2)
print(eigenvalues)

# Definição da quantidade de fatores (autovalores > 1)
k <- sum(eigenvalues > 1)

# PCA com os fatores selecionados
fatorial2 <- principal(df_filtrado[,1:5], nfactors = k, rotate = "none", scores = TRUE)
print(fatorial2)
```

```r
# Criando o gráfico de cargas fatoriais
cargas_fatoriais <- as.data.frame(unclass(fatorial2$loadings))

ggplot(cargas_fatoriais, aes(x = PC1, y = PC2, label = rownames(cargas_fatoriais))) +
  geom_point(color = "darkorchid", size = 3) +
  geom_text_repel(size = 5) +
  geom_vline(aes(xintercept = 0), linetype = "dashed", color = "orange") +
  geom_hline(aes(yintercept = 0), linetype = "dashed", color = "orange") +
  expand_limits(x = c(-1, 1), y = c(-1, 1)) +
  theme_bw(base_size = 14) +
  labs(title = "Gráfico de Cargas Fatoriais",
       x = paste0("PC1 (", round(fatorial2$Vaccounted[2,1] * 100, 1), "% da variância)"),
       y = paste0("PC2 (", round(fatorial2$Vaccounted[2,2] * 100, 1), "% da variância)"))
```

![PCA](https://github.com/user-attachments/assets/9c043dfc-3e87-4129-9acd-f22b532ced34)

### Resultados
Os dois primeiros componentes principais explicaram **72,5%** da variância dos dados originais:
- **PC1**: Relacionado à temperatura (-0,704) e umidade do ar (0,848), sugerindo representação de condições climáticas úmidas e frias.
- **PC2**: Relacionado à radiação solar (0,834) e velocidade do vento (-0,516), inferindo condições de alta radiação solar e vento fraco.

## 5. Conclusão
A análise indicou que as variáveis estão inter-relacionadas, e a PCA ajudou a resumir essas relações sem perda significativa de informação. 
Optou-se por manter todas as variáveis na modelagem, garantindo uma representação completa do sistema climático na Região Hidrográfica do São Francisco.

---
**Referência:** Fávero, L. P., & Belfiore, P. (2017). Análise de dados: modelagem multivariada para tomada de decisão. Elsevier Brasil.

