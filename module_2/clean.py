import json
import os
import time
import pickle

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








