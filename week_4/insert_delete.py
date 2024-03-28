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
    try:
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
    except Exception as e:
        print(f"Error inserting data from {csv_file}: {e}")

def update_data():
    start_time = time.time()
    try:
        # Update data in the table
        cursor.execute("UPDATE Network SET ip_version = 'IPv6' WHERE ip_version = 'IPv4'")
        conn.commit()
        end_time = time.time()
        print("Data updated successfully.")
        print(f"Time taken for update: {end_time - start_time} seconds")
    except Exception as e:
        print(f"Error updating data: {e}")

def delete_data(csv_file):
    start_time = time.time()
    with open(csv_file, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip header row if exists
        for row in csv_reader:
            scr_ip, des_ip, scr_port, des_port, ip_version = row
            # Delete data from the table
            cursor.execute("DELETE FROM network WHERE scr_ip = %s AND des_ip = %s AND scr_port = %s AND des_port = %s AND ip_version = %s", (scr_ip, des_ip, scr_port, des_port, ip_version))
    # Commit the transaction
    conn.commit()

    end_time = time.time()
    print("Data deleted successfully.")
    print(f"Time taken for deletion: {end_time - start_time} seconds")

def restore_netflow5(csv_file):
    #conn = sqlite3.connect('flow.db')
    df = pd.read_csv(csv_file, header=None)
    df.columns = ['version', 'source_ip', 'destination_ip', 'source_port', 'destination_port']
    df.to_sql('Netflow5', conn, if_exists='append', index=False)
    conn.close()


# Switch case for different operations
operation = input("Enter operation (insert/update/delete): ").lower()

if operation == "insert":
    insert_data_from_csv('data_100_tuples.csv')
    insert_data_from_csv('data_1000_tuples.csv')
    insert_data_from_csv("data_10000_tuples.csv")
    insert_data_from_csv("data_100000_tuples.csv")
    insert_data_from_csv("data_1000000_tuples.csv")
elif operation == "update":
    update_data()
elif operation == "delete":
    delete_data("data_100_delete.csv")
    delete_data("data_1000_delete.csv")
    delete_data("data_10000_delete.csv")
    delete_data("data_100000_delete.csv")
else:
    print("Invalid operation.")

# Close cursor and connection
try:
    cursor.close()
    conn.close()
    print("Connection closed.")
except Exception as e:
    print(f"Error closing connection: {e}")
