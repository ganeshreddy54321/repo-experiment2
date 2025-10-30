# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = r"C:\python\SYB67_123_202411_Total Imports Exports and Balance of Trade (2).csv"
df = pd.read_csv(file_path)

# --- Clean the Data ---
# Skip first info row
df_clean = df.iloc[1:].copy()

# Rename columns for easier handling
df_clean = df_clean.rename(columns={
    'Unnamed: 2': 'Year',
    'Unnamed: 3': 'Series',
    'Unnamed: 6': 'Value'
})

# Keep only necessary columns
df_clean = df_clean[['Year', 'Series', 'Value']]

# Drop rows with missing essential data
df_clean = df_clean.dropna()

# Convert 'Year' to int and 'Value' to float (remove commas)
df_clean['Year'] = df_clean['Year'].astype(int)
df_clean['Value'] = df_clean['Value'].str.replace(',', '').astype(float)

# --- Plotting ---

# Set style for all plots
sns.set(style="whitegrid")

# 1. Line Graph with Data Points
plt.figure(figsize=(10, 6))
for series_name in df_clean['Series'].unique():
    subset = df_clean[df_clean['Series'] == series_name]
    plt.plot(subset['Year'], subset['Value'], marker='o', label=series_name)

plt.title('Total Imports, Exports, and Balance Over Years')
plt.xlabel('Year')
plt.ylabel('Value (Millions of US Dollars)')
plt.legend()
plt.grid(True)
plt.show()

# 2. Histogram
plt.figure(figsize=(10, 6))
sns.histplot(df_clean['Value'], bins=15, kde=True, color='orange')
plt.title('Distribution of Trade Values')
plt.xlabel('Value (Millions of US Dollars)')
plt.ylabel('Frequency')
plt.show()

# 3. Horizontal Bar Chart
plt.figure(figsize=(10, 6))
series_sum = df_clean.groupby('Series')['Value'].sum().sort_values()
series_sum.plot(kind='barh', color='skyblue')
plt.title('Total Value by Series')
plt.xlabel('Total Value (Millions of US Dollars)')
plt.ylabel('Series')
plt.show()

# 4. Scatter Plot
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df_clean, x='Year', y='Value', hue='Series', s=100, palette='deep')
plt.title('Scatter Plot of Trade Values Over Years')
plt.xlabel('Year')
plt.ylabel('Value (Millions of US Dollars)')
plt.legend()
plt.show()

# 5. Regular Bar Chart
plt.figure(figsize=(10, 6))
sns.barplot(data=df_clean, x='Year', y='Value', hue='Series')
plt.title('Yearly Comparison of Imports, Exports, and Balance')
plt.xlabel('Year')
plt.ylabel('Value (Millions of US Dollars)')
plt.legend()
plt.show()
