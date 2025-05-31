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




path_pkl = 'test_25.pkl'

# Check that the file is created and is readable
if os.path.exists(path_pkl):

    # Load in the data from the pickle file
    with open(path_pkl, 'rb') as file:
        data = pickle.load(file)


print('------------------------------------')
print(data[0])

print('------------------------------------')
print(data[1])










