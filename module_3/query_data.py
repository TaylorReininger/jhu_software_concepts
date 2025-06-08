import psycopg



class QueryData:

    def __init__(self):

        self.name_db = 'module3'
        self.name_table = 'applications'
        self.current_term = 'Fall 2025'

        self.conn = psycopg.connect(dbname=self.name_db, user="postgres")
        self.cur = self.conn.cursor()

        # Display all the content from the table at this stage
        self.cur.execute("""
            select * from %s;
            """%(self.name_table))

        # Print outputs
        table_content = self.cur.fetchall()
        #print("The table has this content in it: %s"%(table_content))
        self.num_rows = len(table_content)
        if self.num_rows < 1:
            print('WARNING: Table is empty')


    def q1(self):

        # Problem 1: How many entries do you have in your database who have applied for Spring 2025?
        text_query = """SELECT *
            FROM %s
            WHERE %s = '%s';
            """%(self.name_table, 'term', self.current_term)

        self.cur.execute(text_query)
        # Print outputs
        output = self.cur.fetchall()
        answer = len(output)
        print("Here's your output: %s"%(answer))
        return answer


    def q2(self):

        # Problem 2: What percentage of entries are from international students (not American or Other) (to two decimal places)?
        text_query = """SELECT 
            %s
            FROM %s
            WHERE %s = '%s';
            """%('us_or_international', self.name_table, 'us_or_international', 'false')

        self.cur.execute(text_query)
        # Print outputs
        output = self.cur.fetchall()

        percentage = ((10000*len(output))//(self.num_rows))/100
        print("Here's your output: %5.2f"%(percentage))
        return percentage


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

        if len(gpa) > 1:
            av_gpa = sum([a[0] for a in gpa])/len(gpa)
        else:
            av_gpa = -1
        print("Here's your output: %s"%(av_gpa))

        text_query = """SELECT 
            %s
            FROM %s
            WHERE %s != '-1';
            """%('gre', self.name_table, 'gre')

        self.cur.execute(text_query)
        # Print outputs
        gre = self.cur.fetchall()
        if len(gre) > 1:
            av_gre = sum([a[0] for a in gre])/len(gre)
        else:
            av_gre = -1
        print("Here's your output: %s"%(av_gre))

        text_query = """SELECT 
            %s
            FROM %s
            WHERE %s != '-1';
            """%('gre_v', self.name_table, 'gre_v')

        self.cur.execute(text_query)
        # Print outputs
        gre_v = self.cur.fetchall()
        if len(gre_v) > 1:
            av_gre_v = sum([a[0] for a in gre_v])/len(gre_v)
        else:
            av_gre_v = -1
        print("Here's your output: %s"%(av_gre_v))

        text_query = """SELECT 
            %s
            FROM %s
            WHERE %s != '-1';
            """%('gre_aw', self.name_table, 'gre_aw')

        self.cur.execute(text_query)
        # Print outputs
        gre_aw = self.cur.fetchall()
        if len(gre_aw) > 1:
            av_gre_aw = sum([a[0] for a in gre_aw])/len(gre_aw)
        else:
            av_gre_aw = -1
        print("Here's your output: %s"%(av_gre_aw))

        return av_gpa, av_gre, av_gre_v, av_gre_aw



    def q4(self):

        # Problem 4: What is their average GPA of American students in Spring 2025?
        text_query = """SELECT 
            %s
            FROM %s
            WHERE %s = 'true' 
            AND %s = '%s';
            """%('gpa', self.name_table, 'us_or_international', 'term', self.current_term)

        self.cur.execute(text_query)
        # Print outputs
        recent_us_gpas = self.cur.fetchall()
        recent_us_gpas = [v[0] for v in recent_us_gpas if v[0] >= 0]
        sum_gpas = 0
        if len(recent_us_gpas) > 1:
            for g in recent_us_gpas:
                sum_gpas += g

            av_us = sum_gpas/len(recent_us_gpas)
        else:
            av_us = -1

        print("Here's your output: %s"%(av_us))

        return av_us


    def q5(self):

        # Problem 5: What percent of entries for Spring 2025 are Acceptances (to two decimal places)?
        text_query = """SELECT 
            %s
            FROM %s
            WHERE %s = '%s';
            """%('status', self.name_table, 'term', self.current_term)

        self.cur.execute(text_query)
        # Print outputs
        decisions = self.cur.fetchall()
        
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

        return recent_acc_percentage


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
        recent_acceptance_gpa = [v[0] for v in recent_acceptance_gpa if v[0] >= 0]

        if len(recent_acceptance_gpa) > 1:
            av_gpa_acc = sum(recent_acceptance_gpa)/len(recent_acceptance_gpa)
        else:
            av_gpa_acc = -1

        print("Here's your output: %s"%(av_gpa_acc))

        return av_gpa_acc



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
        num_hopkins_ms_cs = len(self.cur.fetchall())
        print("Here's your output: %s"%(num_hopkins_ms_cs))

        return num_hopkins_ms_cs


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





