"""
Using pandas, determine the following for the sales.csv data:

The total revenue for each product (quantity  x price_per_unit).
The total cost for each product (quantity  x cost_per_unit).
The profit for each product (total revenue - total cost).
Finally, find the most profitable product overall.
"""

# Basic example

import pandas as pd

# Load the CSV file
df = pd.read_csv("sales.csv")

# Step 1: Compute total revenue and total cost for each row
df["total_revenue"] = df["quantity"] * df["price_per_unit"]
df["total_cost"] = df["quantity"] * df["cost_per_unit"]

# Step 2: Compute profit for each row
df["profit"] = df["total_revenue"] - df["total_cost"]

# Step 3: Group by product and sum the totals
product_summary = (
    df.groupby("product")[["total_revenue", "total_cost", "profit"]]
    .sum()
    .reset_index()
)

# Step 4: Sort by profit descending to find the most profitable product
most_profitable = product_summary.sort_values(by="profit", ascending=False).head(1)

print("=== Product Profit Summary ===")
print(product_summary)
print("\n=== Most Profitable Product ===")
print(most_profitable)

# Be always aware of the iterative vs vectorized approach - 10-100x faster
# vectorized
df = pd.DataFrame({'a': [1, 2, 3, 4]})
df['b'] = df['a'] * 2

# iterative 
df['b'] = 0
for i, row in df.iterrows():
    df.at[i, 'b'] = row['a'] * 2 # type: ignore
