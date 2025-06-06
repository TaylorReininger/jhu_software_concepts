import json
import psycopg

"""
Notes:

- All the data shall go into a table named "applicants"
- The table should have these fields:

| **Column Name** | **Data Type** | **Description** |
| ---             | ---           | ---             |
| p_id | integer | Unique identifier |
| program | text | University and Department |
| comments | text | Comments |
| date_added | date | Date Added |
| url | text | Link to Post on Grad Café |
| status | text | Admission Status |
| term | text | Start Term |
| us_or_international | text | Student nationality |
| gpa | float | Student GPA |
| gre | float | Student GRE Quant |
| gre_v | float | Student GRE Verbal |
| gre_aw | float | Student Average Writing |
| degree | text | Student Program Degree Type |


- I ran the following commands to stand up the database:
```
sudo -u postgres createdb -O postgres module3
```

"""

# JSON file name
name_json = '../module_2/application_data.json'

# Database name
name_db = 'module3'
name_table = 'test_table'



# Load in and extract the data from the JSON
with open(name_json, 'r') as f:
    # Load the JSON data into a Python object
    data = json.load(f)


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
                CREATE TABLE %s(
                p_id int,
                program TEXT,
                comments TEXT,
                date_added date,
                url TEXT,
                status TEXT,
                term TEXT,
                us_or_international TEXT,
                gpa FLOAT,
                gre FLOAT,
                gre_v FLOAT,
                gre_aw FLOAT,
                degree TEXT)
                ;"""%(name_table))


        # Iterate through the elements in the data
        for index in data:

            entry = data[index]
            print(entry)
            print(index)
            print(type(index))
            print(        entry['major'])
            print(        entry['notes'])
            print(        entry['date_entry'])
            print(        'put_url_here.com')
            print(        entry['decision'])
            print(        entry['semester'])
            print(        entry['american'])
            print(        entry['gpa'])
            print(        entry['gre'])
            print(        entry['grev'])
            print(        entry['greaw'])
            print(        entry['degree'])





            row = "%d, %s, %s, TO_DATE('%s', 'Month Day, Year'), %s, %s, %s, %s, %3.2f, %5.2f, %5.2f, %5.2f, %5.2f, %s"%(
                    int(index), 
                    entry['major'],
                    entry['notes'],
                    entry['date_entry'],
                    'put_url_here.com',
                    entry['decision'],
                    entry['semester'],
                    entry['american'],
                    entry['gpa'],
                    entry['gre'],
                    entry['grev'],
                    entry['greaw'],
                    entry['degree']
                )

            print(row)
            print(taylor)    

            index += 1



        

        


        # Put data in the table
        cur.execute("""
            INSERT INTO %s (
                p_id,
                program,
                comments,
                date_added,
                url,
                status,
                term,
                us_or_international,
                gpa,
                gre,
                gre_v,
                gre_aw,
                degree)
                VALUES ()
                );"""%(name_table, row
                ))






