
from flask import Flask, render_template


# Create Web Server Gateway Interface (WSGI) application by instantiating a 
# Flask object
web_app = Flask(__name__)


# Use the route() decorator to define which URL triggers the function.
@web_app.route("/")
# Custom function to display web content (can use HTML syntax here if desired)
def index():
    # This is my landing page
    return render_template('index.html', 
        ans1 = 'Blah blah blah',
        ans2 = 'Blah blah blah',
        ans3 = 'Blah blah blah',
        ans4 = 'Blah blah blah',
        ans5 = 'Blah blah blah',
        ans6 = 'Blah blah blah',
        ans7 = 'Blah blah blah')


# Run the webapp with appropriate IP and port values
if __name__ == '__main__':
    web_app.run(host='0.0.0.0', port=8080, debug=True)    