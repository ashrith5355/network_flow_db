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

def update_ip_version_batched(batch_size):
    total_start_time = time.time()
    
    # Example update query to update ip_version from IPv4 to IPv6
    update_query = """
        UPDATE Network
        SET ip_version = 'IPv4'
        WHERE ip_version = 'IPv6'
        LIMIT %s
    """
    
    cursor.execute("SELECT COUNT(*) FROM Network WHERE ip_version = 'IPv6'")
    total_rows = cursor.fetchone()[0]
    batches = total_rows // batch_size
    remainder = total_rows % batch_size
    if remainder > 0:
        batches += 1

    batch_count = 0
    total_time = 0
    for i in range(batches):
        start_time = time.time()
        cursor.execute(update_query, (batch_size,))
        conn.commit()
        end_time = time.time()
        batch_count += 1
        batch_time = end_time - start_time
        total_time += batch_time
        print(f"Batch {batch_count} updated successfully. Time taken: {batch_time:.2f} seconds.")

    print("All data updated successfully.")
    print(f"Total time taken for update: {total_time:.2f} seconds")
    print(f"Average time per batch: {total_time / batch_count:.2f} seconds")


# Switch case for different operations
operation = input("Enter operation (update): ").lower()

if operation == "update":
    batch_size = int(input("Enter batch size: "))
    update_ip_version_batched(batch_size)
else:
    print("Invalid operation.")

# Close cursor and connection
cursor.close()
conn.close()
