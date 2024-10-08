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

# Scattered plot to visualize more
plt.figure(figsize=(10, 6))
sns.scatterplot(x=df_nhl['Winning Team Score'], y=df_nhl['Total Goals'])
plt.title('Winning Team Score vs Total Goals')
plt.xlabel('Winning Team Score')
plt.ylabel('Total Goals')
plt.show()

# Scattered plot of losses
plt.figure(figsize=(10, 6))
sns.scatterplot(x=df_nhl['Losing Team Score'], y=df_nhl['Total Goals'], color='red')
plt.title('Losing Team Score vs Total Goals')
plt.xlabel('Losing Team Score')
plt.ylabel('Total Goals')
plt.show()

# Print out the correlation ( 4 decimals )
print(f"Correlation between Winning Team Score and Total Goals: {correlation_matrix.loc['Winning Team Score', 'Total Goals']:.4f}")
print(f"Correlation between Losing Team Score and Total Goals: {correlation_matrix.loc['Losing Team Score', 'Total Goals']:.4f}")
