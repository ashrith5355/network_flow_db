import csv
import mysql.connector
import time

# Connect to MariaDB
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="ashrith789",
    database="ashrith"
)

# Cursor
cursor = conn.cursor()

def insert_data_from_csv(csv_file):
    start_time = time.time()
    with open(csv_file, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip header row if exists
        for row in csv_reader:
            scr_ip, des_ip, scr_port, des_port, ip_version = row
            # Insert data into the table
            cursor.execute("INSERT INTO Network (scr_ip, des_ip, scr_port, des_port, ip_version) VALUES (%s, %s, %s, %s, %s)",
                           (scr_ip, des_ip, scr_port, des_port, ip_version))
    # Commit the transaction
    conn.commit()

    end_time = time.time()
    print("Data inserted successfully.")
    print(f"Time taken for insertion: {end_time - start_time} seconds")

csv_file = "data_100_tuples.csv"  # Change this line to the new CSV file name
insert_data_from_csv(csv_file)

# Close cursor and connection
cursor.close()
conn.close()
