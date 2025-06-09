
from flask import Flask, render_template
from query_data import QueryData


# Create Web Server Gateway Interface (WSGI) application by instantiating a 
# Flask object
web_app = Flask(__name__)


# Use the route() decorator to define which URL triggers the function.
@web_app.route("/")
# Custom function to display web content (can use HTML syntax here if desired)
def index():


    # Get the statistics from the database
    qd = QueryData()

    # Run all 7 queries and format the answers
    answer1 = 'Application Count = %d'%(qd.q1())
    answer2 = 'Percent International = %5.2f'%(qd.q2())
    gparevaw = qd.q3()
    answer3 = 'Average GPA = %3.2f,  Average GRE = %5.2f,  Average GRE V = %5.2f,  Average GRE AW = %3.2f'%(gparevaw[:])
    answer4 = 'Average American GPA = %3.2f'%(qd.q4())
    answer5 = 'Acceptance Percentage = %5.2f'%(qd.q5())
    answer6 = 'Average GPA of Accepted = %3.2f'%(qd.q6())
    answer7 = 'Number of JHU Masters in Computer Science Entries = %d'%(qd.q7())

    # Create the index html file and pass all the variables into it
    return render_template('index.html', 
        ans1 = answer1,
        ans2 = answer2,
        ans3 = answer3,
        ans4 = answer4,
        ans5 = answer5,
        ans6 = answer6,
        ans7 = answer7)


# Run the webapp with appropriate IP and port values
if __name__ == '__main__':
    web_app.run(host='0.0.0.0', port=8080)    