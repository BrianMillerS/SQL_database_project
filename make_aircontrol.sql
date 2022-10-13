-- GENERATE DATABASE
drop database if exists aircontrol ;
create database aircontrol ;
use aircontrol ;
 
 
-- CREATE TABLES
drop table if exists flight ;
drop table if exists airplane ;
drop table if exists passenger ;
drop table if exists pilot ;
drop table if exists airport ;
drop table if exists housed ;
 
create table airplane (
   plane_id int NOT NULL,
   seat_capacity int,
   name varchar(20),
   plane_model_number int,
   skill_level_required int,
   weight_capacity int,
   Primary Key (plane_id)) ;
 
create table passenger (
   passenger_id int NOT NULL,
   flight_number varchar(20),
   name varchar(20),
   age int,
   weight int,
   Primary Key (passenger_id)) ;
 
create table pilot (
   pilot_id int NOT NULL,
   name varchar(20),
   age int,
   skill_level int,
   Primary Key (pilot_id)) ;
 
create table airport (
   airplort_code varchar(20) NOT NULL,
   city varchar(20),
   num_stores int,
   Primary Key (airplort_code)) ;
 
create table housed (
   plane_id int NOT NULL,
   airport_code varchar(20) NOT NULL,
   Primary Key (plane_id, airport_code)) ;
 
create table flight (
   flight_number varchar(20) NOT NULL,
   pilot_id int ,
   plane_id int,
   airline varchar(20),
   destination_city varchar(20),
   departure_city varchar(20),
   cost int,
   departure_time varchar(20),
   date varchar(20),
   Primary Key (flight_number),
   Foreign Key (pilot_id) references pilot(pilot_id),
   Foreign Key (plane_id) references airplane(plane_id));
 
 
-- ADDING DATA
SET GLOBAL local_infile=1;
 
load data local infile '/Users/brianmiller/Desktop/db_class/passenger' into table passenger
fields terminated by ','
lines terminated by '\n'
;
 
load data local infile '/Users/brianmiller/Desktop/db_class/housed' into table housed
fields terminated by ','
lines terminated by '\n'
;
 
load data local infile '/Users/brianmiller/Desktop/db_class/airport' into table airport
fields terminated by ','
lines terminated by '\n'
;
 
load data local infile '/Users/brianmiller/Desktop/db_class/pilot' into table pilot
fields terminated by ','
lines terminated by '\n'
;
 
load data local infile '/Users/brianmiller/Desktop/db_class/airplane' into table airplane
fields terminated by ','
lines terminated by '\n'
;
 
load data local infile '/Users/brianmiller/Desktop/db_class/flight' into table flight
fields terminated by ','
lines terminated by '\n'
;
