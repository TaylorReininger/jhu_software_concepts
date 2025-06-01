import json
import os
import time
import pickle
import re

"""
Notes:

We are trying to clean and format the data we scraped. The following fields should be in the 
columns of each list as shown:
- col1 = University
- col2 = Program name & degree level
- col3 = Date added
- col4 = Decision date
- col5 = Junk from the additional options (throw away)
- col6 = Semester, International/American, GPA, GRE scores (not all applicable for every entry)
- col7 = OPTIONAL: notes


Program Design:

class Clean
    
    def _load_pickle()

    def _clean_row()

    def clean_data()
    
    def load_data()

    def save_data()


"""





class Clean:
    
    def __init__(self):
        self.data_clean = None
        self.data_raw = None


    def _load_pickle(self, path_pkl: str) -> None:

        # Check that the file exists
        if os.path.exists(path_pkl):

            # Load in the data from the pickle file
            with open(path_pkl, 'rb') as file:
                self.data_raw = pickle.load(file)

        else:
            print('WARNING: File does not exist')

    def _clean_row(self, row: str):

        # All rows should have 6 or 7 columns. If not, something is wrong
        if len(row) < 6 or len(row) > 7:
            print('WARNING: Bad row length of ' + str(len(row)))

        # Create a dictionary to store the cleaned data
        cleaned = {}

        # The university does not require cleaning
        cleaned['university'] = row[0]

        # The major and degree are together, separated by '\n' characters
        degree = row[1].split('\n')
        cleaned['major'] = degree[0]
        cleaned['degree'] = degree[-1]

        # The date added does not require cleaning
        cleaned['date_entry'] = row[2]

        # The decision outcome and date
        decision = row[3].split('on')
        cleaned['decision'] = decision[0].strip()
        cleaned['date_decision'] = decision[1].strip()

        # The details are all in row 6 and is very unreliable. Using regex to find content if it exists
        details = row[5].split('\n')

        # The semester is reliably the 2nd column
        cleaned['semester'] = details[1]

        # Look for GPA
        gpa = re.search('^GPA [0-9]*\.[0.9]+*')

        # Check for "International" or "American"
        if 'International' in details:
            cleaned['american'] = False
        elif 'American' in details:
            cleaned['american'] = True
        else:
            cleaned['american'] = None


        gre = re.search('GRE \d+')
        grev = re.search('GRE V \d+')
        greaw = re.search('GRE AW \d+')


        print(row)
        x = 1



        return True

    def clean_data(self, path_pkl):
    
        self._load_pickle(path_pkl)

        for row in self.data_raw:

            cleaned = self._clean_row(row)
    
        
    def load_data(self):
        pass
    def save_data(self):
        pass





if __name__ == "__main__":

    path_pkl = 'test_25.pkl'


    c = Clean()
    c.clean_data(path_pkl)








