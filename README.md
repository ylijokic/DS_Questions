
# Data Science Internship Questions

This repository contains answers to the Data Science Internship take home assessment.

---

1. - A.) Answer to Question 1A located in question1A.sql. 
      The specific queries are as follows:
      ```sql
        -- Create variable to hold Total_Marks of Student V002
        SELECT @grade := Total_Marks
        FROM mark_table
        WHERE StudentID = 'V002';

        -- Select all Students with a higher grade than V002 using an inner join statement
        SELECT name_table.Student_Name, mark_table.StudentID
        FROM name_table 
        INNER JOIN mark_table 
        ON name_table.StudentID = mark_table.StudentID
        WHERE mark_table.Total_Marks > @grade;
    
- B.) Answer to Question 1B is located in question1B.py. 
        The specific function is the following:

    ```python
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
    ```
 - C.) Answer to Question 1C is located in question1C.py.
      The specific function is the following:

      ```python
            def summarize_averages(names_df, marks_df):
                merge_df = pd.merge(names_df, marks_df, on='StudentID')
                summary_df = pd.DataFrame(columns = ['Name_Type', 'Average_Marks'], dtype=int)
                
                for index in merge_df.index:
                    name = merge_df['Student_Name'][index]
                    mark = merge_df['Total_Marks'][index]

                    if (name.isupper()):
                        new_row = {'Name_Type': 'uppercase', 'Average_Marks': mark}
                        summary_df = summary_df.append(new_row, ignore_index=True)
                        
                    else:
                        new_row = {'Name_Type': 'lowercase', 'Average_Marks': mark}
                        summary_df = summary_df.append(new_row, ignore_index=True)
                
                
                summary_df = summary_df.groupby('Name_Type', as_index=False)['Average_Marks'].mean()
                return summary_df
      ``` 

2. 