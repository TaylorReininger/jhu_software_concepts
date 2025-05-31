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


Program Design:

class Scrape
    def scrape_grad_cafe()

    def save_data()


"""




class Scrape:

    def __init__(self):
        
        # Base URL
        self.url = "https://www.thegradcafe.com/survey/"
        self.num_entries = 0
        self.data = []

    
    def _scrape_page(self, url: str) -> list:
        
        # Create a URL object
        page = urlopen(url)

        # Read the web page and convert it to html
        html_bytes = page.read()
        html = html_bytes.decode("utf-8")


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

        return this_page_data


    def _save_data(self, path_pkl: str) -> None:

        # Write the HTML to file for future use to reduce page hits
        with open(path_pkl, 'wb') as file:
            pickle.dump(self.data, file)


    def scrape_grad_cafe(self, num_apps: int, save_path: str) -> None:
        
        # Ensure that we don't overwrite existing pkl files
        if os.path.exists(save_path):
            print('WARNING: The specified filename already exists.')
            print('Please delete it or choose another name, then try again')
            return

        # Go through as many pages as needed to meet our desired number of entries
        index_page = 1
        while self.num_entries < num_apps:

            # Create URL for individual pages on the site
            url_this_page = 'https://www.thegradcafe.com/survey/?page='+str(index_page)
            # Scrape the individual page
            this_data = self._scrape_page(url_this_page)
            # Store this page's data in our list
            self.data.extend(this_data)
            # Update the number of entries we've scraped and the page we're on
            self.num_entries += len(this_data)
            index_page += 1

        # Save off the data as a pickle file
        self._save_data(save_path)




if __name__ == "__main__":
    
    # Create scrape object
    s = Scrape()

    # Call the method to scrape with the desired input parameters
    path_pkl = 'test_25.pkl'
    s.scrape_grad_cafe(25, path_pkl)

    # Check that the file is created and is readable
    if os.path.exists(path_pkl):

        # Load in the data from the pickle file
        with open(path_pkl, 'rb') as file:
            stuff = pickle.load(file)

        print(len(stuff))
