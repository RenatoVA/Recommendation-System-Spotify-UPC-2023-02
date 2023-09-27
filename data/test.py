import pandas as pd
path='data/processed_tracks.csv'
df=pd.read_csv(path,index_col=False)
print(df.head())
df = df.drop(df.columns[0], axis=1)
print(df.head())
df.to_csv('processed_tracks2.csv', index=False)   