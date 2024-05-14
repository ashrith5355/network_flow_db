import csv
import mysql.connector
import ipaddress
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

def update_data():
    start_time = time.time()
    # Update data in the table
    cursor.execute("UPDATE Network1000000 SET ip_version = 'IPv6' WHERE ip_version = 'IPv4'")
    conn.commit()

    end_time = time.time()
    print("Data updated successfully.")
    print(f"Time taken for update: {end_time - start_time} seconds")

def delete_data():
    start_time = time.time()
    # Delete all data from the table
    cursor.execute("DELETE FROM Network1000000")
    conn.commit()

    end_time = time.time()
    print("All data deleted successfully.")
    print(f"Time taken for deletion: {end_time - start_time} seconds")
    
# Switch case for different operations
operation = input("Enter operation (insert/update/delete): ").lower()

if operation == "insert":
    csv_file = "data_1000000_tuples.csv"  # Change this line to the new CSV file name
    insert_data_from_csv(csv_file)
elif operation == "update":
    update_data()
elif operation == "delete":
    delete_data()
else:
    print("Invalid operation.")

# Close cursor and connection
cursor.close()
conn.close()
