## Simple EDA Generator Introduction
### Author: Fiona Wu
### UID: 905774219

Introduction to my streamlit application: 

This application is able to allow users to upload a csv file, provide dataset information, and generate apppropriate visualizations for different types of variables.

Funcitonalities:

 1. Upload file by clicking "Browse files"
    - the application will read the csv file and store it as a data frame
 2. Display dataset as data frame
    - if the file is successfully uploaded and read, the data frame can be displayed by checking the box 
 3. Display relevant dataset statistics
    - by checking the second box, relevant statistics are displayed, including number of rows and columns, and number of categorical/numerical/boolean variables.
 4. Select a column for EDA
    - the user can select a column to perform simple EDA. Depending on the type of variable, there will be different information and visualizations provided.
 5. View five number summary and distribution graph for numerical variables
    - for numerical variables, five number summary is displayed in a table, and a distribution graph is displayed.
 6. View proportions visualizations for categorical variables
    - for categorical variables, proportions of each category is displayed in a table, and a bar graph is displayed.

 
Here is a link to the application:

[streamlit application](https://rwu331-streamlit-application-app-u1jj90.streamlit.app/)