import pandas as pd

# Load data
df = pd.read_csv("books.csv")

# Remove extra spaces
df = df.apply(lambda col: col.str.strip() if col.dtype == "object" else col)

# Remove duplicate books using UPC
df = df.drop_duplicates(subset="upc")

# Fill missing descriptions
df["description"] = df["description"].fillna("No Description")

# Convert price (£51.77 -> 51.77)
df["price"] = df["price"].str.replace("£", "", regex=False).astype(float)

# Convert ratings to numbers
rating_map = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}
df["rating"] = df["rating"].map(rating_map)

# Extract stock count
df["stock"] = df["availability"].str.extract(r'(\d+)').fillna(0).astype(int)

# New Features
df["description_word_count"] = df["description"].apply(lambda x: len(str(x).split()))

df["price_band"] = pd.cut(
    df["price"],
    bins=[0, 20, 40, 60, 100],
    labels=["Cheap", "Medium", "Expensive", "Premium"]
)

df["value_score"] = df["rating"] / df["price"]

# Save cleaned data
df.to_csv("books_cleaned.csv", index=False)

print(df.head())

print("\nTotal Records:", len(df))
print("Missing Values:\n", df.isnull().sum())
print("Duplicate UPC:", df["upc"].duplicated().sum())