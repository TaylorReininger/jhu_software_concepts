
from flask import Flask



# Create Web Server Gateway Interface (WSGI) application by instantiating a 
# Flask object
web_app = Flask(__name__)


# Use the route() decorator to define which URL triggers the function.
@web_app.route("/")
# Custom function to display web content (can use HTML syntax here if desired)
def hello_world():
    return "Hello, World! My name is Taylor"


# Run the webapp with appropriate IP and port values
if __name__ == '__main__':
    web_app.run(host='0.0.0.0', port=8080)    