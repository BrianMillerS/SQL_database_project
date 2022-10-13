#!/usr/bin/env python3

# DESCRIPTION:
# This script generates csv files with randomly generated data for all of the tables/relations 
# necessary for the aircontrol database to function properly. One csv file each will be made
# with the name of the csv file as the same as the name of the table or relation.
#
# USAGE:
# python3 generate_aircontrol_data.py

import pandas as pd
import datetime 
import string
import random
from random import randrange


def random_date(start,l):
   current = start
   while l >= 0:
      curr = current + datetime.timedelta(minutes=randrange(60))
      yield curr
      l-=1
    

def make_list_random_time(output_type, n):
    # params
    startDate = datetime.datetime(2000, 1, 20,13,00)
    output = []
    
    # make random date
    for x in random_date(startDate, n):
        if output_type == 'date':
            output.append(x.strftime("%d/%m/%Y"))
        elif output_type == 'time':
            output.append(x.strftime("%H:%M"))
    return output


# load txt of common english names
my_file = open("names.txt", "r")
data = my_file.read()
common_eng_names = data.replace('\n', '.').split(".")  # replacing end of line('/n') with ' ' and splitting the text
my_file.close()

# load ascii letter
letters = string.ascii_uppercase

###  PASSENGER ###
# passenger_id (int) range 1 - 30,000
# flight_number (str) (all caps) (15 character length) random string
# name (str) from corpus
# age (int) range from 10-100
# weight: (int) range from 100-200

## flight_number
# make list of 2000 flights
unique_flight_universe = []
for i in range(1,2001):
    unique_flight_universe.append(''.join(random.choice(letters) for i in range(15)))

passenger_df = pd.DataFrame()
passenger_df['passenger_id'] = range(1, 30001)
passenger_df['flight_number'] = [random.choice(unique_flight_universe) for i in range(1, 30001)]
passenger_df['name'] = [random.choice(common_eng_names) for i in range(1, 30001)]
passenger_df['age'] = [random.randint(10, 100) for i in range(1, 30001)]
passenger_df['weight'] = [random.randint(100, 200) for i in range(1, 30001)]


### PILOT ###
# pilot_id (int) range 1 - 2000
# name (str) from corpus
# age (int) range from 10-100
# skill_level (int) 1-5
pilot_df = pd.DataFrame()
pilot_df['pilot_id'] = range(1, 2001)
pilot_df['name'] = [random.choice(common_eng_names) for i in range(1, 2001)]
pilot_df['age'] = [random.randint(25, 60) for i in range(1, 2001)]
pilot_df['skill_level'] = [random.randint(1, 5) for i in range(1, 2001)]


### AIRPORT ###
# airport_code (str) 5 length
# city (str) (10 length)
# num_stores (int) 1-100
airport_df = pd.DataFrame()
airport_df['airport_code'] = [''.join(random.choice(letters) for i in range(5)) for i in range(1, 2001)]
airport_df['city'] = [''.join(random.choice(letters) for i in range(10)) for i in range(1, 2001)]
airport_df['num_stores'] = [random.randint(1, 10) for i in range(1, 2001)]


### AIRPLANE ###
# plane_id (int) 1-2000
# seat_capacity (int) range 5-250
# name (str) from corpus
# plane_model_number (int) range 1-15
# skill_level_required (int) range 1-5
# weight_capacity (int) (avg weight = 150)
airplane_df = pd.DataFrame()
airplane_df['plane_id'] = range(1, 2001)
airplane_df['seat_capacity'] = [random.randint(5, 250) for i in range(1, 2001)]
airplane_df['name'] = [random.choice(common_eng_names) for i in range(1, 2001)]
airplane_df['plane_model_number'] = [random.randint(1, 15) for i in range(1, 2001)]
airplane_df['skill_level_required'] = [random.randint(1, 10) for i in range(1, 2001)]
airplane_df['weight_capacity'] = airplane_df["seat_capacity"] * 150


### FLIGHT ###
# flight_number (str) from passenger_df
# pilot_id (int) random range 1-2000
# plane_id (int) random range 1-2000
# airline (str) (length=7)
# destination_city (str) (random from AIRPORT)
# departure_city (str) (random from AIRPORT)
# cost (int) range 100-2000
# departure_time (str)
# date (str)
flight_df = pd.DataFrame()
flight_df['flight_number'] = unique_flight_universe
flight_df['pilot_id'] = [random.randint(1, 2001) for i in range(1, 2001)]
flight_df['plane_id'] = [random.randint(1, 2001) for i in range(1, 2001)]
flight_df['airline'] = [''.join(random.choice(letters) for i in range(7)) for i in range(1, 2001)]
flight_df['destination_city'] = [random.choice(airport_df["city"]) for i in range(1, 2001)]
flight_df['departure_city'] = [random.choice(airport_df["city"]) for i in range(1, 2001)]
flight_df['cost'] = [random.randint(100, 2000) for i in range(1, 2001)]
flight_df['departure_time'] = make_list_random_time('time', 1999)
flight_df['date'] = make_list_random_time('date', 1999)
 
### HOUSED ###
housed_df = pd.DataFrame()
housed_df['plane_id'] = airplane_df['plane_id']
housed_df['airport_code'] = airport_df['airport_code']

# write to csv files
passenger_df.to_csv('/Users/brianmiller/Desktop/db_class/passenger', sep=',', index=False, header=False)
pilot_df.to_csv('/Users/brianmiller/Desktop/db_class/pilot', sep=',', index=False, header=False)
airport_df.to_csv('/Users/brianmiller/Desktop/db_class/airport', sep=',', index=False, header=False)
airplane_df.to_csv('/Users/brianmiller/Desktop/db_class/airplane', sep=',', index=False, header=False)
flight_df.to_csv('/Users/brianmiller/Desktop/db_class/flight', sep=',', index=False, header=False)
housed_df.to_csv('/Users/brianmiller/Desktop/db_class/housed', sep=',', index=False, header=False)
