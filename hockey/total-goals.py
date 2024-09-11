from main import *

# Laskee maalit, vieraspeleistä sekä koti
visitor_goals = df_nhl.groupby('Visitor')['Visitor Score'].sum().sort_values(ascending=False)
home_goals = df_nhl.groupby('Home')['Home Score'].sum().sort_values(ascending=False)

# Laskee yhteen maalit
total_goals = visitor_goals.add(home_goals, fill_value=0).sort_values(ascending=False)

# Luo dataframen
total_goals_df = total_goals.reset_index()
total_goals_df.columns = ['Team', 'Total Goals']

# Seaborn barplotin luomiseksi
sns.barplot(x='Total Goals', y='Team', hue='Total Goals', data=total_goals_df, palette='light:blue', errorbar=None, dodge=False)

# Titlet, fonttikoot
plt.title('Total Goals per Team', fontsize=16)
plt.xlabel('Total Goals', fontsize=14)
plt.ylabel('Team', fontsize=14)

# xticks joka 15.   /  45asteen käännös
max_goals = total_goals.max()
plt.xticks(ticks=range(0, int(max_goals) + 15, 15))
plt.xticks(rotation=45)


plt.tight_layout()
plt.show()