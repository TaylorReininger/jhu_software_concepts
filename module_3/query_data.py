import psycopg



class QueryData:

    def __init__(self, name_db='module3'):
        """
        Initializes the class with some class members
        """

        # Database name, table name, and the current term
        self.name_db = name_db
        self.name_table = 'applications'
        self.current_term = 'Fall 2025'

        # Create a database connection and get a cursor
        self.conn = psycopg.connect(dbname=self.name_db, user="postgres")
        self.cur = self.conn.cursor()

        # Peek at the data in the database
        self.cur.execute("""
            select * from %s;
            """%(self.name_table))
        table_content = self.cur.fetchall()
        self.num_rows = len(table_content)

        # Ensure that data exists in this database
        if self.num_rows < 1:
            print('WARNING: Table is empty')


    def q1(self):
        """
        Answers question 1
        """

        # Problem 1: How many entries do you have in your database who have applied for Spring 2025?
        # Get data from db
        text_query = """SELECT *
            FROM %s
            WHERE %s = '%s';
            """%(self.name_table, 'term', self.current_term)

        self.cur.execute(text_query)
        # Print outputs
        output = self.cur.fetchall()
        answer = len(output)
        print("Here's your output: %s"%(answer))

        # Returns to user
        return answer


    def q2(self):
        """
        Answers question 2
        """

        # Problem 2: What percentage of entries are from international students (not American or Other) (to two decimal places)?
        # Get data from db
        text_query = """SELECT 
            %s
            FROM %s
            WHERE %s = '%s';
            """%('us_or_international', self.name_table, 'us_or_international', 'false')

        self.cur.execute(text_query)
        output = self.cur.fetchall()

        # Calculate percentage
        percentage = ((10000*len(output))//(self.num_rows))/100
        print("Here's your output: %5.2f"%(percentage))

        # Returns to user
        return percentage


    def q3(self):
        """
        Answers question 3
        """

        # Problem 3: What is the average GPA, GRE, GRE V, GRE AW of applicants who provide these metrics?
        # Get data from db
        text_query = """SELECT 
            %s
            FROM %s
            WHERE %s != '-1';
            """%('gpa', self.name_table, 'gpa')

        self.cur.execute(text_query)
        gpa = self.cur.fetchall()

        # Process GPA information to calculate the average
        if len(gpa) > 1:
            av_gpa = sum([a[0] for a in gpa])/len(gpa)
        else:
            av_gpa = -1
        print("Here's your output: %s"%(av_gpa))


        # Get data from db
        text_query = """SELECT 
            %s
            FROM %s
            WHERE %s != '-1';
            """%('gre', self.name_table, 'gre')
        self.cur.execute(text_query)
        gre = self.cur.fetchall()

        # Process GRE information to calculate the average
        if len(gre) > 1:
            av_gre = sum([a[0] for a in gre])/len(gre)
        else:
            av_gre = -1
        print("Here's your output: %s"%(av_gre))


        # Get data from db
        text_query = """SELECT 
            %s
            FROM %s
            WHERE %s != '-1';
            """%('gre_v', self.name_table, 'gre_v')
        self.cur.execute(text_query)
        gre_v = self.cur.fetchall()

        # Process GRE V information to calculate the average
        if len(gre_v) > 1:
            av_gre_v = sum([a[0] for a in gre_v])/len(gre_v)
        else:
            av_gre_v = -1
        print("Here's your output: %s"%(av_gre_v))


        # Get data from db
        text_query = """SELECT 
            %s
            FROM %s
            WHERE %s != '-1';
            """%('gre_aw', self.name_table, 'gre_aw')

        self.cur.execute(text_query)
        gre_aw = self.cur.fetchall()

        # Process GRE AW information to calculate the average
        if len(gre_aw) > 1:
            av_gre_aw = sum([a[0] for a in gre_aw])/len(gre_aw)
        else:
            av_gre_aw = -1
        print("Here's your output: %s"%(av_gre_aw))

        # Returns all 4 values to user
        return av_gpa, av_gre, av_gre_v, av_gre_aw


    def q4(self):
        """
        Answers question 4
        """

        # Problem 4: What is their average GPA of American students in Spring 2025?
        # Get data from db
        text_query = """SELECT 
            %s
            FROM %s
            WHERE %s = 'true' 
            AND %s = '%s';
            """%('gpa', self.name_table, 'us_or_international', 'term', self.current_term)
        self.cur.execute(text_query)
        recent_us_gpas = self.cur.fetchall()

        # Process recent US GPA data
        recent_us_gpas = [v[0] for v in recent_us_gpas if v[0] >= 0]
        sum_gpas = 0
        if len(recent_us_gpas) > 1:
            sum_gpas = sum(recent_us_gpas)
            av_us = sum_gpas/len(recent_us_gpas)
        else:
            av_us = -1
        print("Here's your output: %s"%(av_us))

        # Returns to user
        return av_us


    def q5(self):
        """
        Answers question 5
        """

        # Problem 5: What percent of entries for Spring 2025 are Acceptances (to two decimal places)?
        # Get data from db
        text_query = """SELECT 
            %s
            FROM %s
            WHERE %s = '%s';
            """%('status', self.name_table, 'term', self.current_term)
        self.cur.execute(text_query)
        decisions = self.cur.fetchall()

        # Process recent acceptance data
        count_acc = 0
        if len(decisions) > 1:
            for a in decisions:
                if a[0] == 'Accepted':
                    count_acc += 1
            ratio = count_acc/len(decisions)
            recent_acc_percentage = round(10000*ratio)/100

        else:
            recent_acc_percentage = -1

        print("Here's your output: %s"%(recent_acc_percentage))

        # Returns to user
        return recent_acc_percentage


    def q6(self):
        """
        Answers question 6
        """
        # Problem 6: What is the average GPA of applicants who applied for Spring 2025 who are Acceptances?
        # Get data from db
        text_query = """SELECT 
            %s
            FROM %s
            WHERE %s = '%s'
            AND %s = 'Accepted';
            """%('gpa', self.name_table, 'term', self.current_term, 'status')
        self.cur.execute(text_query)
        recent_acceptance_gpa = self.cur.fetchall()

        # Process recent acceptance GPA data
        recent_acceptance_gpa = [v[0] for v in recent_acceptance_gpa if v[0] >= 0]
        if len(recent_acceptance_gpa) > 1:
            av_gpa_acc = sum(recent_acceptance_gpa)/len(recent_acceptance_gpa)
        else:
            av_gpa_acc = -1

        print("Here's your output: %s"%(av_gpa_acc))

        # Returns to user
        return av_gpa_acc



    def q7(self):
        """
        Answers question 6
        """

        # Problem 7: How many entries are from applicants who applied to JHU for a masters degrees in Computer Science?
        # Get data from db
        text_query = """SELECT 
            %s
            FROM %s
            WHERE %s = '%s'
            AND %s = '%s';
            """%('p_id', self.name_table, 'program', 'JHU', 'degree', 'Masters')
        self.cur.execute(text_query)
        
        # Process Hopkins CS MS data
        num_hopkins_ms_cs = len(self.cur.fetchall())
        print("Here's your output: %s"%(num_hopkins_ms_cs))

        # Returns to user
        return num_hopkins_ms_cs


if __name__ == "__main__":

    # Create the query data object
    qd = QueryData('module3')

    # Run all 7 queries
    qd.q1()
    qd.q2()
    qd.q3()
    qd.q4()
    qd.q5()
    qd.q6()
    qd.q7()





