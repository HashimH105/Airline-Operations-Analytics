# 🛫 Airline Operations Analytics Dashboard

## Project Overview
This project demonstrates an **end-to-end airline operations analytics workflow**.  
It generates synthetic airline operational data using Python, stores it in a **MySQL database**, and creates interactive **Tableau dashboards** for business intelligence insights. An Excel file is also generated for backup and reporting purposes.

The dashboard helps monitor:

- Flight performance & delay patterns  
- Passenger revenue by seat class  
- On-time performance and delay causes  
- Airline operational trends  

This project is ideal for **data analyst, BI analyst, and data engineering portfolios**.

---

## 🛠️ Technologies Used

| Layer | Technology |
|-------|------------|
| Data Generation & ETL | Python (pandas, faker, mysql-connector-python, numpy) |
| Database | MySQL |
| Visualization | Tableau Desktop |
| Reporting | Excel (OpenPyXL) |

---

## ⚙️ Features

### Python ETL Pipeline
- Generates realistic flight, passenger, and flight status data.  
- Automatically inserts data into MySQL tables.  
- Exports synchronized Excel files for reporting.

### MySQL Database
- Stores flights, passengers, and flight status tables.  
- Supports SQL queries for analytics and KPI calculation.  
- Database creation script included (`database.sql`):

🚀 How to Run

## 1 Clone the repository
git clone https://github.com/<your-username>/Airline-Operations-Analytics.git
cd Airline-Operations-Analytics

## 2 Install Python dependencies
pip install pandas numpy faker mysql-connector-python openpyxl

## 3 Set up MySQL Database
Open MySQL → Run database.sql to create database and tables.

## 4 Update Python ETL script with your MySQL credentials:

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="airline_ops"
)

## 5 Run Python ETL script
python generate_airline_mysql.py
This will generate synthetic data and insert it into MySQL tables.
Excel file airline_operations_data.xlsx will also be created.

## 6 Verify data in MySQL
SELECT * FROM flights LIMIT 10;

## 7 Open Tableau Desktop
Connect to MySQL database airline_ops.
Use the three tables: flights, passengers, flight_status.
Build dashboards with KPIs, Pie Chart (Revenue by Seat Class), Flight Trends, Delay Analysis, and apply action filters.

📊 Dashboard Insights
Identify most delayed routes and airlines.
Track revenue distribution across seat classes.
Monitor monthly flight trends.
Analyze delay causes to support operational decisions.

FOR looking at my own Dashboard 
link:- https://public.tableau.com/app/profile/hashim.ebrahim/viz/AirlineOperationsAnalytics/AirlineFlights
