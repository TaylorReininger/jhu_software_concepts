# Module 1

## Assignment

From the homework instructions:

**"This assignment will teach you the fundamentals of website construction. You will construct a
personal developer website that includes a biography, contact information/links, and information
about your python projects. This will give you a chance to both be creative and learn the
fundamentals of website development.
You will practice working with Flask – a micro web framework written in Python. You will also
build upon the html skills taught in module 1, and you will work with cascading style sheets
(CSS) to describe how HTML elements are to be displayed. Your resultant output should be a
functional personal website that includes details about you, your projects, and contact
information."**



## Implementation

- I am using Python==3.12
- I am using Flask as the web framework
- I am using HTML for the page content
- I am using CSS for styling
- I am using Bootstrap for the navigation bar
- I am using inherited templates to keep common themes across pages



## Installation and Execution

NOTE: These instructions assume the user either has Anaconda or another method of creating virtual environments already configured. 

Follow these steps to configure and execut the web app:

1. Create your virtual environment (Anaconda or Pyenv)
```bash
## Anaconda

# Create new Anaconda environment based on Python 3.12 (enter "y" to continue)
conda create -n mod1 python==3.12

# Activate the newly created environment 
conda activate mod1
```

((OR))

```bash
## Pyenv

# Install the latest version of Python 12 for pyenv
pyenv install 3.12.10

# Activate this version of pyenv for use in the next step
pyenv shell 3.12.10

# Create the virtual environment
python -m venv mod1

# Activate the newly created environment
source ./mod1/bin/activate

# Update pip just in case it's on an old version
pip install --upgrade pip
```

2. Navigate to the ```module_1``` folder of this repo
3. Install the dependencies for the app
```bash
# Install all the libraries in the requirements file
pip install -r requirements.txt
```

4. Run the web app
```bash
python run.py
```
5. Open the web app by navigating your browser to the URL printed in the terminal
```bash
# Example URL
http://127.0.0.1:8080
```


An example of the web app in action can be seen [here](./site_screenshots.pdf)




## Resources and Citations

- I followed along with a the course notes from the lecture, the live lecture, and the homework PDF. 
- I found the [Flask quickstart](https://flask.palletsprojects.com/en/stable/quickstart/) guide very helpful for reading about the decorators and the ```__name__``` field at instantiation. 
- I found Tech with Tim had a great tutorial on [using Flask with Bootstrap and template inheritance](https://www.techwithtim.net/tutorials/flask/flask-adding-bootstrap) for a nav bar
- I used [W3 School](https://www.w3schools.com/css) for a ton of CSS references
- I used [coder coder!](https://coder-coder.com/display-divs-side-by-side/) to find a neat trick for doing two divs side by side
- I used Llama3.2 for advice on solving a couple annoying HTML/CSS gremlins (like spans). 