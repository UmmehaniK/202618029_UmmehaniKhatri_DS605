import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Load cleaned data
df = pd.read_csv("books_cleaned.csv")

# Graph 1: Price Distribution
plt.figure(figsize=(8,5))
plt.hist(df["price"], bins=10)
plt.title("Price Distribution")
plt.xlabel("Price")
plt.ylabel("Number of Books")
plt.savefig("price_distribution.png")
plt.close()

# Graph 2: Rating Distribution
plt.figure(figsize=(8,5))
df["rating"].value_counts().sort_index().plot(kind="bar")
plt.title("Rating Distribution")
plt.xlabel("Rating")
plt.ylabel("Count")
plt.savefig("rating_distribution.png")
plt.close()

# Graph 3: Average Price by Category
plt.figure(figsize=(10,6))
df.groupby("category")["price"].mean().sort_values().plot(kind="bar")
plt.title("Average Price by Category")
plt.ylabel("Average Price")
plt.tight_layout()
plt.savefig("average_price_category.png")
plt.close()

# Graph 4: Price vs Rating
plt.figure(figsize=(8,5))
plt.scatter(df["price"], df["rating"])
plt.title("Price vs Rating")
plt.xlabel("Price")
plt.ylabel("Rating")
plt.savefig("price_vs_rating.png")
plt.close()

# Word Cloud
text = " ".join(df["description"].astype(str))

wc = WordCloud(width=1200, height=600, background_color="white").generate(text)

plt.figure(figsize=(12,6))
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.savefig("wordcloud.png")
plt.close()

print("All graphs created successfully!")