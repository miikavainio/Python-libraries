from main import *
import matplotlib.ticker as mticker

df_nhl['Overtime or Shootout'] = df_nhl['Status'].str.contains('OT|SO', case=False, na=False)

# Wins for overtime or shootout games
df_nhl['Overtime Win'] = df_nhl.apply(
    lambda row: row['Winning Team'] if 'OT' in row['Status'] or 'SO' in row['Status'] else None, axis=1
)

# Losses for overtime or shootout games
df_nhl['Overtime Loss'] = df_nhl.apply(
    lambda row: row['Losing Team'] if 'OT' in row['Status'] or 'SO' in row['Status'] else None, axis=1
)

# Calculate the counts of overtime and shootout wins and losses by team
overtime_wins = df_nhl['Overtime Win'].value_counts()
overtime_losses = df_nhl['Overtime Loss'].value_counts()

# Combine the wins and losses into a single DataFrame
overtime_data = pd.concat([overtime_wins, overtime_losses], axis=1).fillna(0)
overtime_data.columns = ['Overtime Wins', 'Overtime Losses']

# Add a column for total overtime and shootout games (wins + losses)
overtime_data['Total Overtime Games'] = overtime_data['Overtime Wins'] + overtime_data['Overtime Losses']

# Sort by total overtime and shootout games
overtime_data = overtime_data.sort_values(by='Total Overtime Games', ascending=False)

# Plot stacked bar chart
plt.figure(figsize=(12, 8))
ax = overtime_data[['Overtime Wins', 'Overtime Losses']].plot(kind='bar', stacked=True, color=['lightblue', 'salmon'], figsize=(14, 8))

# Customize the plot
plt.title('Overtime and Shootout Wins (Blue) and Losses (Red) by Team')
plt.xlabel('Team')
plt.ylabel('')
plt.xticks(rotation=44, ha='right')
plt.legend(loc='upper right')
plt.tight_layout()

ax.yaxis.set_major_locator(mticker.MultipleLocator(1))

plt.grid(True, which='both', axis='y', linestyle='--', linewidth=0.3, color='gray')

plt.show()
