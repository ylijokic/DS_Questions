import pandas as pd
import sqlalchemy
from question1B import change_names

engine = sqlalchemy.create_engine('mysql://root:@localhost/ds_questions')
df1 = pd.read_sql_table('name_table', engine)
df2 = pd.read_sql_table('mark_table', engine)

# Create new data frame with function from question 1B
df3 = change_names(df1)

def summarize_averages(names_df, marks_df):
    # Merge the two DFs passed in as parameters
    merge_df = pd.merge(names_df, marks_df, on='StudentID')
    summary_df = pd.DataFrame(columns = ['Name_Type', 'Average_Marks'], dtype=int)
    
    # Iterate through merged DF
    for index in merge_df.index:
        name = merge_df['Student_Name'][index]
        mark = merge_df['Total_Marks'][index]

        # Conditional to add name/grade to summary DF
        if (name.isupper()):
            new_row = {'Name_Type': 'uppercase', 'Average_Marks': mark}
            summary_df = summary_df.append(new_row, ignore_index=True)
            
        else:
            new_row = {'Name_Type': 'lowercase', 'Average_Marks': mark}
            summary_df = summary_df.append(new_row, ignore_index=True)
    
    # Group By statement to categorize name type and get average of grades
    summary_df = summary_df.groupby('Name_Type', as_index=False)['Average_Marks'].mean()
    return summary_df

df4 = summarize_averages(df3, df2)

print(df4.head())

