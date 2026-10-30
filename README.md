
# ☁️ CloudPulse — AWS Cloud Data Pipeline & Analytics

An end-to-end cloud data engineering project that processes retail transaction data using Python, Pandas, Amazon S3, Amazon Athena, SQL, and Streamlit.

CloudPulse demonstrates how raw data can be cleaned, validated, stored in the cloud, queried for insights, and presented through an interactive analytics dashboard.

## 🚀 Project Overview

The project uses an ETL (Extract, Transform, Load) workflow to transform raw retail transaction data into structured datasets suitable for analysis.

### Key Features

- **Data Inspection:** Examines the structure and quality of raw retail data.
- **Data Cleaning:** Removes duplicate records and validates transaction data using Python and Pandas.
- **Data Quality Checks:** Separates valid and invalid records for further analysis.
- **Cloud Storage:** Uses Amazon S3 to organize raw and processed datasets.
- **SQL Analytics:** Uses Amazon Athena to query data stored in S3.
- **Interactive Dashboard:** Uses Streamlit to present analytical results and visualizations.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | ETL and data processing |
| Pandas | Data cleaning and transformation |
| Amazon S3 | Cloud object storage |
| Amazon Athena | SQL-based analytics |
| SQL | Data querying and analysis |
| Streamlit | Interactive dashboard |
| Git & GitHub | Version control and project management |

## 🏗️ Project Architecture

```text
Raw Retail Dataset
        |
        v
Python + Pandas
Data Inspection & ETL
        |
        v
Data Validation
   /          \
  v            v
Valid Data   Invalid Data
   |            |
   v            v
Amazon S3    Quarantine Storage
   |
   v
Amazon Athena
SQL Analytics
   |
   v
Streamlit Dashboard
```

*Note: This diagram represents the intended workflow. Adjust the components to match your actual implementation.*

## 📊 Data Processing Results

The following results were obtained during a previous ETL run:

| Metric | Result |
|---|---:|
| Original records | 541,909 |
| Records after duplicate removal | 536,641 |
| Valid records | 524,878 |
| Invalid records | 11,763 |
| Data quality rate | 97.81% |

These results demonstrate the data cleaning and validation stages of the pipeline.

## 🔍 Analytics

Amazon Athena and SQL can be used to explore questions such as:

- What is the total revenue?
- Which countries generate the highest revenue?
- Which products perform best?
- How do sales vary across dates?
- What patterns can be identified in the transaction data?

## 📁 Project Structure

```text
CloudPulse/
├── src/
│   ├── inspect_data.py
│   └── etl_pipeline.py
├── data/
│   └── raw/
├── README.md
└── requirements.txt
```

*Update this structure to match the files and folders actually present in your GitHub repository.*

## ▶️ Getting Started

### 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd CloudPulse
```

Replace the placeholder with your actual repository URL.

### 2. Install dependencies

```bash
pip install pandas openpyxl streamlit
```

Install any additional packages required by your project.

### 3. Prepare the dataset

Place the input dataset in the appropriate local data directory, following the paths configured in your Python scripts.

### 4. Run data inspection

```bash
python src/inspect_data.py
```

### 5. Run the ETL pipeline

```bash
python src/etl_pipeline.py
```

Review the generated valid and invalid datasets.

### 6. Run the dashboard

If your Streamlit dashboard is implemented in `app.py`, run:

```bash
streamlit run app.py
```

Update the filename if your dashboard uses a different entry point.

## 🔐 AWS Configuration

The original workflow uses Amazon S3 for storage and Amazon Athena for querying data.

To reproduce the cloud workflow:

1. Configure AWS credentials securely using an approved AWS authentication method.
2. Create or select an S3 bucket.
3. Upload the required datasets.
4. Configure Athena to query the stored data.
5. Configure the dashboard to use the appropriate processed data and query results.

**Cost note:** AWS services may incur charges. The cloud resources used during development may be deleted when they are no longer needed.

Never commit AWS access keys, secret keys, private credentials, or sensitive datasets to GitHub.

## 🎯 Skills Demonstrated

- ETL pipeline development
- Data cleaning and validation
- Python-based data engineering
- Cloud object storage
- SQL analytics
- Data quality assessment
- Interactive data visualization
- Version control with Git and GitHub

## 👨‍💻 Author

**Subash Selvam K.**

B.Tech — Computer Science and Business Systems

GitHub: [subashselvamk](https://github.com/subashselvamk)

LinkedIn: [Subash Selvam K.](https://www.linkedin.com/in/subash-selvam-k-a3a917290/)

---

⭐ If you find this project interesting, feel free to explore the repository and share your feedback.
