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

# Visitor ja Home tulokset
df_nhl['Visitor Score'] = df_nhl['Score'].str.extract(r'(\d+)').astype(float)
df_nhl['Home Score'] = df_nhl['Score.1'].str.extract(r'(\d+)').astype(float)

# print(df_nhl['Visitor Score'].head(10))

def test_for_visitor_score_and_score():
    # Vertailee Visitor scorea sekä Scorea float arvoina
    mismatches = df_nhl[df_nhl['Visitor Score'] != df_nhl['Score'].str.extract(r'(\d+)').astype(float)[0]]
    
    if mismatches.empty:
        print("Test passed")
    else:
        print(f"Test failed")
        print(mismatches[['Score', 'Visitor Score']])

# Testi
# test_for_visitor_score_and_score()

# Määrittelee voittajan ja häviäjän tulosten perusteella
df_nhl['Winning Team'] = df_nhl.apply(
    lambda row: row['Visitor'] if row['Visitor Score'] > row['Home Score'] else row['Home'], axis=1
)
df_nhl['Losing Team'] = df_nhl.apply(
    lambda row: row['Home'] if row['Visitor Score'] > row['Home Score'] else row['Visitor'], axis=1
)