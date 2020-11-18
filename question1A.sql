-- Create Database
CREATE DATABASE ds_questions;

-- Navigate to DATABASE
USE ds_questions;

-- Create name_table
CREATE TABLE name_table (
    StudentID VARCHAR(40) NOT NULL,
    Student_Name VARCHAR(40) NOT NULL,
    PRIMARY KEY ( StudentID )
);

-- Create mark_table
CREATE TABLE mark_table (
    StudentID VARCHAR(40) NOT NULL,
    Total_Marks INT NOT NULL,
    PRIMARY KEY ( StudentID )
);

-- Insert Values Into name_table
INSERT INTO name_table (StudentID, Student_Name)
    VALUES
    ('V001', 'Abe');

INSERT INTO name_table (StudentID, Student_Name)
    VALUES
    ('V002', 'Abhay');

INSERT INTO name_table (StudentID, Student_Name)
    VALUES
    ('V003', 'Acelin');

INSERT INTO name_table (StudentID, Student_Name)
    VALUES
    ('V004', 'Adelphos');

-- Insert Values Into mark_table
INSERT INTO mark_table (StudentID, Total_Marks)
    VALUES
    ('V001', 95);

INSERT INTO mark_table (StudentID, Total_Marks)
    VALUES
    ('V002', 80);

INSERT INTO mark_table (StudentID, Total_Marks)
    VALUES
    ('V003', 74);

INSERT INTO mark_table (StudentID, Total_Marks)
    VALUES
    ('V004', 81);

-- Select all from name_table
SELECT * FROM name_table;

-- Select all from mark_table
SELECT * FROM mark_table;

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