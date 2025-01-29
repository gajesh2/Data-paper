import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv('House_Data.csv')

# Display basic information about the dataset
print("Dataset Information:\n")
print(data.info())

# Checking for missing values
print("\nMissing Values:\n")
print(data.isnull().sum())

# Handling missing values (dropping rows with missing values for simplicity)
data_cleaned = data.dropna()

# Checking for duplicate records
print("\nDuplicate Records:", data_cleaned.duplicated().sum())

# Removing duplicate records
data_cleaned = data_cleaned.drop_duplicates()

# Detecting outliers using boxplots
numeric_columns = data_cleaned.select_dtypes(include=[np.number]).columns

plt.figure(figsize=(10, 6))
for col in numeric_columns:
    plt.figure()
    sns.boxplot(x=data_cleaned[col])
    plt.title(f'Boxplot of {col}')
    plt.show()

# Handling outliers (removing values beyond 1.5*IQR as an example)
def remove_outliers(df, col):
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return df[(df[col] >= lower_bound) & (df[col] <= upper_bound)]

for col in numeric_columns:
    data_cleaned = remove_outliers(data_cleaned, col)

# Save the cleaned dataset
data_cleaned.to_csv('/mnt/data/House_Data_Cleaned.csv', index=False)

print("\nData cleaning completed. Cleaned file saved as 'House_Data_Cleaned.csv'.")
