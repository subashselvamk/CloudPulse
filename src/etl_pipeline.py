import pandas as pd

# ==============================
# 1. Load raw data
# ==============================

input_file = "../data/raw/Online Retail.xlsx"

df = pd.read_excel(input_file)

print("Raw data loaded successfully!")
print("Total records:", len(df))


# ==============================
# 2. Remove duplicate records
# ==============================

df = df.drop_duplicates()

print("After removing duplicates:", len(df))


# ==============================
# 3. Create invalid-data rules
# ==============================

invalid_quantity = df["Quantity"] <= 0
invalid_price = df["UnitPrice"] <= 0
cancelled_invoice = df["InvoiceNo"].astype(str).str.startswith("C")


# ==============================
# 4. Separate invalid records
# ==============================

invalid_data = df[
    invalid_quantity |
    invalid_price |
    cancelled_invoice
]

valid_data = df[
    ~(
        invalid_quantity |
        invalid_price |
        cancelled_invoice
    )
].copy()


# ==============================
# 5. Clean valid data
# ==============================

# Remove rows without description
valid_data = valid_data.dropna(subset=["Description"])

# Calculate revenue
valid_data["Revenue"] = (
    valid_data["Quantity"] *
    valid_data["UnitPrice"]
)


# ==============================
# 6. Save processed data
# ==============================

valid_data.to_csv(
    "../data/processed/valid_orders.csv",
    index=False
)


# ==============================
# 7. Save invalid data
# ==============================

invalid_data.to_csv(
    "../data/quarantine/invalid_orders.csv",
    index=False
)


# ==============================
# 8. Print pipeline summary
# ==============================

print("\n========== ETL PIPELINE REPORT ==========")

print("Original records       :", len(df))
print("Valid records          :", len(valid_data))
print("Invalid records        :", len(invalid_data))

print(
    "Data Quality Score     :",
    round((len(valid_data) / len(df)) * 100, 2),
    "%"
)

print("\nProcessed file:")
print("../data/processed/valid_orders.csv")

print("\nQuarantine file:")
print("../data/quarantine/invalid_orders.csv")

print("=========================================")