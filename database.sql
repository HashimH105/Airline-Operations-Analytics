CREATE DATABASE airline_ops;
USE airline_ops;

CREATE TABLE flights (
flight_id INT PRIMARY KEY,
airline VARCHAR(50),
origin_airport VARCHAR(10),
destination_airport VARCHAR(10),
departure_time TIMESTAMP,
arrival_time TIMESTAMP,
delay_minutes INT,
distance INT
);

CREATE TABLE passengers (
passenger_id INT,
flight_id INT,
ticket_price DECIMAL(10,2),
seat_class VARCHAR(20)
);

CREATE TABLE flight_status (
flight_id INT,
status VARCHAR(20),
weather_delay INT,
technical_delay INT,
security_delay INT
);

