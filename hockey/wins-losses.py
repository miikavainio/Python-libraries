from main import *

# Wins and Losses by Team
plt.figure(figsize=(14, 10))
wins_losses = pd.concat([
    df_nhl['Winning Team'].value_counts(),
    df_nhl['Losing Team'].value_counts()
], axis=1).fillna(0)
wins_losses.columns = ['Wins', 'Losses']
wins_losses = wins_losses.sort_values(by='Wins', ascending=False)

wins_losses.plot(kind='bar', stacked=True, figsize=(14, 10))
plt.title('Wins and Losses by Team')
plt.xlabel('Team')
plt.xticks(rotation=45, ha = 'right')
plt.tight_layout()

plt.show()