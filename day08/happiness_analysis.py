import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\ronyh\OneDrive\Desktop\python_course\python-course-assignments\data\2019.csv")

#print(df.head())
#print(df.info())
#print(df.describe())

latest_year = df["Year"].max()
top10 = df[df["Year"] == latest_year].sort_values(
    by="Life Ladder", ascending=False
).head(10)

plt.barh(top10["Country"], top10["Life Ladder"])
plt.title(f"Top 10 Happiest Countries ({latest_year})")
plt.xlabel("Happiness Score")
plt.gca().invert_yaxis()
plt.show()
