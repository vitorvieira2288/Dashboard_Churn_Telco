import pandas as pd


df = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")

print(df.head())
print(df.info())


df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')

df['TotalCharges'].fillna(0, inplace=True)


df['Churn_Num'] = df['Churn'].map({'Yes': 1, 'No': 0})

print("\nValores nulos por coluna:")
print(df.isnull().sum())


print("\nEstatísticas descritivas:")
print(df.describe())


df.to_csv("telco_churn_limpo.csv", index=False)

print("\nArquivo 'telco_churn_limpo.csv' criado com sucesso.")
