import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# CSV data
df_nhl = pd.read_csv('nhl-202324-asplayed.csv')

# print(df_nhl.head(5))

# Datetime muutos selkeämmäksi
df_nhl['Date'] = pd.to_datetime(df_nhl['Date'], format='%Y-%m-%d')

# print(df_nhl['Date'].head(5))

# Täsmennys, koska kaksi 'Score' osiota
df_nhl['Score'] = df_nhl['Score'].astype(str)
df_nhl['Score.1'] = df_nhl['Score.1'].astype(str)

# print(df_nhl['Score'].head(10))