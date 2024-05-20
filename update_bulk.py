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

def update_data():
    start_time = time.time()
    # Update data in the table
    cursor.execute("UPDATE Network SET ip_version = 'IPv6' WHERE ip_version = 'IPv4'")
    conn.commit()

    end_time = time.time()
    print("Data updated successfully.")
    print(f"Time taken for update: {end_time - start_time} seconds")

update_data()

# Close cursor and connection
cursor.close()
conn.close()
