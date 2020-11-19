## Data Science Internship Questions
---
## Charlie Ylijoki

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

2. - A.) Answer to Question 2A is located in question2A.py.
   
   - B.) Answer to question 2B is located in question2B.py. There is also an associated Jupyter Notebook question2B.py.

---


3. 
    **If you were asked to impute null values in a column of a file that was 365 Gigabytes, what would you do?  What tools would you use?  What tools would you NOT use?**

    In order to accomplish this task I would think about the different strategies to account for the NULL values and whether the NULL values are occurring completely at random or not. Since the file is so large, and simply ignoring the records with NULL values could result in algorithmic complications, a solid imputation strategy will needed. 

    A simple approach could be to replace the NULL values with the Mean of the non-NULL values for that column. This would only work for numeric data types and could lead to loss in data correlations. A similar approach could be used with categorical data by replacing NULL values with the most common category. Neither of these are ideal, and for such a large file would probably not be recommended.

    I better approach would be to use an algorithm to try to accurately predict what the NULL value should be. An example of this would be K Nearest Neighbors algorithm available in the impyute python library. This could potentially lead to long analysis times for such a large file. 

    A more advanced imputation approach would be to use the multiple imputation approach. This involves generating replacement values more than one time, analyzing how to combine the various replacement values, and then integrating the final imputed values. The popular algirithm for this approach is MICE, which is available as a python package or within an R-script library. 

    All of these approaches could be implemented using python and various python or R libraries (scikitlearn, impyute, fancyimpute, missingpy, miceRanger). Assuming this would be a one time project, I would not rely on third party paid software, but as the data grows it might be needed.  
   
---


4. **What would you do if you were asked to do the above task every Thursday morning at 2:00am?**
   
   In order to automate this task based on a time stamp, I would think about what my chosen solution was and how long it takes to complete. I would also be considerate of where the input data files are coming from, and where the output data needs to be stored. 
   
   If it were one of the less computationally expensive solutions that can be implemented with python and a few libraries, then I would create a trigger to run the code. This could be a script running on in internal server, or it could be a function running on a cloud infastructure such as AWS Lambda. Chances are the amount of data would add up over time and a Big Data storage solution would become available for the output data.

   If one of the more complex solutions was chosen as the most suitable, then there may be a need to have the cloud infastructure take care of the automation. This might be beyond the scope of severless functions mentioned for the simpler solution. I know Microsoft Azure has the Data Factory tool to create automated data pipelines, and I'm sure AWS, Google, and the other cloud providers have similar services. 

---

5. **Who is your favorite mathematician, statistician or computer scientist and why?**
   
   As a Computer Science student I would have to say Linus Torvalds, the creator of Linux and Git. The fact that Linux is present in the vast majority of computers throughout the world, and is considered the most successful software by many software developers, could alone be enough to say he is the most influential Computer Scientist in my lifetime. 
   
   However, what really sets him apart is Linus and the Linux Foundations's role in popularizing open source software. Git is probably the most popular version control system, and it is kind of crazy to think that it is his second most famous development. Without tools like git, it might not have been possible for free and open source software to advance at the rate it has in the past 30 years.  
   
   Also, like me, he is Finnish-American and lives in Portland, OR.