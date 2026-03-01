import pandas as pd
import numpy as np
import mysql.connector
from faker import Faker
import random

fake = Faker()

# -----------------------------
# MYSQL CONNECTION
# -----------------------------
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root@h1hashim",
    database="airline_ops"
)

cursor = conn.cursor()

# -----------------------------
# PARAMETERS
# -----------------------------
num_flights = 2000

airlines = ["Emirates","Qatar Airways",
            "Oman Air","Etihad","Turkish Airlines"]

airports = ["DXB","DOH","MCT","AUH","IST","LHR","JFK"]

seat_classes = ["Economy","Business","First"]

# -----------------------------
# GENERATE FLIGHTS DATA
# -----------------------------
flights_data = []

for i in range(num_flights):

    origin = random.choice(airports)
    destination = random.choice(
        [a for a in airports if a != origin]
    )

    departure = fake.date_time_between(
        start_date="-1y",
        end_date="now"
    )

    arrival = departure + pd.Timedelta(
        minutes=random.randint(60,600)
    )

    delay = max(0, int(np.random.normal(20,30)))

    flights_data.append((
        i+1,
        random.choice(airlines),
        origin,
        destination,
        departure,
        arrival,
        delay,
        random.randint(500,8000)
    ))

flights_df = pd.DataFrame(flights_data, columns=[
    "flight_id","airline","origin_airport",
    "destination_airport","departure_time",
    "arrival_time","delay_minutes","distance"
])

# -----------------------------
# INSERT FLIGHTS INTO MYSQL
# -----------------------------
flight_query = """
INSERT INTO flights
VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
"""

cursor.executemany(flight_query, flights_data)
conn.commit()

print("✅ Flights inserted")

# -----------------------------
# PASSENGERS DATA
# -----------------------------
passenger_data = []

for i in range(5000):
    passenger_data.append((
        i+1,
        random.randint(1, num_flights),
        round(random.uniform(100,2500),2),
        random.choice(seat_classes)
    ))

passengers_df = pd.DataFrame(passenger_data, columns=[
    "passenger_id","flight_id",
    "ticket_price","seat_class"
])

passenger_query = """
INSERT INTO passengers
VALUES (%s,%s,%s,%s)
"""

cursor.executemany(passenger_query, passenger_data)
conn.commit()

print("✅ Passengers inserted")

# -----------------------------
# FLIGHT STATUS DATA
# -----------------------------
status_data = []

for i in range(num_flights):
    status_data.append((
        i+1,
        random.choice(["On Time","Delayed","Cancelled"]),
        random.randint(0,60),
        random.randint(0,40),
        random.randint(0,20)
    ))

status_df = pd.DataFrame(status_data, columns=[
    "flight_id","status",
    "weather_delay",
    "technical_delay",
    "security_delay"
])

status_query = """
INSERT INTO flight_status
VALUES (%s,%s,%s,%s,%s)
"""

cursor.executemany(status_query, status_data)
conn.commit()

print("✅ Flight status inserted")

# -----------------------------
# EXPORT TO EXCEL
# -----------------------------
with pd.ExcelWriter("airline_operations_data.xlsx") as writer:
    flights_df.to_excel(writer,
                        sheet_name="Flights",
                        index=False)

    passengers_df.to_excel(writer,
                           sheet_name="Passengers",
                           index=False)

    status_df.to_excel(writer,
                       sheet_name="Flight_Status",
                       index=False)

print("✅ Excel file created")

cursor.close()
conn.close()