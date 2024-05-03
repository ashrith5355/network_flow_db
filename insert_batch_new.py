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

def insert_data_from_csv_batched(csv_file, batch_size):
    total_start_time = time.time()
    with open(csv_file, 'r') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)  # Read and store the header row
        batch_count = 0
        total_time = 0
        while True:
            start_time = time.time()
            batch_data = []
            for _ in range(batch_size):
                try:
                    scr_ip, des_ip, scr_port, des_port, ip_version = next(csv_reader)
                    batch_data.append((scr_ip, des_ip, scr_port, des_port, ip_version))
                except StopIteration:
                    break  # End of file reached

            if batch_data:
                cursor.executemany("INSERT INTO Network (scr_ip, des_ip, scr_port, des_port, ip_version) VALUES (%s, %s, %s, %s, %s)",
                                   batch_data)
                conn.commit()
                batch_count += 1
                end_time = time.time()
                batch_time = end_time - start_time
                total_time += batch_time
                print(f"Batch {batch_count} inserted successfully. Time taken: {batch_time:.2f} seconds.")

            if not batch_data:
                break  # No more data to read

    total_end_time = time.time()
    print("All data inserted successfully.")
    print(f"Total time taken for insertion: {total_end_time - total_start_time:.2f} seconds")
    print(f"Average time per batch: {total_time / batch_count:.2f} seconds")


# Switch case for different operations
operation = input("Enter operation (insert): ").lower()

if operation == "insert":
    csv_file = "data_1000000_tuples.csv"  # Change this line to the new CSV file name
    batch_size = int(input("Enter batch size: "))  # Get batch size from user
    insert_data_from_csv_batched(csv_file, batch_size)
else:
    print("Invalid operation.")

# Close cursor and connection
cursor.close()
conn.close()
