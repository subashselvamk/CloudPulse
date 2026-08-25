import pandas as pd

# Load dataset
file_path = "../data/Online Retail.xlsx"
df = pd.read_excel(file_path)

print("========== DATA QUALITY REPORT ==========")

# 1. Total records
print("\nTotal Records:", len(df))

# 2. Total columns
print("Total Columns:", len(df.columns))

# 3. Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# 4. Duplicate records
print("\nDuplicate Records:", df.duplicated().sum())

# 5. Invalid quantity
print("\nInvalid Quantity:", (df["Quantity"] <= 0).sum())

# 6. Invalid price
print("Invalid Unit Price:", (df["UnitPrice"] <= 0).sum())

# 7. Cancelled transactions
print("Cancelled Transactions:",
      df["InvoiceNo"].astype(str).str.startswith("C").sum())

print("\n==========================================")