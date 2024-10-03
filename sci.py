# here I will observe the data, I will understand the data
import matplotlib as plt
import numpy as np
import pandas as pd

# Load the CSV data into a DataFrame
df = pd.read_csv('Guess.csv')

for i in range(len(df['Number of tries'])):
    if df['Number of tries'][i] != i:
       df.drop(i)
        

# print(df["Number of tries"])
# print(len(df['Number of tries']))
# Display basic statistics
# print(df.describe())

# Displays win/loss trends over time
# print(df.head())