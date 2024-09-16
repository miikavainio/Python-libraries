from main import *

df_nhl['Total Goals'] = df_nhl['Visitor Score'] + df_nhl['Home Score']

df_nhl['Winning Team Score'] = df_nhl.apply(
    lambda row: row['Visitor Score'] if row['Visitor Score'] > row['Home Score'] else row['Home Score'], axis=1
)
df_nhl['Losing Team Score'] = df_nhl.apply(
    lambda row: row['Home Score'] if row['Visitor Score'] > row['Home Score'] else row['Visitor Score'], axis=1
)

# Correlation matrix.
correlation_matrix = df_nhl[['Winning Team Score', 'Losing Team Score', 'Total Goals']].corr()

# Plot of correlation
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Matrix of Winning, Losing, and Total Goals')
plt.show()
