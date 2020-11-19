import pandas as pd
import sqlalchemy

engine = sqlalchemy.create_engine('mysql://root:@localhost/ds_questions')
df1 = pd.read_sql_table('name_table', engine)
df2 = pd.read_sql_table('mark_table', engine)
    
def change_names(data_frame):
    
    # Create DF copy and iterate through 'Student_Name' col using index method
    new_df = data_frame.copy(deep=True)
    
    for index in new_df.index:
        name = new_df['Student_Name'][index]
        
        # Conditional to make name upper/lower case
        if ('e' in name or 'E' in name):
            new_df['Student_Name'][index] = name.upper()
        else:
            new_df['Student_Name'][index] = name.lower()
    
    return new_df


df3 = change_names(df1)

# for index in df3.index:
#     print(df3['Student_Name'][index])

