import psycopg



class QueryData:

    def __init__(self):

        self.name_db = 'module3'
        self.name_table = 'applications'
        self.current_term = 'Spring 2025'

        self.conn = psycopg.connect(dbname=self.name_db, user="postgres")
        self.cur = self.conn.cursor()

        # Display all the content from the table at this stage
        self.cur.execute("""
            select * from %s;
            """%(self.name_table))

        # Print outputs
        table_content = self.cur.fetchall()
        print("The table has this content in it: %s"%(table_content))



    def q1(self):

        # Problem 1: How many entries do you have in your database who have applied for Spring 2025?
        text_query = """SELECT *
            FROM %s
            WHERE %s = '%s';
            """%(self.name_table, 'term', self.current_term)

        self.cur.execute(text_query)
        # Print outputs
        output = self.cur.fetchall()
        print("Here's your output: %s"%(len(output)))


    def q2(self):

        # Problem 2: What percentage of entries are from international students (not American or Other) (to two decimal places)?
        text_query = """SELECT 
            %s
            FROM %s;
            """%('us_or_international', self.name_table)

        self.cur.execute(text_query)
        # Print outputs
        output = self.cur.fetchall()
        #print("Here's your output: %s"%(output))


    def q3(self):

        # Problem 3: What is the average GPA, GRE, GRE V, GRE AW of applicants who provide these metrics?
        text_query = """SELECT 
            %s
            FROM %s
            WHERE %s != '-1';
            """%('gpa', self.name_table, 'gpa')

        self.cur.execute(text_query)
        # Print outputs
        gpa = self.cur.fetchall()
        print("Here's your output: %s"%(gpa))

        text_query = """SELECT 
            %s
            FROM %s
            WHERE %s != '-1';
            """%('gre', self.name_table, 'gre')

        self.cur.execute(text_query)
        # Print outputs
        gre = self.cur.fetchall()
        print("Here's your output: %s"%(gre))

        text_query = """SELECT 
            %s
            FROM %s
            WHERE %s != '-1';
            """%('gre_v', self.name_table, 'gre_v')

        self.cur.execute(text_query)
        # Print outputs
        gre_v = self.cur.fetchall()
        print("Here's your output: %s"%(gre_v))

        text_query = """SELECT 
            %s
            FROM %s
            WHERE %s != '-1';
            """%('gre_aw', self.name_table, 'gre_aw')

        self.cur.execute(text_query)
        # Print outputs
        gre_aw = self.cur.fetchall()
        print("Here's your output: %s"%(gre_aw))



    def q4(self):

        # Problem 4: What is their average GPA of American students in Spring 2025?
        text_query = """SELECT 
            %s
            FROM %s
            WHERE %s = 'American' 
            AND %s = '%s';
            """%('gpa', self.name_table, 'us_or_international', 'term', self.current_term)

        self.cur.execute(text_query)
        # Print outputs
        recent_us_gpas = self.cur.fetchall()
        print("Here's your output: %s"%(recent_us_gpas))


    def q5(self):

        # Problem 5: What percent of entries for Spring 2025 are Acceptances (to two decimal places)?
        text_query = """SELECT 
            %s
            FROM %s
            WHERE %s = '%s';
            """%('status', self.name_table, 'term', self.current_term)

        self.cur.execute(text_query)
        # Print outputs
        recent_acceptances = self.cur.fetchall()
        print("Here's your output: %s"%(recent_acceptances))


    def q6(self):

        # Problem 6: What is the average GPA of applicants who applied for Spring 2025 who are Acceptances?
        text_query = """SELECT 
            %s
            FROM %s
            WHERE %s = '%s'
            AND %s = 'Accepted';
            """%('gpa', self.name_table, 'term', self.current_term, 'status')

        self.cur.execute(text_query)
        # Print outputs
        recent_acceptance_gpa = self.cur.fetchall()
        print("Here's your output: %s"%(recent_acceptance_gpa))



    def q7(self):

        # Problem 7: How many entries are from applicants who applied to JHU for a masters degrees in Computer Science?
        text_query = """SELECT 
            %s
            FROM %s
            WHERE %s = '%s'
            AND %s = '%s';
            """%('p_id', self.name_table, 'program', 'JHU', 'degree', 'Masters')

        self.cur.execute(text_query)
        # Print outputs
        hopkins_ms_cs = self.cur.fetchall()
        print("Here's your output: %s"%(hopkins_ms_cs))
















if __name__ == "__main__":

    # Create the query data object
    qd = QueryData()

    # Run all 7 queries
    qd.q1()
    qd.q2()
    qd.q3()
    qd.q4()
    qd.q5()
    qd.q6()
    qd.q7()





