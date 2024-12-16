import pandas as pd

data = {
    "Date": ["2024-01-01", "2024-01-02", "2024-01-03", "2024-01-04", "2024-01-05"],
    "Product": ["Product A", "Product B", "Product C", "Product D", "Product A"],
    "Region": ["North", "East", "South", "West", "North"],
    "Sales": [1000, 800, 1200, None, 900],
    "Profit": [200, 150, 250, 300, None],
}
sales_data = pd.DataFrame(data)

print("First 5 rows of the dataset:")
print(sales_data.head())

print("\nDataset Info:")
print(sales_data.info())

print("\nMissing Values:")
print(sales_data.isnull().sum())

sales_data["Sales"] = sales_data["Sales"].fillna(sales_data["Sales"].mean())
sales_data["Profit"] = sales_data["Profit"].fillna(sales_data["Profit"].mean())

print("\nAfter cleaning missing values:")
print(sales_data)

sales_data["Date"] = pd.to_datetime(sales_data["Date"])

print("\nDataset with Date converted to datetime:")
print(sales_data)

print("\nSummary Statistics:")
print(sales_data.describe())
