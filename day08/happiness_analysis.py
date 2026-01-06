import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

import pandas as pd
from pathlib import Path

# Path to the directory of this script
base_dir = Path(__file__).parent

# Path to the CSV file (same folder)
data_path = base_dir / "2019.csv"

df = pd.read_csv(data_path)

print(df.head())



print(df.head())
print(df.info())
print(df.describe())
print(df.columns)

#Happiness score distribution
top10 = df.sort_values(by="Score", ascending=False).head(10)

plt.figure(figsize=(10, 6))
bars = plt.bar(top10["Country or region"], top10["Score"], color='lightblue')

plt.title("Top 10 Happiest Countries in 2019")
plt.xlabel("Country")
plt.ylabel("Happiness Score")
plt.xticks(rotation=45, ha="right")

for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        height,
        f"{height:.2f}",
        ha="center",
        va="bottom"
    )

plt.tight_layout()
plt.show()

#GDP and happiness
df_corr = df[['GDP per capita', 'Score']].dropna()

x = df_corr['GDP per capita']
y = df_corr['Score']

correlation = np.corrcoef(x, y)[0, 1]
print("Correlation between GDP and Happiness:", correlation)


plt.scatter(x, y, alpha=0.4, color='lightpink')
plt.xlabel("GDP per capita")
plt.ylabel("Happiness Score")
plt.title("GDP vs Happiness")
plt.show()

#Hit map
features = [
    "Score",
    "GDP per capita",
    "Social support",
    "Healthy life expectancy",
    "Freedom to make life choices",
    "Generosity",
    "Perceptions of corruption"
]

df_corr = df[features].dropna()

corr = df_corr.corr()

plt.figure(figsize=(8, 6))
plt.imshow(corr, cmap='coolwarm', vmin=-1, vmax=1)
plt.colorbar()
plt.xticks(range(len(features)), features, rotation=90)
plt.yticks(range(len(features)), features)
plt.title("Correlation Matrix")
plt.tight_layout()
plt.show()

#Comparison between Europe and Asia
europe_countries = ['Germany', 'France', 'Italy', 'Spain', 'Norway', 'Sweden']  
asia_countries = ['China', 'India', 'Japan', 'South Korea', 'Thailand'] 

df['Region'] = df['Country or region'].apply(
    lambda x: 'Europe' if x in europe_countries else ('Asia' if x in asia_countries else 'Other')
)

df_regions = df[df['Region'].isin(['Europe', 'Asia'])]

plt.figure(figsize=(8, 6))
sns.boxplot(x='Region', y='Score', data=df_regions, color='lightgreen')
plt.title('Happiness Score: Europe vs Asia')
plt.ylabel('Happiness Score')
plt.show()


# clustering analysis
features = ['Score', 'GDP per capita', 'Social support', 'Healthy life expectancy',
            'Freedom to make life choices', 'Generosity', 'Perceptions of corruption']

df_cluster = df[features].dropna()


scaler = StandardScaler()
X_scaled = scaler.fit_transform(df_cluster)

kmeans = KMeans(n_clusters=3, random_state=42)
clusters = kmeans.fit_predict(X_scaled)

df_cluster['Cluster'] = clusters

plt.figure(figsize=(8, 6))
sns.scatterplot(x='GDP per capita', y='Score', hue='Cluster', palette='Set1', data=df_cluster)
plt.title('Clustering of Countries by Happiness')
plt.show()

