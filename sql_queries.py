import pandas as pd
from pandasql import sqldf

# Load the clean CSV 
df = pd.read_csv(r"data\clean_csv\Hospital_Readmissions_Clean.csv")

pysql = lambda q: sqldf(q, globals())

print(" Clean data loaded")
print(f"Shape: {df.shape}")

# SQL Queries for analysis

# Query 1 - which condition has the highest average excess readmission ratio?

q1 = pysql("""
    SELECT condition, 
           AVG(excess_readmission_ratio) as avg_excess_ratio,
           count(*) AS total_hospitals
    FROM df
    GROUP BY condition
    ORDER BY avg_excess_ratio DESC
""")
print("\n Query 1 — Avg Readmission Ratio by Condition:")
print(q1)

# Query 2 - Which states have the worst average readmission ratio?

q2 = pysql(""" 
    SELECT state, 
           AVG(excess_readmission_ratio) as avg_excess_ratio
    FROM df
    GROUP BY state
    ORDER BY avg_excess_ratio DESC
    LIMIT 10
""")
print("\n Query 2 — Avg Readmission Ratio by State:")
print(q2)

# Query 3 - Which top 10 hospitals are the worst performers

q3 = pysql("""
    SELECT hospital_name,
           state,
           condition,
           excess_readmission_ratio
    FROM df
    WHERE excess_readmission_ratio > 1.0
    ORDER BY excess_readmission_ratio DESC
    LIMIT 10;
""")


# Query 4 — How many hospitals are above vs below expected rate?

q4 = pysql("""
    SELECT
        CASE 
            WHEN excess_readmission_ratio > 1.0 THEN 'Above Expected'
            WHEN excess_readmission_ratio < 1.0 THEN 'Below Expected'
            ELSE 'At Expected'
        END AS performance,
        COUNT(*) AS num_hospitals
    FROM df
    GROUP BY performance
""")
print("\n Query 4 — Hospital Performance Distribution:")
print(q4)