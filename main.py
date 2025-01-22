import pandas as pd
import numpy as np

# Load the dataset from the CSV file in the same folder
df = pd.read_csv('iris.data', header=None)

# Add column names
df.columns = ["SepalLength", "SepalWidth", "PetalLength", "PetalWidth", "Species"]

# Data cleaning function
def clean_data(df):
    # Remove duplicates
    df = df.drop_duplicates()

    # Check for missing values and handle them
    if df.isnull().values.any():
        df = df.fillna(df.median(numeric_only=True))  # Fill missing numerical values with the median

    # Ensure correct data types
    for col in ["SepalLength", "SepalWidth", "PetalLength", "PetalWidth"]:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    # Handle any invalid rows (e.g., rows with NaN after conversion)
    df = df.dropna()

    # Reset the index
    df = df.reset_index(drop=True)

    return df

# Clean the dataset
cleaned_data = clean_data(df)

# Display cleaned dataset
print("Cleaned Dataset:")
print(cleaned_data)
