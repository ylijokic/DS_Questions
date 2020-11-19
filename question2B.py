import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('./data.csv', names=['index', 'value'])

# Descriptive Stats
mean = df['value'].mean()
print(mean)

max = df['value'].max()
print(max)

min = df['value'].min()
print(min)

median = df['value'].median()
print(median)

std = df['value'].std()
print(std)

# Summary of Descriptive Stats
print('---------------------------')

print(df['value'].describe())

print('---------------------------')

# Display Histogram
df.plot(x = 'index', y = 'value', kind = 'hist')
plt.show()

print('---------------------------')

# Display skew of values 
print(df['value'].skew())

# The data is skewed to the right so we can cap the higher values.
# We can get the 90th percentile of the values and cap the data there
print(df['value'].quantile(0.90))
df["value"] = np.where((df["value"] > 26.9) & (df["value"] < 19.2), 26.9 , df['value'])
print(df['value'].skew())

df.plot(x = 'index', y = 'value', kind = 'hist')
plt.show()



