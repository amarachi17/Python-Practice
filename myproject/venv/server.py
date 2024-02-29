from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

print(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        name = data['name']
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{name}, {email}, {subject}, {message}')

def write_to_csv(data):
    with open('database.csv', mode='a') as database2:
        name = data['name']
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',', newline='', quotechar=',', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name, email, subject, message])

@app.route('/submit_form', methods=['POST','GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        # write_to_file(data)
        write_to_csv(data)
        # print(data)
        return redirect('/thankyou.html')
    else:
        return 'Something went wrong. Try again'


    # return "Form Submitted Hurray!!!!!"



# @app.route('/')
# def hello_world():
#     return render_template('index.html')

# @app.route('/contact.html')
# def contact():
#     return render_template('contact.html')
# @app.route('/index.html')
# def index():
#     return render_template('index.html')


# @app.route('/blog')
# def blog():
#     return 'These are my thoughts on blogs'

# @app.route('/blog/2023/dogs')
# def blog2():
#     return 'I love my tolls'

# set FLASK_APP=server.py
# flask run
# cd venv
# flask run server
# web server python server.py


# Python is a server site programming language
# The difference between server site and customer programming language
# Learn design concepts
# Learn firebase or sqlite 
# Docker, Gitlab, circe ci, aws, microsoft azure, devOps, jest, 
# Road map for development