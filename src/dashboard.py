import streamlit as st
import pandas as pd

# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="CloudPulse Analytics",
    page_icon="☁️",
    layout="wide"
)

# =========================================================
# LOAD DATA
# =========================================================

@st.cache_data
def load_data():
    file_path = "../data/processed/valid_orders.csv"

    df = pd.read_csv(file_path)

    # Convert date
    df["InvoiceDate"] = pd.to_datetime(
        df["InvoiceDate"],
        errors="coerce"
    )

    # Remove invalid dates
    df = df.dropna(subset=["InvoiceDate"])

    return df


df = load_data()

# =========================================================
# TITLE
# =========================================================

st.title("☁️ CloudPulse Analytics")

st.caption(
    "Cloud Data Quality & Retail Analytics Platform"
)

st.markdown(
    "Interactive analytics powered by Python, Pandas, "
    "AWS S3, Amazon Athena and SQL."
)

# =========================================================
# SIDEBAR FILTERS
# =========================================================

st.sidebar.header("🎛️ Filters")

# -------------------------
# Date filter
# -------------------------

min_date = df["InvoiceDate"].min().date()
max_date = df["InvoiceDate"].max().date()

date_range = st.sidebar.date_input(
    "Select Date Range",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date
)

# Handle single date selection
if isinstance(date_range, tuple) and len(date_range) == 2:

    start_date = pd.Timestamp(date_range[0])
    end_date = pd.Timestamp(date_range[1]) + pd.Timedelta(days=1)

else:

    start_date = pd.Timestamp(date_range)
    end_date = start_date + pd.Timedelta(days=1)


# -------------------------
# Country filter
# -------------------------

countries = sorted(
    df["Country"]
    .dropna()
    .unique()
    .tolist()
)

selected_countries = st.sidebar.multiselect(
    "Select Countries",
    countries,
    default=[]
)


# -------------------------
# Product search
# -------------------------

product_search = st.sidebar.text_input(
    "🔎 Search Product",
    placeholder="Example: HEART"
)


# =========================================================
# APPLY FILTERS
# =========================================================

filtered_df = df[
    (df["InvoiceDate"] >= start_date) &
    (df["InvoiceDate"] < end_date)
].copy()


# Country filter
if selected_countries:

    filtered_df = filtered_df[
        filtered_df["Country"].isin(
            selected_countries
        )
    ]


# Product filter
if product_search:

    filtered_df = filtered_df[
        filtered_df["Description"]
        .fillna("")
        .str.contains(
            product_search,
            case=False,
            na=False
        )
    ]


# =========================================================
# KPI CALCULATIONS
# =========================================================

total_revenue = filtered_df["Revenue"].sum()

total_orders = filtered_df["InvoiceNo"].nunique()

total_quantity = filtered_df["Quantity"].sum()

total_products = filtered_df["StockCode"].nunique()

average_order_value = (
    total_revenue / total_orders
    if total_orders > 0
    else 0
)


# =========================================================
# KPI CARDS
# =========================================================

st.subheader("📊 Key Performance Indicators")

col1, col2, col3, col4, col5 = st.columns(5)

with col1:

    st.metric(
        "💰 Revenue",
        f"£{total_revenue:,.2f}"
    )

with col2:

    st.metric(
        "🛒 Orders",
        f"{total_orders:,}"
    )

with col3:

    st.metric(
        "📦 Quantity Sold",
        f"{total_quantity:,}"
    )

with col4:

    st.metric(
        "🏷️ Products",
        f"{total_products:,}"
    )

with col5:

    st.metric(
        "💳 Avg Order Value",
        f"£{average_order_value:,.2f}"
    )


st.divider()


# =========================================================
# REVENUE TREND
# =========================================================

st.subheader("📈 Revenue Trend")

if not filtered_df.empty:

    daily_revenue = (
        filtered_df
        .set_index("InvoiceDate")
        .resample("D")["Revenue"]
        .sum()
    )

    st.line_chart(
        daily_revenue,
        use_container_width=True
    )

else:

    st.warning(
        "No data available for the selected filters."
    )


# =========================================================
# COUNTRY ANALYSIS
# =========================================================

col1, col2 = st.columns(2)


with col1:

    st.subheader("🌍 Revenue by Country")

    country_revenue = (
        filtered_df
        .groupby("Country")["Revenue"]
        .sum()
        .sort_values(
            ascending=False
        )
        .head(10)
    )

    st.bar_chart(
        country_revenue,
        use_container_width=True
    )


with col2:

    st.subheader("📦 Quantity by Country")

    country_quantity = (
        filtered_df
        .groupby("Country")["Quantity"]
        .sum()
        .sort_values(
            ascending=False
        )
        .head(10)
    )

    st.bar_chart(
        country_quantity,
        use_container_width=True
    )


# =========================================================
# TOP PRODUCTS
# =========================================================

st.divider()

st.subheader("🏆 Top 10 Products")

top_products = (
    filtered_df
    .groupby("Description")
    .agg(
        Revenue=("Revenue", "sum"),
        Quantity=("Quantity", "sum")
    )
    .sort_values(
        "Revenue",
        ascending=False
    )
    .head(10)
)

st.dataframe(
    top_products,
    use_container_width=True
)


# =========================================================
# DATA QUALITY
# =========================================================

st.divider()

st.subheader("🔍 Data Quality")

quality_col1, quality_col2, quality_col3, quality_col4 = st.columns(4)

with quality_col1:

    st.metric(
        "Raw Records",
        "541,909"
    )

with quality_col2:

    st.metric(
        "Duplicates Removed",
        "5,268"
    )

with quality_col3:

    st.metric(
        "Invalid Records",
        "11,763"
    )

with quality_col4:

    st.metric(
        "Quality Score",
        "97.81%"
    )


# =========================================================
# FILTERED DATA
# =========================================================

st.divider()

st.subheader("📋 Filtered Data")

st.write(
    f"Showing {len(filtered_df):,} records"
)

st.dataframe(
    filtered_df.head(500),
    use_container_width=True
)


# =========================================================
# DOWNLOAD
# =========================================================

csv_data = filtered_df.to_csv(
    index=False
)

st.download_button(
    label="⬇️ Download Filtered Data",
    data=csv_data,
    file_name="cloudpulse_filtered_data.csv",
    mime="text/csv"
)