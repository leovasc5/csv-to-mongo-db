import pandas as pd

df = pd.read_csv("assets/base_jogadores.csv", sep=";", low_memory=False)
print(df.head())