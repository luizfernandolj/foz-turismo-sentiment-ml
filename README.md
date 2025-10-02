## Como Rodar os Experimentos (detalhado)

Os experimentos utilizam o protocolo APP (Artificial Prevalence Protocol) para avaliar quantificadores sob diferentes distribuições de classe artificialmente geradas. O fluxo é o seguinte:

- Separe os dados em conjunto de treinamento (L) e conjunto de teste (U), onde \( U \) permanece não rotulado para o quantificador.

- No conjunto de teste \( U \), realize a subamostragem repetida para gerar **50 distribuições artificiais de classes**. Essas distribuições são **uniformemente espaçadas** no intervalo de prevalência entre 0 e 1 para a classe positiva (em problemas binários). Ou seja, as prevalências testadas são:
  
  \[
  \left\{0, \frac{1}{49}, \frac{2}{49}, \frac{3}{49}, ..., 1\right\}
  \]

- Para cada uma dessas 50 distribuições, selecione amostras de cinco tamanhos diferentes que são também **uniformemente espaçados** entre um tamanho mínimo de 25 instâncias e o tamanho máximo disponível no conjunto de teste para o aspecto/categoria avaliada. Por exemplo, se o tamanho máximo disponível for \( N \), os tamanhos testados serão aproximadamente:

  \[
  \left\{25, 25 + \frac{N-25}{4}, 25 + 2 \times \frac{N-25}{4}, 25 + 3 \times \frac{N-25}{4}, N \right\}
  \]

- Para cada combinação de prevalência e tamanho de amostra, realizam-se **3 réplicas independentes** para garantir confiabilidade estatística.

- Para cada execução, é calculado o Erro Absoluto Médio (MAE) entre a distribuição verdadeira de prevalência e a estimada pelo quantificador. As métricas de todas as réplicas são então médias para análise final dos métodos.

Este protocolo permite testar os quantificadores em cenários variados de prevalência e tamanho de dados, simulando condições reais e desafiadoras para a análise robusta de sentimentos.

---


# Análise de sentimento do setor de turismo de Foz do Iguaçu utilizando aprendizado de máquina

Este projeto contém uma análise completa dos dados utilizando notebooks Python. Abaixo estão as imagens dos gráficos gerados e uma breve explicação de cada notebook.

## Gráficos

Visualize os gráficos gerados pelos relatórios em PDF:

- [Bourbon](plots/Bourbon.pdf)
- [Taroba](plots/Taroba.pdf)
- [Viale Cataratas](plots/Viale%20Cataratas.pdf)
- [Viale Tower](plots/Viale%20Tower.pdf)

## Notebooks

A seguir, uma descrição dos notebooks que compõem a análise:

1. **0. Leitura banco**  
   Responsável por conectar-se ao banco de dados e realizar a extração dos dados para posterior processamento.

2. **1. Descrição dos datasets**  
   Apresenta uma análise exploratória dos dados, mostrando informações sobre as variáveis, tipos e possíveis inconsistências.

3. **2. Padronização das colunas**  
   Realiza a normalização dos nomes das colunas e a correção de formatações para facilitar as análises subsequentes.

4. **3. Balanceamento dos datasets**  
   Implementa técnicas para balanceamento de classes nos datasets, garantindo que os algoritmos de classificação não sofram com vieses.

5. **4. Classificação com RoBERTa**  
   Utiliza o modelo RoBERTa para realizar a classificação dos dados, demonstrando a aplicação de modelos avançados de NLP.

6. **5. Quantificação**  
   Procede à quantificação dos resultados, elaborando métricas e relatórios de performance dos modelos.

7. **6. Análise**  
   Consolida os resultados obtidos em uma análise final, integrando as etapas anteriores e oferecendo insights relevantes para a tomada de decisão.

## Experimentos

### Conjuntos de Dados

Os conjuntos de dados utilizados neste trabalho foram coletados por meio de web scraping em plataformas de avaliação de hotéis como Google, Expedia, Booking e Tripadvisor, focando em hotéis de Foz do Iguaçu. As reviews foram separadas pela categoria aspecto juntamente com o sentimento (positivo ou negativo). O armazenamento foi realizado em banco de dados relacional.

| Hotel           | Total Reviews | Reviews Positivas | Reviews Negativas | Categorias                                            |
|-----------------|---------------|-------------------|-------------------|------------------------------------------------------|
| Bourbon         | 1254          | 1032              | 222               | Quarto, Localização, áreas comuns, Atendimento da equipe, Café da manhã |
| Continental     | 310           | 255               | 55                | Atendimento da equipe, Quarto                         |
| Foz Plaza       | 468           | 371               | 97                | Atendimento da equipe, Quarto, áreas comuns          |
| Nadai           | 812           | 607               | 205               | Atendimento da equipe, Quarto, áreas comuns, Café da manhã |
| Taroba          | 4316          | 3522              | 794               | Atendimento da equipe, Experiência, Café da manhã, Restaurante/Bar, Banheiro, Quarto, Localização, áreas comuns |
| Viale Cataratas | 930           | 656               | 274               | Quarto, áreas comuns, Experiência, Café da manhã, Atendimento da equipe, Restaurante/Bar |
| Viale Tower     | 1324          | 997               | 327               | Localização, Quarto, Café da manhã, Atendimento da equipe, áreas comuns, Experiência |

### Métodos de Quantificação Utilizados

A quantificação é a tarefa de estimar a distribuição relativa das classes em um conjunto de dados. Diferentemente da classificação, que rotula instâncias individuais, a quantificação prevê a prevalência das classes em amostras. Seguindo a taxonomia de Esuli et al. (2023), os algoritmos de quantificação utilizados foram divididos em três grupos:

1. Aggregative  
2. Aggregative Methods Based on Special-Purpose Learners  
3. Non-Aggregative  

| Grupo         | Subgrupo                  | Algoritmo                               | Referência                          |
|---------------|---------------------------|---------------------------------------|-----------------------------------|
| Aggregative   | Classify and Count        | CC (Classify and Count)                | Forman, 2005                      |
| Aggregative   | -                         | Expectation Maximization Quantifier   | Saerens et al., 2002              |
| Aggregative   | -                         | Friedman Method                       | Friedman                         |
| Aggregative   | -                         | Generalized Adjust Count              | Firat, 2008                      |
| Aggregative   | -                         | Probabilistic Classify and Count      | Bella et al., 2010                |
| Aggregative   | -                         | Nearest-Neighbor based Quantification | Barraquero et al., 2013           |
| Aggregative   | Threshold Methods         | Adjusted Classify and Count (ACC)     | Forman, 2008                     |
| Aggregative   | Threshold Methods         | Threshold MAX                         | Forman, 2005                     |
| Aggregative   | Threshold Methods         | Median Sweep                         | Forman, 2008                     |
| Aggregative   | Threshold Methods         | Probabilistic Adjusted Classify and Count | Bella et al., 2010                |
| Aggregative   | Mixture Models            | Distribution y-Similarity             | Maletzke et al., 2019            |
| Aggregative   | Mixture Models            | Synthetic Distribution y-Similarity   | Maletzke et al., 2021            |
| Aggregative   | Mixture Models            | Hellinger Distance Minimization       | Gonzáles-Castro et al., 2013     |
| Aggregative   | Mixture Models            | Sample Mean Matching                  | Hassan et al., 2013              |
| Aggregative   | Mixture Models            | Sample Ordinal Distance               | Maletzke et al., 2019            |
| Non-Aggregative | -                       | Hellinger Distance Minimization       | Gonzáles-Castro et al., 2013     |

### Bibliotecas Escolhidas para Quantificação

Comparação entre as bibliotecas Quapy e mlquantify em termos de implementações dos métodos e usabilidade:

| Biblioteca | Aggregative | Threshold Methods | Mixture Models | Non-Aggregative | Total Métodos | Gerenciamento Dinâmico de Classes | Documentação | Usabilidade Alta |
|------------|-------------|-------------------|----------------|-----------------|---------------|---------------------------------|--------------|------------------|
| Quapy      | 9           | 5                 | 3              | 2               | 19            | Não                             | Sim          | Não              |
| mlquantify | 7           | 7                 | 5              | 1               | 20            | Sim                             | Sim          | Sim              |

A biblioteca mlquantify foi escolhida para o desenvolvimento devido à sua versatilidade, suporte ao gerenciamento dinâmico de classes e interface amigável, similar ao padrão do scikit-learn.

### Composição dos Experimentos

Os experimentos foram conduzidos sobre aspectos que continham mais de 100 exemplos para garantir uma avaliação robusta, focando nos aspectos comuns a todos os hotéis:

- Atendimento da equipe
- Quarto
- Café da manhã
- Localização
- Áreas comuns

Utilizou-se o protocolo APP (Artificial Prevalence Protocol) para avaliação dos quantificadores, que consiste em várias repetições com prevalências artificialmente alteradas para medir robustez e precisão.

Para cada combinação de prevalências e tamanhos de amostras (mínimo de 25 instâncias até o total disponível), foram feitas 3 réplicas para confiabilidade dos resultados.

A métrica principal usada para avaliação foi o Erro Absoluto Médio (MAE).

### Referências para Métodos de Quantificação

Esuli, A., Fabris, A., Moreo, A., Sebastiani, F. (n.d.). Learning to Quantify. The Information Retrieval Series.

Barranquero, J., González, P., Dez, J., del Coz, J. J. (2013). On the study of nearest neighbor algorithms for prevalence estimation in binary problems. Pattern Recognition, 46(2), 472-482. https://doi.org/10.1016/j.patcog.2012.07.022

Bella, A., Ferri, C., Hernández-Orallo, J., Ramírez-Quintana, M. J. (2010). Quantification via probability estimators. Proceedings - IEEE International Conference on Data Mining (ICDM), 737-742. https://doi.org/10.1109/ICDM.2010.75

Firat, A. (2016). Unified Framework for Quantification. arXiv:1606.00868.

Forman, G. (2005). Counting Positives Accurately Despite Inaccurate Classification. Lecture Notes in Artificial Intelligence, Vol. 3720.

Forman, G. (2008). Quantifying counts and costs via classification. Data Mining and Knowledge Discovery, 17(2), 164-206. https://doi.org/10.1007/s10618-008-0097-y

Friedman, J. H. (n.d.). Class counts in future unlabeled samples: Detecting and dealing with concept drift.

González-Castro, V., Alaíz-Rodríguez, R., Alegre, E. (2013). Class distribution estimation based on the Hellinger distance. Information Sciences, 218, 146-164. https://doi.org/10.1016/j.ins.2012.05.028

Hassan, W., Maletzke, A., Batista, G. (2020). Accurately quantifying a billion instances per second. Proceedings - 2020 IEEE 7th International Conference on Data Science and Advanced Analytics (DSAA), 110. https://doi.org/10.1109/DSAA49011.2020.00012

Maletzke, A. G., et al. (2019). DyS a framework for mixture models in quantification. Proceedings of AAAI Conference on Artificial Intelligence, Palo Alto AAAI Press. https://doi.org/10.1609/aaai.v33i01.33014552

Maletzke, A., Reis D. D., Hassan, W., Batista, G. (2021). Accurately Quantifying under Score Variability. 2021 IEEE International Conference on Data Mining (ICDM), Auckland, New Zealand. https://doi.org/10.1109/ICDM51629.2021.00149

Pérez-Gállego, P., Castaño, A., Ramírez Quevedo, J., del Coz, J. (2019). Dynamic ensemble selection for quantification tasks. Information Fusion, 45, 1-15. https://doi.org/10.1016/j.inffus.2018.01.001

Pérez-Gállego, P., Quevedo, J. R., del Coz, J. J. (2017). Using ensembles for problems with characterizable changes in data distribution: A case study on quantification. Information Fusion, 34, 87-100. https://doi.org/10.1016/j.inffus.2016.07.001

Saerens, M., Latinne, P., Decaestecker, C. (2001). Adjusting the Outputs of a Classifier to New a Priori Probabilities: A Simple Procedure. Neural Computation, 14(1), 21-41.

Milli, L., Monreale, A., Rossetti, G., Giannotti, F., Pedreschi, D., Sebastiani, F. (2013). Quantification trees. 2013 IEEE 13th International Conference on Data Mining, 528-536.

Gao, W., Sebastiani, F. (2016). From classification to quantification in tweet sentiment analysis. Social Network Analysis and Mining, 6(1), 1-22.

Dietterich, T. G., Kong, E. B. (1995). Machine learning bias, statistical bias, and statistical variance of decision tree algorithms. Technical Report, Department of Computer Science, Oregon State University.

Qiu, G., Liu, B., Bu, J., Chen, C. (2011). Opinion word expansion and target extraction through double propagation. Computational Linguistics, 37(1), 9-27.

Sun, C., Huang, L., Qiu, X. (2019). Utilizing BERT for aspect-based sentiment analysis via constructing auxiliary sentence. arXiv preprint arXiv:1903.09588.

Saeidi, M., Bouchard, G., Liakata, M., Riedel, S. (2016). Sentihood: Targeted aspect-based sentiment analysis dataset for urban neighbourhoods. arXiv preprint arXiv:1610.03771.

Sanchez-Franco, M. J., Cepeda-Carrion, G., Roldan, J. L. (2019). Understanding relationship quality in hospitality services: A study based on text analytics and partial least squares. Internet Research, 29(3), 478-503.

Ministerio do Turismo. (2023, January 11). Turismo internacional: Conheça as principais portas de entrada de estrangeiros no Brasil. https://www.gov.br/turismo/pt-br/assuntos/noticias/turismo-internacional-conheca-as-principais-portas-de-entrada-de-estrangeiros-no-brasil

