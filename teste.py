import pandas as pd


df = pd.read_csv('quantification_results.csv')

df = df[df['QUANTIFIER'] != 'DySsyn']

df.to_csv('quantification_results.csv', index=False)