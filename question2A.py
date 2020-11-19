import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./data2.csv')

# Print the Shape of the DataFrame to see number of expected rows & columns
print('DATA FRAME SHAPE:')
print('---------------------------')

print(df.shape)

# Print the DataFrame info to see what columns have missing data
print('DATA FRAME INFO:')
print('---------------------------')

print(df.info())

print('NULL VALUES PER COLUMN:')
print('---------------------------')
print(df.apply(lambda x: sum(x.isnull()), axis=0))

# The Position Title has 2 Null Values, so we need to account for that
# Looking at the CSV File we can see that there are two rows where the Position Title got appended to the Pay Basis

# Search for the rows where the Pay Basis is not "Per Annum"
for index in df.index:
        pay_basis = df['PAY BASIS'][index]
        if (pay_basis != "Per Annum"):
            # Slice the pay_basis string to extract the actual job title
            job_title = pay_basis[10:]

            # Fill in the correct pay_basis and position_title for this specific index
            df['PAY BASIS'][index] = pay_basis[:10]
            df['POSITION TITLE'][index] = job_title

print('NULL VALUES PER COLUMN AFTER TRANSFORMATION:')
print('--------------------------------------------')

# Print the Columns and count of NULL Values to see we got rid of the NULL Values in POSITION TITLE Column
print(df.apply(lambda x: sum(x.isnull()), axis=0))

print('EMPLOYEE NAME FREQUENCY:')
print('---------------------------')
# Get counts of Employee Names to see if there are duplicates:
print(df['NAME'].value_counts())

# Convert Salary into a float so you can calculate additional features
df['MONTHLY PAY'] = df['SALARY'].astype('str').str.replace('$', '').str.replace(',', '')
df['MONTHLY PAY'] = df['MONTHLY PAY'].astype(float)
df['MONTHLY PAY'] = df['MONTHLY PAY'].apply(lambda x: x/12)

# Print final Data Frame
print('FINAL DATA FRAME:')
print('---------------------------')
print(df.info())
print(df.head())

