# Final Project Submission Files

## Database Description
My PDA is a database to organize flight information for airway control and general information regarding flights. flown_by, uses, and has_booking relations do not need to be added to the sql database as their keys are already a part of both relational sets. All tables have 3000 rows, except for Passenger, which has 30,000 rows.

![alt text](https://github.com/BrianMillerS/SQL_database_project/blob/main/aircontrol_ER_diagram.png)

<br/><br/>
## File Descriptions
*generate_aircontrol_data.py*<br/>
Python script that generates csv files for each of the tables in the database<br/><br/>
*make_aircontrol.sql*<br/>
SQL script that creates the database, and uses the csv files to propogate the database<br/><br/>
*display_tables.sql*<br/>
SQL script that displays the databse<br/><br/>
*test_aircontrol.py*<br/>
python script that runs a single unit test on the database, this checks that a given filght passes all requirements<br/><br/>
*Miller_Brian_test_example.pdf*<br/>
An example ouput of test_aircontrol.py<br/>
