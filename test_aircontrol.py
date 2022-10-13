#!/usr/bin/env python3

import mysql.connector #### USER INPUT ####

flight_number = "AABFJFNZATRXXGO"


#### SQL CONNECTION ####
mydb = mysql.connector.connect(
user='pysql', # could be root, or a user you created, I created 'testuser' passwd='ilovesql', # the password for that use
database='aircontrol', # the database to connect to
host='127.0.0.1', # localhost
allow_local_infile='1' # needed so can load local files
)
myc = mydb.cursor()
myc.execute('set global local_infile = 1') # allow loading of local files

# use the correct database
myc.execute ("use aircontrol")


#### SQL COMMANDS ####
myc.execute ("""SELECT plane_id FROM flight F WHERE F.flight_number = "{}"; """.format(flight_number))
plane_id_int = myc.fetchall()[0][0]

myc.execute ("""SELECT pilot_id FROM flight F WHERE F.flight_number = "{}"; """.format(flight_number))
pilot_id_int = myc.fetchall()[0][0]

myc.execute ("""SELECT COUNT(*) FROM passenger P WHERE P.flight_number = "{}"; """.format(flight_number))
num_passengers_int = myc.fetchall()[0][0]

myc.execute ("""SELECT SUM(weight) FROM passenger P WHERE P.flight_number = "{}"; """.format(flight_number))

sum_passenger_weight_int = myc.fetchall()[0][0]
myc.execute ("""SELECT seat_capacity FROM airplane A WHERE A.plane_id = "{}"; """.format(plane_id_int))

plane_seat_capacity_int = myc.fetchall()[0][0]
myc.execute ("""SELECT weight_capacity FROM airplane A WHERE A.plane_id = "{}"; """.format(plane_id_int))

plane_weight_capacity_int = myc.fetchall()[0][0]
myc.execute ("""SELECT skill_level_required FROM airplane A WHERE A.plane_id = "{}"; """.format(plane_id_int))

plane_skill_level_required_int = myc.fetchall()[0][0]
myc.execute ("""SELECT skill_level FROM pilot P WHERE P.pilot_id = "{}"; """.format(pilot_id_int))

pilot_skill_level_int = myc.fetchall()[0][0]


#### CHECK FLGIHT REQUIREMENTS ####
req_seat_capacity = num_passengers_int <= plane_seat_capacity_int
req_weight_capacity = sum_passenger_weight_int <= plane_weight_capacity_int
req_pilot_skill = pilot_skill_level_int >= plane_skill_level_required_int

if ((req_seat_capacity == True) & (req_weight_capacity == True) & (req_pilot_skill == True)): 
    all_requirements_satisfied = True
else:
    all_requirements_satisfied = False

print("Flight Number: {} \n".format(flight_number))
print("Seat Capacity Requirement Satisfied: {}".format(req_seat_capacity))
print("Number of total passengers: {}".format(num_passengers_int))
print("Plane seat capacity: {} \n".format(plane_seat_capacity_int))
print("Weight Requirement Satisfied: {}".format(req_weight_capacity))
print("Total weight of passengers (lbs): {}".format(sum_passenger_weight_int))
print("Plane weight capacity (lbs): {} \n".format(plane_weight_capacity_int))
print("Pilot Skill Level Requirement Satisfied: {}".format(req_pilot_skill))
print("Pilot skill level: {}".format(pilot_skill_level_int))
print("Plane skill level requires: {} \n".format(plane_skill_level_required_int))
print("RESULT: flight {} is cleared for flight: {}".format(flight_number, all_requirements_satisfied))


#### END SQL SESSION ####
mydb.commit()
mydb.close()