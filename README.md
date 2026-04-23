# Patient Readmission ETL Pipeline & Analytics Dashboard

## Project Overview
Hospital readmissions are a major financial and operational challenge 
in healthcare. Medicare penalizes hospitals that readmit too many 
patients within 30 days of discharge through the Hospital Readmissions 
Reduction Program (HRRP). This project builds an end-to-end ETL pipeline 
to clean and transform real CMS government data, performs SQL analysis 
to uncover readmission trends, and delivers an interactive Tableau 
dashboard for healthcare stakeholders.

## Tools Used
- **Python** — ETL pipeline development
- **Pandas** — Data ingestion, cleaning, and transformation
- **SQL (pandasql)** — Analytical queries and trend analysis
- **Tableau Public** — Interactive dashboard and visualizations

## Project Structure
- `etl_pipeline.py` — Full ETL pipeline: extracts raw CMS data, 
  validates and cleans it, and loads a clean CSV for downstream analysis
- `sql_queries.py` — SQL queries analyzing readmission trends by 
  condition, state, and hospital performance
- `Hospital_Readmissions_Clean.csv` — Clean output dataset 
  produced by the pipeline

## ETL Pipeline Steps

### 1. Extract
- Loaded raw CMS Hospital Readmissions Reduction Program dataset
- Dataset contained 12 fields across thousands of hospital records

### 2. Transform
- Renamed all columns to clean snake_case format
- Identified and converted text "N/A" values to real null values
- Dropped rows missing critical readmission metrics
- Removed duplicate records
- Converted numeric columns from text to correct data types
- Standardized text columns by stripping whitespace and 
  normalizing casing

### 3. Load
- Exported clean dataset to CSV for downstream SQL analysis 
  and Tableau visualization
- Final clean dataset: 11,720 rows across 12 columns

## SQL Analysis
Queries written to answer real business questions:

- Which conditions have the highest average excess readmission ratio?
- Which states have the worst average readmission performance?
- Which hospitals are the worst performers with ratios above 1.0?
- How many hospitals are performing above vs below expected rates?

## Key Findings
- Hip & Knee Replacement had the highest excess readmission 
  ratio of all conditions
- Massachusetts, New Jersey, and Florida were the worst 
  performing states
- Approximately 48% of hospitals performed above expected 
  readmission rates, triggering potential Medicare penalties
- Only 7 hospitals performed at exactly the expected rate

## Understanding the Excess Readmission Ratio
The excess readmission ratio is calculated as:

Predicted Readmission Rate ÷ Expected Readmission Rate

- Above 1.0 = hospital is readmitting more patients than expected
- Below 1.0 = hospital is performing better than expected
- Exactly 1.0 = performing exactly as predicted

CMS adjusts expectations based on patient complexity so hospitals 
treating sicker patients are compared fairly.

## Dashboard
Built an interactive Tableau dashboard with 3 visualizations:
- Map of average excess readmission ratio by state
- Bar chart of readmission rates by condition
- Hospital performance distribution showing above vs below expected

**Tableau Dashboard**
https://public.tableau.com/shared/CMHGSMTN3
