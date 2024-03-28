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

def delete_data_from_csv(csv_file):
    start_time = time.time()
    with open(csv_file, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip header row if exists
        for row in csv_reader:
            scr_ip, des_ip, scr_port, des_port, ip_version = row
            # Delete data from the table
            cursor.execute("DELETE FROM network1000000 WHERE scr_ip = %s AND des_ip = %s AND scr_port = %s AND des_port = %s AND ip_version = %s", (scr_ip, des_ip, scr_port, des_port, ip_version))
    # Commit the transaction
    conn.commit()

    end_time = time.time()
    print("Data deleted successfully.")
    print(f"Time taken for deletion: {end_time - start_time} seconds")

# Main function
def main():
    # Switch case for different operations
    operation = input("Enter operation (delete): ").lower()

    if operation == "delete":
        csv_file = "data_100000_delete.csv"  # Change this line to the new CSV file name
        delete_data_from_csv(csv_file)
    else:
        print("Invalid operation.")

    # Close cursor and connection
    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()
