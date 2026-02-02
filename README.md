Análise de Churn de Clientes – Telco Customer Churn

Este projeto tem como objetivo analisar o **churn de clientes** (cancelamento de serviços) em uma empresa de telecomunicações, identificando padrões e fatores que influenciam a saída dos clientes.



 Objetivos da Análise

- Calcular a **taxa de churn**
- Identificar perfis de clientes com maior propensão ao churn
- Analisar churn por:
  - Tipo de contrato
  - Método de pagamento
  - Serviço de internet
  - Gênero
  - Tempo de permanência (tenure)
- Criar um **dashboard interativo no Power BI**

---

Base de Dados

- **Dataset:** Telco Customer Churn  
- **Origem:** Kaggle (dataset público)
- **Formato:** CSV

O dataset contém informações demográficas, contratuais e de uso dos clientes, além da variável alvo **Churn**.

---

 Ferramentas Utilizadas

- **Python (Pandas)**  
  - Limpeza e preparação dos dados  
  - Criação de variáveis auxiliares (ex: `Churn_Num`)

- **Power BI**  
  - Modelagem de dados  
  - Medidas DAX  
  - Visualizações e dashboard interativo

---

Etapas do Projeto

###  Limpeza de Dados (Pandas)
- Tratamento de valores ausentes
- Conversão de tipos de dados
- Criação da variável numérica de churn:
  - `Churn_Num` (1 = Churn, 0 = Não churn)



### Modelagem no Power BI
- Criação de medidas DAX:
  - Taxa de Churn
- Criação de colunas traduzidas:
  - `Contract_PT`
  - `PaymentMethod_PT`
  - `InternetService_PT`
  - `Genero_PT`

###  Dashboard
- Gráficos de churn por perfil do cliente
- Filtros interativos


---

##  Principais Visualizações

- Taxa geral de churn
- Churn por tipo de contrato
- Churn por método de pagamento
- Churn por serviço de internet
- Churn por gênero
- Churn por tempo de permanência (tenure)

## Insights

- Churn bem mais alto em contratos mensais do que os anuais e bienais. 
- Clientes que pagam com cheque eletrônico cancelam mais o serviço, averiguar quais as causas (Dificuldade no pagamento? Taxas que encarecem esse método? Outro fator do perfil desses clientes?)
- Gênero do cliente não altera a chance de cancelar o serviço
- Parceiros com bem menos taxas de abandono que não parceiros
- Clientes que incluem Internet no plano tem mais chances de abandonarem os serviços, principalmente os de fibra optica. Sinal de que o serviço apresenta grandes problemas(Taxa de banda? Instabilidade? Dificuldade de manutenção e/ou infraestrutura?)
- Clientes que assinaram o serviço há menos de um ano com mais taxas de abandono do que os estão a mais de um ano. Maiores benefícios os descontos a esse grupo durante esse período podem ser recomendações apropriadas