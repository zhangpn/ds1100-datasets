import pandas as pd

df = pd.read_csv('raw_mock_data.csv')

features = pd.get_dummies(old['What was the most important consideration for you in choosing this product?'])

df = pd.concat([df, features],axis=1)

for c in df.columns[4:]:
  df[c] = df[c].astype(str).replace({'0': np.nan, '1': c})

df.to_csv('mock_data.csv')
