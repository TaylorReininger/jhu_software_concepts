import json
import psycopg
import datetime

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


class LoadData:

    def __init__(self, name_json=None, name_db='module3'):
        """
        Initializes the LoadData object and stores class members
        """

        # Stores class members
        # The JSON file path to load in
        if not name_json:
            self.name_json = './application_data.json'
        else:
            self.name_json = name_json
        # The name of the existing database to write to
        self.name_db = 'module3'
        # The name of the table to write the data into within the database
        self.name_table = 'applications'


    def load(self):
        """
        Loads all the data from the JSON file into the database
        """

        # Extract class members
        name_json = self.name_json
        name_db = self.name_db
        name_table = self.name_table

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

                    # Extract this entry from the JSON data and get the entry ID
                    entry = data[index]
                    p_id = int(index)

                    # Handle optional fields
                    if entry['notes']:
                        notes = entry['notes']
                    else:
                        notes = 'None'

                    if entry['gpa']:
                        gpa = '%3.2f'%(float(entry['gpa']))
                    else:
                        gpa = '-1'

                    if entry['gre']:
                        gre = '%5.2f'%(float(entry['gre']))
                    else:
                        gre = '-1'

                    if entry['grev']:
                        grev = '%5.2f'%(float(entry['grev']))
                    else:
                        grev = '-1'

                    if entry['greaw']:
                        greaw = '%5.2f'%(float(entry['greaw']))
                    else:
                        greaw = '-1'

                    # Fix the date format
                    date_str = entry['date_entry']
                    formatted_date = datetime.datetime.strptime(date_str, "%B %d, %Y").strftime("%Y-%m-%d")

                    # Create a parameterized SQL query
                    command = """
                        INSERT INTO applications (
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
                        VALUES (%(p_id)s, %(program)s, %(comments)s, %(date_added)s, %(url)s, %(status)s, %(term)s, %(us_or_international)s, 
                        %(gpa)s, %(gre)s, %(gre_v)s, %(gre_aw)s, %(degree)s);
                    """

                    # Prepare a dictionary of values to insert
                    values = {
                        'p_id': p_id,
                        'program': entry['major'],
                        'comments': notes,
                        'date_added': formatted_date,
                        'url': entry['url'],
                        'status': entry['decision'],
                        'term': entry['semester'],
                        'us_or_international': entry['american'],
                        'gpa': gpa,
                        'gre': gre,
                        'gre_v': grev,
                        'gre_aw': greaw,
                        'degree': entry['degree']
                    }

                    # Execute the query with a dictionary of values
                    cur.execute(command, values)


                # Display all the content from the table at this stage
                cur.execute("""
                    select * from %s;
                    """%(name_table))

                # Print outputs
                table_content = cur.fetchall()
                print("The table now has %d rows in it"%(len(table_content)))

                # Commit the changes to the table
                conn.commit()


    def delete_table(self):

        """
        Deletes a table from the database (handy for clearing old entries while debuggin)
        """
        # Extract class members
        name_db = self.name_db
        name_table = self.name_table

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
                if matches[0]:
                    print('Deleting table')
                    # Drop the table (replace 'table_name' with your actual table name)
                    cur.execute("""DROP TABLE %s;"""%(name_table))
                    # Commit the changes to the table
                    conn.commit()



if __name__ == "__main__":

    # Create the load data object
    ld = LoadData(name_json = '../module_2/application_data.json', name_db='module3')
    # Clear any existing tables before populating
    ld.delete_table()
    # Load all the data into a the database
    ld.load()




