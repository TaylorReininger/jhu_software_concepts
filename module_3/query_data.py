import psycopg












name_db = 'module3'
name_table = 'applications'




# Connect to a postgresql server (must follow steps from above)
with psycopg.connect(dbname=name_db, user="postgres") as conn:


    # Open a cursor to perform database operations
    with conn.cursor() as cur:
    
        # Display all the content from the table at this stage
        cur.execute("""
            select * from %s;
            """%(name_table))

        # Print outputs
        table_content = cur.fetchall()
        #print("The table has this content in it: %s"%(table_content))


        # Problem 1: How many entries do you have in your database who have applied for Fall 2024?
        text_query = """SELECT *
            FROM %s
            WHERE %s = '%s';
            """%(name_table, 'term', 'Spring 2025')

        cur.execute(text_query)
        # Print outputs
        output = cur.fetchall()
        #print("Here's your output: %s"%(len(output)))


        # Problem 2: What percentage of entries are from international students (not American or Other) (to two decimal places)?
        text_query = """SELECT 
            %s
            FROM %s;
            """%('us_or_international', name_table)

        cur.execute(text_query)
        # Print outputs
        output = cur.fetchall()
        #print("Here's your output: %s"%(output))


        # Problem 3: What is the average GPA, GRE, GRE V, GRE AW of applicants who provide these metrics?
        text_query = """SELECT 
            %s
            FROM %s
            WHERE %s != '-1';
            """%('gpa', name_table, 'gpa')

        cur.execute(text_query)
        # Print outputs
        gpa = cur.fetchall()
        print("Here's your output: %s"%(gpa))

        text_query = """SELECT 
            %s
            FROM %s
            WHERE %s != '-1';
            """%('gre', name_table, 'gre')

        cur.execute(text_query)
        # Print outputs
        gre = cur.fetchall()
        print("Here's your output: %s"%(gre))

        text_query = """SELECT 
            %s
            FROM %s
            WHERE %s != '-1';
            """%('gre_v', name_table, 'gre_v')

        cur.execute(text_query)
        # Print outputs
        gre_v = cur.fetchall()
        print("Here's your output: %s"%(gre_v))

        text_query = """SELECT 
            %s
            FROM %s
            WHERE %s != '-1';
            """%('gre_aw', name_table, 'gre_aw')

        cur.execute(text_query)
        # Print outputs
        gre_aw = cur.fetchall()
        print("Here's your output: %s"%(gre_aw))










