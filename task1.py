import pandas as pd
import matplotlib.pyplot as plt

# Read the dataset
df = pd.read_csv("geo_population.csv")


# Bar Chart: Top 10 Countries

top10 = df.sort_values(by="Population", ascending=False).head(10)

plt.figure(figsize=(12, 6))
plt.bar(top10["Country"], top10["Population"])
plt.title("Top 10 Most Populous Countries")
plt.xlabel("Country")
plt.ylabel("Population")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("OUTPUT/bar_chart.png")
plt.show()


# Histogram: Population Distribution

plt.figure(figsize=(10, 6))
plt.hist(df["Population"], bins=20, edgecolor="black")
plt.title("Distribution of Country Populations")
plt.xlabel("Population")
plt.ylabel("Number of Countries")
plt.tight_layout()
plt.savefig("OUTPUT/histogram.png")
plt.show()