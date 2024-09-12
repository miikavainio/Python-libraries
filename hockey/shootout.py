from main import *

df_nhl['Shootout'] = df_nhl['Status'].str.contains('SO', case=False, na=False)


plt.figure(figsize=(12, 8))
shootout_games_over_time = df_nhl.groupby('Date')['Shootout'].sum()
shootout_games_over_time.plot(figsize=(12, 8), color='blue')
plt.title('Shootout Games Over Time')
plt.xlabel('Date')
plt.ylabel('Number of Shootout Games')
plt.show()
