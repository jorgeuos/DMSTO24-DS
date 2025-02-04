import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data from the CSV file
df = pd.read_csv('/Users/viktorheidmark/Documents/DMSTO24-DS/ovningar/inlämningsuppgift_2.csv')

# Handle missing values (if any)
df.fillna(0, inplace=True)

# Create new columns
df['total'] = df['women'] + df['men']
df['women_percentage'] = round((df['women'] / df['total']) * 100, 1)
df['men_percentage'] = round((df['men'] / df['total']) * 100, 1)




# Filter data (example: focus on years where total is greater than a threshold)
filtered_df = df[df['total'] > 600000]



# Summarize and analyze key metrics
summary = filtered_df.groupby('year').agg({
    'women': 'sum',
    'men': 'sum',
    'total': 'sum',
    'women_percentage': 'sum',
    'men_percentage': 'sum'
})

print(summary)