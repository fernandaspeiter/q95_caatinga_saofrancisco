[Voltar para a página inicial](/)

## Análise de Modelos de Regressão no R

Esta etapa apresenta a análise da capacidade de predição do conjunto de dados por meio da implementação de diferentes modelos supervisionados de regressão utilizando a linguagem de programação R. Foram considerados os seguintes modelos:

- Regressão Linear Múltipla
- Regressão Não Linear com transformação de Box-Cox
- Árvore de Regressão
- Random Forest

#### Etapas
- **Regressão Linear e Regressão Não Linear**  
![regressao_linear](https://github.com/user-attachments/assets/b62770dc-68f4-4cb9-af53-4b6c83bd68ed)

- **Árvore de Regressão**  
![arvore_regressao](https://github.com/user-attachments/assets/1254e3a9-ee56-4262-91ef-c81db5851ecb)

- **Random Forest**  
![random_forest](https://github.com/user-attachments/assets/0da686d3-4313-4754-a866-3181b37cac48)

### Parâmetros e Resultados dos Modelos

| Modelo | Parâmetros | R² |
|--------|------------|----|
| **Regressão Linear Múltipla** | Coeficientes significativos (teste t): Intercepto, Precipitação, Radiação, Temperatura, Umidade do ar, Velocidade do vento, Agropecuária, Área não vegetada, Corpo d'água, Formação natural não florestal (p-values < 0,05). Testes F, Shapiro-Francia e Breusch-Pagan significativos. | 0,33 |
| **Regressão Não Linear (Transformação de Box-Cox)** | Parâmetro Box-Cox: 0,1257. Coeficientes significativos (teste t) para todas as variáveis. Testes F, Shapiro-Francia e Breusch-Pagan significativos. | 0,35 |
| **Árvore de Regressão** | maxdepth = 30, cp = 5.105288e-08, k-fold = 10 | 0,68 |
| **Random Forest** | ntree = 50 | 0,80 |

### Conclusão
- A **Regressão Linear** apresentou coeficientes altamente significativos, mas evidenciou violações nas suposições de normalidade dos resíduos e homocedasticidade.
- A **Regressão Não Linear** com transformação de Box-Cox mostrou melhoria no R², mas ainda indicou desafios semelhantes.
- A **Árvore de Regressão** capturou relações não lineares e obteve um melhor desempenho.
- O **Random Forest** demonstrou a melhor capacidade preditiva e generalização, destacando-se como o modelo mais robusto para a previsão da vazão Q95.

Essa comparação reforça a importância de avaliar diferentes abordagens para modelagem de dados, permitindo melhor compreensão e previsão dos fenômenos analisados.
