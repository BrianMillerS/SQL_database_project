# Final Project Submission Files

# ER Diagram
My PDA is a database to organize flight information for airway control and general information regarding flights. flown_by, uses, and has_booking relations do not need to be added to the sql database as their keys are already a part of both relational sets. All tables have 3000 rows, except for Passenger, which has 30,000 rows.

Descriptions of each files:
generate_aircontrol_data.py       Python script that generates csv files for each of the tables in the database
make_aircontrol.sql               SQL script that creates the database, and uses the csv files to propogate the database
display_tables.sql                SQL script that displays the databse  
test_aircontrol.py                python script that runs a single unit test on the database, this checks that a given filght passes all requirements
Miller_Brian_test_example.pdf     An example ouput of test_aircontrol.py 
