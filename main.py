import pymssql

# Define connection details
server = 'ServerName' # Replace with actual servername
port = 1433
user = 'YourUsername'  # Replace with your username
password = 'YourPasswords'  # Replace with the actual password
database = 'Datbase-Name' #  Replace with the database password

try:
    # Connect to the database
    print("Connecting to the database...")
    conn = pymssql.connect(server=server, user=user, password=password, database=database)
    cursor = conn.cursor()
    print("Connected successfully!")

    # Step 1: Check existing columns in the cash_flow_data table
    print("Checking existing columns in the table...")
    cursor.execute("""
        SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'cash_flow_data'
    """)
    columns = [row[0] for row in cursor.fetchall()]
    print("Existing columns:", columns)

    # Step 2: Add missing columns if they don't exist
    if 'amount' not in columns:
        print("Adding missing column 'amount'...")
        cursor.execute("ALTER TABLE cash_flow_data ADD amount DECIMAL(10,2);")
        conn.commit()
        print("Column 'amount' added successfully.")
    else:
        print("Column 'amount' already exists.")

    if 'transaction_date' not in columns:
        print("Adding missing column 'transaction_date'...")
        cursor.execute("ALTER TABLE cash_flow_data ADD transaction_date DATE;")
        conn.commit()
        print("Column 'transaction_date' added successfully.")
    else:
        print("Column 'transaction_date' already exists.")

    # Step 3: Insert sample data into cash_flow_data table
    print("Inserting sample data into the table...")
    insert_data_query = """
    INSERT INTO cash_flow_data (amount, transaction_date, transaction_category)
    VALUES 
        (5000.00, '2024-01-20', 'Income'),
        (1200.00, '2024-01-15', 'Expense'),
        (2000.00, '2024-01-10', 'Income')
    """
    cursor.execute(insert_data_query)
    conn.commit()
    print("Sample data inserted into 'cash_flow_data'.")

    # Step 4: Fetch and print the inserted data to verify
    print("Fetching data from the table...")
    cursor.execute("SELECT * FROM cash_flow_data")
    rows = cursor.fetchall()

    print("\n--- Cash Flow Data for Akash ---")
    for row in rows:
        print(row)

    # Close the connection
    cursor.close()
    conn.close()
    print("Database connection closed.")

except pymssql.DatabaseError as db_err:
    print("Database Error:", db_err)
except pymssql.InterfaceError as conn_err:
    print("Connection Error:", conn_err)
except Exception as e:
    print("An unexpected error occurred:", e)
