
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("customer_churn.csv")

# Display first five rows
print("First Five Rows:")
print(df.head())

# Display dataset information
print("\nDataset Information:")
print(df.info())

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Handle missing values
for col in df.select_dtypes(include=np.number).columns:
    df[col] = df[col].fillna(df[col].median())

for col in df.select_dtypes(include="object").columns:
    df[col] = df[col].fillna(df[col].mode()[0])

# Remove duplicate records
df = df.drop_duplicates()

# Display cleaned data
print("\nCleaned Dataset:")
print(df.head())

# Generate summary statistics
print("\nSummary Statistics:")
print(df.describe())

# Churn count
print("\nCustomer Churn Count:")
print(df["Churn"].value_counts())

# Average monthly charges
print("\nAverage Monthly Charges:")
print(df["MonthlyCharges"].mean())

# Visualization 1: Churn Count
sns.countplot(x="Churn", data=df)
plt.title("Customer Churn Count")
plt.show()

# Visualization 2: Monthly Charges
sns.histplot(df["MonthlyCharges"], kde=True)
plt.title("Monthly Charges Distribution")
plt.show()

# Visualization 3: Churn by Contract
sns.countplot(x="Contract", hue="Churn", data=df)
plt.title("Churn by Contract Type")
plt.xticks(rotation=30)
plt.show()

# Visualization 4: Correlation Heatmap
numeric_df = df.select_dtypes(include=np.number)
sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()
