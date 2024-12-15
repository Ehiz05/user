import pandas as pd

# Load the sales dataset (replace 'sales.csv' with the actual path to your dataset)
data = {
    "Date": ["2024-01-01", "2024-01-02", "2024-01-03", "2024-01-04", "2024-01-05"],
    "Product": ["Product A", "Product B", "Product C", "Product D", "Product A"],
    "Region": ["North", "East", "South", "West", "North"],
    "Sales": [1000, 800, 1200, None, 900],
    "Profit": [200, 150, 250, 300, None],
}
sales_data = pd.DataFrame(data)

# Display the first few rows
print("First 5 rows of the dataset:")
print(sales_data.head())

# Explore the structure of the dataset
print("\nDataset Info:")
print(sales_data.info())

# Check for missing values
print("\nMissing Values:")
print(sales_data.isnull().sum())

# Clean the dataset
# Fill missing Sales and Profit with their column means
sales_data["Sales"] = sales_data["Sales"].fillna(sales_data["Sales"].mean())
sales_data["Profit"] = sales_data["Profit"].fillna(sales_data["Profit"].mean())

print("\nAfter cleaning missing values:")
print(sales_data)

# Convert 'Date' to datetime
sales_data["Date"] = pd.to_datetime(sales_data["Date"])

print("\nDataset with Date converted to datetime:")
print(sales_data)

# Display summary statistics
print("\nSummary Statistics:")
print(sales_data.describe())
