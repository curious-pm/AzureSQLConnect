## Join the Community  
[Join Curious PM Community](https://curious.pm) to connect, share, and learn with others!
---
# Azure SQL Database Interaction Guide

This repository demonstrates how to interact with an Azure-hosted SQL Database using Python. The provided script showcases how to connect to the database, check for existing columns, add missing ones, insert sample data, and retrieve records.

**Note:** This repository is for educational purposes only.
---
## What the Code Does  
The code helps users connect to an Azure SQL Database, verify table structures, add missing columns, insert sample data, and retrieve records for analysis. It ensures smooth interaction with the database and follows best practices for secure operations.

---

## What is an Azure SQL Database?

Azure SQL Database is a cloud-based relational database service by Microsoft Azure. It offers features such as scalability, security, and high availability. Azure SQL databases allow users to interact with structured data while benefiting from cloud advantages like automated backups and disaster recovery.

---

## Choosing Your Preferred Library

You can interact with Azure SQL Database using various Python libraries such as:

- **`pymssql`** – A simple SQL Server driver for Python.
- **`pyodbc`** – A more versatile ODBC driver that works across different platforms.
- **`sqlalchemy`** – An ORM that provides a high-level way to interact with databases.

Choose the library that best suits your application's needs and ensure it is installed using:

```bash
pip install pymssql  # For pymssql
pip install pyodbc   # For pyodbc
pip install sqlalchemy  # For sqlalchemy
```

---
## Folder Structure  

```
azure_sql_connect/
├── README.md             # Documentation explaining the project and usage.
├── main.py               # Main script for database interaction.
└── requirements.txt      # List of required Python libraries to run the application.
```
### Explanation of Files  

- **README.md**  
  Provides details on project setup, usage, and security considerations.

- **main.py**  
  Handles connection, schema checking, data insertion, and retrieval.

- **requirements.txt**  
  Contains dependencies needed to run the application.

--- 


## Connecting to Azure SQL Database

### Prerequisites
1. **Azure SQL Database Access:**
   - Obtain your database credentials from the administrator.
   - Ensure your assigned table exists.

2. **Install Python Dependencies:**
   Install the required package based on your library preference.

3. **Connecting to Azure SQL Database:**

### 1. Establishing a Connection

To interact with Azure SQL Database, you need to establish a connection using your credentials. Below is an example of how you can connect to the database using Python.

#### **Syntax:**
```python
import pymssql

# Define connection parameters
server = 'your_server.database.windows.net'
user = 'your_username'
password = 'your_password'
database = 'your_database'

try:
    conn = pymssql.connect(server=server, user=user, password=password, database=database)
    cursor = conn.cursor()
    print("Connected to Azure SQL Database successfully.")

    # Always close the connection after usage
    cursor.close()
    conn.close()
except Exception as e:
    print("Connection failed:", e)
```

#### **Explanation:**
1. Define connection parameters (`server`, `user`, `password`, `database`).
2. Use `pymssql.connect()` to establish a connection.
3. Always close the connection after execution to avoid resource leaks.
4. Exception handling to catch connection failures.

---

### 2. Checking and Adding Columns

Before adding new columns to the assigned table, it's essential to check if the column already exists to avoid errors.

#### **Syntax:**
```python
column_name = 'new_column'
column_type = 'VARCHAR(100)'

check_column_query = f"""
SELECT COLUMN_NAME 
FROM INFORMATION_SCHEMA.COLUMNS 
WHERE TABLE_NAME = 'your_assigned_table' 
AND COLUMN_NAME = '{column_name}'
"""

cursor.execute(check_column_query)
result = cursor.fetchone()

if not result:
    alter_table_query = f"ALTER TABLE your_assigned_table ADD {column_name} {column_type};"
    cursor.execute(alter_table_query)
    print(f"Column '{column_name}' added successfully.")
else:
    print(f"Column '{column_name}' already exists.")
```

#### **Explanation:**
1. Check if the column exists using `INFORMATION_SCHEMA.COLUMNS`.
2. Add the column only if it does not exist.
3. Print confirmation messages for better tracking.

---

### 3. Inserting Data

Once the required columns are available, data can be inserted into the assigned table.

#### **Syntax:**
```python
insert_query = """
INSERT INTO your_assigned_table (new_column, transaction_category)
VALUES (%s, %s)
"""
data_to_insert = [
    ('Sample Data 1', 'Category A'),
    ('Sample Data 2', 'Category B'),
    ('Sample Data 3', 'Category C')
]

cursor.executemany(insert_query, data_to_insert)
conn.commit()
print("Sample data inserted successfully.")
```

#### **Explanation:**
1. Prepare an `INSERT` statement with placeholders (`%s`).
2. Use `executemany()` to insert multiple rows efficiently.
3. Commit changes to save data permanently.

---

### 4. Fetching and Displaying Data

Retrieving data from the assigned table to verify that everything works correctly.

#### **Syntax:**
```python
cursor.execute("SELECT * FROM your_assigned_table")
rows = cursor.fetchall()

print("\n--- Retrieved Data ---")
for row in rows:
    print(row)
```

#### **Explanation:**
1. Execute a `SELECT` query to retrieve all data.
2. Use `fetchall()` to get all rows.
3. Print the retrieved data for verification.

---
## What Happens Step by Step  

1. **Connect to Azure SQL Database:**  
   - Establishes a secure connection using credentials.  
   
2. **Check for Missing Columns:**  
   - Ensures required columns exist in the table.  
   
3. **Add Columns if Needed:**  
   - Adds missing columns to match expected structure.  
   
4. **Insert Sample Data:**  
   - Populates the table with test records.  
   
5. **Retrieve Data:**  
   - Fetches and displays data for validation.  
   
6. **Close Connection:**  
   - Safely closes the database connection after processing.

---


## Important Rules and Best Practices

To ensure smooth and secure interaction with the Azure SQL Database, follow these guidelines:

**1. Work Only on Assigned Tables:**  
   - You are authorized to work **only** with the table(s) assigned to you (e.g., `cash_flow_data`).  
   - **Creating new tables or modifying the schema outside your assigned scope is prohibited.**

**2. Security Best Practices:**  
   - Store credentials securely and avoid sharing them with others.  
   - Use parameterized queries to prevent SQL injection.  
   - Handle exceptions gracefully and log errors.

**3. Connection Management:**  
   - Always close database connections after each interaction to avoid resource leaks.  
   - Do not leave connections open unnecessarily.

**4. Query Efficiency:**  
   - Limit queries to only the required data to optimize performance.  
   - Avoid heavy queries that can impact database operations.

By following these rules, you can ensure secure and efficient database interactions while maintaining compliance with access policies.

---

## Connecting to Azure SQL via TablePlus

1. **Install TablePlus:**  
   Download it from [TablePlus](https://tableplus.com/).

2. **Set Up a New Connection:**
   - Open TablePlus and click **Create New Connection** → Select **SQL Server.**
   - Enter:
     - **Host:** `your_server.database.windows.net`
     - **Port:** `1433`
     - **User:** your username
     - **Password:** your password
     - **Database:** your assigned database

3. **Test the Connection** and save for future use.

---

## Database Operations Example (General Guide)

The provided script follows a structured approach to interact with the Azure SQL Database. The key operations performed in the script include:

### Steps in the Script:

1. **Check and Add Missing Columns:**  
   - The script checks if required columns exist in the assigned table.  
   - If any columns are missing, they are automatically added.

2. **Insert Sample Data:**  
   - Sample data is inserted into the table to help verify the setup.  
   - Ensure the data aligns with the assigned table structure.

3. **Retrieve and Display Data:**  
   - The script retrieves and prints data from the assigned table for validation purposes.

### Running the Script

Follow these steps to execute the script successfully:

1. Ensure that your database credentials (such as server name, username, and password) are configured correctly in your environment.
2. Run the script using the appropriate command for your setup, such as:

   ```bash
   python your_script_name.py
   ```
   
---
   
## Video Overview  
   *A short video walkthrough will be provided explaining the script's features and usage.*
   

**Note:** Avoid hardcoding sensitive credentials in the script; use environment variables or configuration files instead.