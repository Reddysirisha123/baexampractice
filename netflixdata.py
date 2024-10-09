import pandas as pd

# Load the dataset
file_path = '/mnt/data/Netflix Userbase.csv'
df = pd.read_csv(file_path)

# Display the first few rows of the dataset
print("First 5 rows of the dataset:")
print(df.head())

# Basic information about the dataset
print("\nDataset Information:")
print(df.info())

# Statistical summary of the dataset
print("\nStatistical Summary:")
print(df.describe())

# Checking for missing values
print("\nMissing Values in the Dataset:")
print(df.isnull().sum())

# Analyzing the distribution of a key column (e.g., 'Country', 'Subscription Type')
if 'Country' in df.columns:
    print("\nCountry-wise User Distribution:")
    print(df['Country'].value_counts())

if 'Subscription Type' in df.columns:
    print("\nSubscription Type Distribution:")
    print(df['Subscription Type'].value_counts())
