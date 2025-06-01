import json
import os
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
        # Store the cleaned data in a dictionary
        self.data_clean = {}
        # Load the raw data in as a list
        self.data_raw = []


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
        gpa = re.search('GPA [0-9]+.[0-9]+', row[5])
        if gpa:
            # Extract the GPA score
            gpa_score = re.search('[0-9]+.[0-9]+', gpa.group(0))
            cleaned['gpa'] = gpa_score.group(0)
        else:
            cleaned['gpa'] = None
        

        # Check for "International" or "American"
        if 'International' in details:
            cleaned['american'] = False
        elif 'American' in details:
            cleaned['american'] = True
        else:
            cleaned['american'] = None

        # Search for a GRE score
        gre = re.search('GRE [0-9]+', row[5])
        if gre:
            # Extract the GRE score
            gre_score = re.search('[0-9]+', gre.group(0))
            cleaned['gre'] = gre_score.group(0)
        else:
            cleaned['gre'] = None
        
        # Search for a GRE V score
        grev = re.search('GRE V [0-9]+', row[5])
        if grev:
            # Extract the GRE V score
            grev_score = re.search('[0-9]+', grev.group(0))
            cleaned['grev'] = grev_score.group(0)
        else:
            cleaned['grev'] = None
        
        # Search for GRE AW score
        greaw = re.search('GRE AW [0-9]+.[0-9]+', row[5])
        if greaw:
            # Extract the GRE AW score
            greaw_score = re.search('[0-9]+.[0-9]+', greaw.group(0))
            cleaned['greaw'] = greaw_score.group(0)
        else:
            cleaned['greaw'] = None
        
        # Extract comments if applicable
        if len(row) >= 7:
            # Remove this weird newline thing that shows up sometimes
            cleaned['notes'] = row[6].replace('\r\n\r\n', ' ').replace('\r\n', ' ')
        else:
            cleaned['notes'] = None

        # Return the cleaned dictionary
        return cleaned



    def clean_data(self, path_pkl: str):
    
        # Load in the data we scraped from the web
        self._load_pickle(path_pkl)

        # Clean each entry and store it in a dictionary
        index_entry = 0
        for row in self.data_raw:
            cleaned = self._clean_row(row)
            self.data_clean[index_entry] = cleaned
            index_entry += 1
        

    def load_data(self, path_json: str):

        # Check that the file exists
        if os.path.exists(path_json):

            # Read the data in from a JSON file and store in the class member
            with open(path_json, 'r') as file:
                self.data_clean = json.load(file)

        else:
            print('WARNING: File does not exist')



    def save_data(self, path_json: str):

        # Write the data out in a JSON file
        with open(path_json, 'w') as file:
            # Dump to file, set indent and ascii settings
            json.dump(self.data_clean, file, indent=4, sort_keys=False, ensure_ascii=False)




if __name__ == "__main__":

    path_pkl = 'test_10k.pkl'


    c = Clean()
    c.clean_data(path_pkl)

    path_json = 'clean_10k.json'
    c.save_data(path_json)

    c2 = Clean()
    c2.load_data(path_json)

    # Display stats
    stats = "Cleaned %d entries"%(len(c2.data_clean.keys()))
    print(stats)







