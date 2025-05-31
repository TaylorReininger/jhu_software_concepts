from bs4 import BeautifulSoup
from urllib import parse
from urllib.request import urlopen
import json


import os
import time
import pickle


"""
Notes:

We are trying to scrape the following fields from the gradcafe site. Some come from the 
survey page (the list of entries), some come from the "more" details page, and some can
be found on both. 
- Program name (both)
- University (both)
- Comments (survey)
- Date of Info Added to Grad Cafe (survey)
- URL link to applicant entry (both)
- Applicant Status (both)
    - Acceptance Date (if applicable) (survey)
    - Rejection Date (if applicable) (survey)
- Semester and Year of Program Start (if available) (survey)
- International (if available) (both)
- GRE Scores (both)
- Masters or PhD (both)
- GPA (both)


The URL for the survey page is:
https://www.thegradcafe.com/survey/

The URL of the application page is:
https://www.thegradcafe.com/result/<ID>

"""



# Base URL
url = "https://www.thegradcafe.com/survey/"

# Save location of raw HTML
path_html = 'html.pkl'

# If it's not already saved off, pull the data from the web
# otherwise, load in the saved version
if os.path.exists(path_html):

    print('LOADING')
    # Load in the data from the pickle file
    with open(path_html, 'rb') as file:
        html = pickle.load(file)

else:

    print('SCRAPING')

    # Create a URL object
    page = urlopen(url)

    # Read the web page and convert it to html
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")

    # Write the HTML to file for future use to reduce page hits
    with open(path_html, 'wb') as file:
        pickle.dump(html, file)


# Use beautiful soup to parse the HTML
soup = BeautifulSoup(html, "html.parser")

# From the survey page, load in the whole table
table_body = soup.find('tbody')


# Extract the data of interest from the table
rows = table_body.find_all('tr')

# Initialize some lists for extracting the tabular data
this_page_data = []
curr_line = []

# Parese each row in the table
for row in rows:

    # This finds an individual row from the table and turns it into a list
    this_row = row.find_all('td')
    this_row = [cell.text.strip() for cell in this_row]

    # This takes care of blank lines that sometimes make it into the table
    if this_row[0] == '':
        continue

    # If this row is not a header, keep building onto the previous list
    if row.attrs and 'class' in row.attrs.keys():
        curr_line.extend(this_row)

    # If this row is a header, store the previously built row list and start a new one
    else:
        this_page_data.append(curr_line)
        curr_line = this_row
        
# Make sure to catch the last row we were building
this_page_data.append(curr_line)


# Sanity check:
for r in this_page_data:
    print('-----------------------------------------------------')
    print(r)
    print(len(r))




