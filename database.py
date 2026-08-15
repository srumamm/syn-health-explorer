import sqlite3
import pandas as pd

# Load the synthetic patient data
patients = pd.read_csv("patients.csv")

# Create a SQLite database
connection = sqlite3.connect("health.db")

# Load the data into a SQL table
patients.to_sql(
    "patients",
    connection,
    if_exists="replace",
    index=False
)

print(f"Loaded {len(patients)} patients into the database.")

# Close the connection
connection.close()