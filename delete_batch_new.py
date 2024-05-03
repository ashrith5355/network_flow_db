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

def delete_data_from_csv_batched(csv_file, batch_size):
    total_start_time = time.time()
    with open(csv_file, 'r') as file:
        csv_reader = csv.reader(file)
        #next(csv_reader)  # Skip header row if exists
        batch_count = 0
        total_time = 0
        for row in csv_reader:
            start_time = time.time()
            batch_data = []
            for _ in range(batch_size):
                try:
                    scr_ip, des_ip, scr_port, des_port, ip_version = next(csv_reader)
                    batch_data.append((scr_ip, des_ip, scr_port, des_port, ip_version))
                except StopIteration:
                    break  # End of file reached

            if batch_data:
                # Construct the WHERE clause using all primary key columns
                where_clause = " OR ".join(["(scr_ip = %s AND des_ip = %s AND scr_port = %s AND des_port = %s AND ip_version = %s)"] * len(batch_data))
                query = f"DELETE FROM Network WHERE {where_clause}"
                # Flatten the batch_data list to use as parameters in executemany
                flat_batch_data = [item for sublist in batch_data for item in sublist]
                cursor.execute(query, flat_batch_data)
                conn.commit()
                batch_count += 1
                end_time = time.time()
                batch_time = end_time - start_time
                total_time += batch_time
                print(f"Batch {batch_count} deleted successfully. Time taken: {batch_time:.2f} seconds.")

    total_end_time = time.time()
    print("All data deleted successfully.")
    print(f"Total time taken for deletion: {total_end_time - total_start_time:.2f} seconds")
    print(f"Average time per batch: {total_time / batch_count:.2f} seconds")


# Switch case for different operations
operation = input("Enter operation (delete): ").lower()

if operation == "delete":
    csv_file = "shuffled_data.csv"  # Change this line to the new CSV file name
    batch_size = int(input("Enter batch size: "))
    delete_data_from_csv_batched(csv_file, batch_size)
else:
    print("Invalid operation.")

# Close cursor and connection
cursor.close()
conn.close()
