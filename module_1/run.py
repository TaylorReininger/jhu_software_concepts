
from flask import Flask, render_template


# Create Web Server Gateway Interface (WSGI) application by instantiating a 
# Flask object
web_app = Flask(__name__)


# Use the route() decorator to define which URL triggers the function.
@web_app.route("/")
# Custom function to display web content (can use HTML syntax here if desired)
def index():
    # This is my landing page
    return render_template('index.html', curr_page='index')


# This is my contact page
@web_app.route("/contact/")
def contact():
    return render_template('contact.html', curr_page='contact')


# This is my projects page
@web_app.route("/projects/")
def projects():
    return render_template('projects.html', curr_page='projects')


# Run the webapp with appropriate IP and port values
if __name__ == '__main__':
    web_app.run(host='0.0.0.0', port=8080)    