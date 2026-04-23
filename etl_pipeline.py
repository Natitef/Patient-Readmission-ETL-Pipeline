import pandas as pd
import matplotlib.pyplot as plt
import os

# -------------Extract--------------------

raw_path = "data/Hospital_Readmissions.csv"

df = pd.read_csv(raw_path)


#  ----------------Transform---------------------

# Change column names to snake_case 
df = df.rename (columns={

    'Facility Name':'hospital_name',
    'Facility ID': 'facility_id',
    'State': 'state',
    'Measure Name': 'condition',
    'Number of Discharges': 'num_discharges',
    'Footnote': 'footnote',
    'Excess Readmission Ratio': 'excess_readmission_ratio',
    'Predicted Readmission Rate': 'predicted_rate',
    'Expected Readmission Rate': 'expected_rate',
    'Number of Readmissions': 'num_readmissions',
    'Start Date': 'start_date',
    'End Date': 'end_date'

})



# Check for missing values 


print("\nMissing values in each column:")

print(df.isnull().sum())


# Replace N/A string with actual nulls

# CSV has text N/A in some cells, not real null values

df = df.replace('N/A',pd.NA)

# Drop rows with missing values in critical columns

df = df.dropna(subset=['excess_readmission_ratio', 'predicted_rate', 'num_readmissions'])

# Drop rows with duplicates

df = df.drop_duplicates()

# Check the shape of the DataFrame after dropping rows with missing values
print("After dropping incomplete rows: ", df.shape)


# Convert numeric columns to appropriate data types

df['excess_readmission_ratio'] = pd.to_numeric(df['excess_readmission_ratio'], errors='coerce')
df['predicted_rate'] = pd.to_numeric(df['predicted_rate'], errors='coerce')
df['expected_rate'] = pd.to_numeric(df['expected_rate'], errors='coerce')
df['num_readmissions'] = pd.to_numeric(df['num_readmissions'], errors='coerce')
df['num_discharges'] = pd.to_numeric(df['num_discharges'], errors='coerce')

# Check data types after conversion
print("\n Data types after conversion: ",df.dtypes)


# Standardize text columns

df['hospital_name'] = df['hospital_name'].str.strip()
df['state'] = df['state'].str.strip().str.upper()
df['condition'] = df['condition'].str.strip()

print("\n Text columns standardized: ", df.head())


# --------- Load -----------------

# Save the clean data as a new CSV file

output_path = r"data\clean_csv\Hospital_Readmissions_Clean.csv"

df.to_csv(output_path, index=False)

