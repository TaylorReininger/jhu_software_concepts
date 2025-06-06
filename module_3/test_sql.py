import psycopg

# Psycopg (psycho pig) is a Python library to allow you to access a PostgreSQL database. 
# Before we can use it, we need to actually install software and create a database right on the OS.
# For demonstration purposes, I am going to go ahead and use it right in Linux first, then do it 
# in Python. 

"""
1. On Ubuntu, install psql (https://documentation.ubuntu.com/server/how-to/databases/install-postgresql/index.html)
    ```
    sudo apt install postgresql
    ```

2. Change permissions so we can access the database from psycopg
    ```
    sudo vim /etc/postgresql/16/main/pg_hba.conf 

    Make the local 'postgres' and 'all' users trusted with a couple edits
    # Database administrative login by Unix domain socket
    local   all         postgres                --> trust <-- this value
    # "local" is for Unix domain socket connections only
    local   all         all                     --> trust <-- this value

    # Save and close the file, then restart the postgresql service
    sudo systemctl reload postgresql
    ```

3. Create a PostgreSQL database
    ```
    sudo -u postgres createdb -O postgres my_database_name
    ```

NOTE: Everything before this must be done on the OS. After this, you can access the DB either
        in the OS or with Python through psycopg


4. Enter the database
    ```
    sudo -u postgres psql my_database_name
    ```

5. Create a table in the database (https://www.w3schools.com/postgresql/postgresql_create_table.php)
    ```
    CREATE TABLE test(a int, b VARCHAR(255), c int);
    ```

6. Insert data into the table
    ```
    INSERT INTO test (a, b, c)
    VALUES (1, 'TAYLOR', 35), (2, 'JACOB', 33), (3, 'ELSIE', 2);
    ```

7. View data in table
    ```
    SELECT * FROM test;
    ```

ADDITIONAL NOTES:
- To check for all the existing databases
```
sudo -u postgres psql -l        (Assuming the username of interest is postgres as used above)
```

- To delete a database (the DROP command)
```
sudo -u postgres psql           # Connect to the PostgreSQL instance
DROP DATABASE name_of_db        # Delete (drop) the database
exit                            # Disconnect from the PostgreSQL instance
```

"""


# Database name
name_db = 'test_db'
name_table = 'test_table'


# Connect to a postgresql server (must follow steps from above)
with psycopg.connect(dbname=name_db, user="postgres") as conn:


    # Open a cursor to perform database operations
    with conn.cursor() as cur:
       

        # Check if the table exists
        cur.execute("""
                SELECT COUNT(*) FROM information_schema.tables 
                WHERE table_name = '%s' 
                AND table_schema = 'public';
            """%(name_table))

        matches = cur.fetchone()

        # Create a the table if needed
        if not matches[0]:
            print('Creating table')
            cur.execute("""
                CREATE TABLE %s(a int, b VARCHAR(255), c int);
                """%(name_table))


        # Check if there is data in the table
        cur.execute("""
            SELECT * FROM %s;
            """%(name_table))

        # If data does not already exist, put some in the table
        if not bool(cur.fetchone()):

            # Put data in the table
            cur.execute("""
                INSERT INTO %s (a, b, c)
                VALUES (1, 'TAYLOR', 35), (2, 'JACOB', 33), (3, 'ELSIE', 2);
                """%(name_table))


        # Display all the content from the table at this stage
        cur.execute("""
            select * from %s;
            """%(name_table))

        # Print outputs
        print(cur.fetchall())

        # Commit the changes to the table
        conn.commit()




