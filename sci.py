# here I will observe the data, I will understand the data
import matplotlib as plt
import numpy as np
import pandas as pd

# Load the CSV data into a DataFrame
df = pd.read_csv('Guess.csv')

# Step 2: Identify the duplicate numbers in a specific column
# Replace 'your_column_name' with the actual name of the column containing numbers
duplicates = df[df.duplicated('Number of tries', keep=False)]

# Step 3: Remove duplicates
df_cleaned = df.drop_duplicates(subset='Number of tries', keep=False)

# Step 4: Optionally save the cleaned data back to a CSV file
df_cleaned.to_csv('Guess.csv', index=False)

# Displays win/loss trends over time
print(df.head())