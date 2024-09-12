from main import *
import matplotlib.ticker as mticker

df_nhl['Overtime'] = df_nhl['Status'].str.contains('OT', case=False, na=False)

# Overtime Wins
df_nhl['Overtime Win'] = df_nhl.apply(
    lambda row: row['Winning Team'] if 'OT' in row['Status'] else None, axis=1
)

# Overtime Losses
df_nhl['Overtime Loss'] = df_nhl.apply(
    lambda row: row['Losing Team'] if 'OT' in row['Status'] else None, axis=1
)

# Laskee määrän
overtime_wins = df_nhl['Overtime Win'].value_counts()
overtime_losses = df_nhl['Overtime Loss'].value_counts()

# DataFrame
overtime_data = pd.concat([overtime_wins, overtime_losses], axis=1).fillna(0)
overtime_data.columns = ['Overtime Wins', 'Overtime Losses']

# Sort (wins + losses)
overtime_data['Total Overtime Games'] = overtime_data['Overtime Wins'] + overtime_data['Overtime Losses']
overtime_data = overtime_data.sort_values(by='Total Overtime Games', ascending=False)

plt.figure(figsize=(12, 8))
ax = overtime_data[['Overtime Wins', 'Overtime Losses']].plot(kind='bar', stacked=True, color=['lightblue', 'salmon'], figsize=(14, 8))

# Plot kustomointi
plt.title('Overtime Wins (Blue) and Losses (Red) by Team')
plt.xlabel('Team')
plt.xticks(rotation=44, ha='right')

plt.ylabel('Count')
plt.legend(loc='upper right')
plt.tight_layout()

# Uutena testinä set_major_locator, jolla säädetään akselin (y) tickerien väliä
ax.yaxis.set_major_locator(mticker.MultipleLocator(2))

plt.show()
