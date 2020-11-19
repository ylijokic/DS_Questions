import pandas as pd
df = pd.read_csv('./data.csv', names=['index', 'value'])

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

print(df.head())