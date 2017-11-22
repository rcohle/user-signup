from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True


# Show the user the signup form
@app.route('/')
def index():
    return render_template('index.html')

# If everything passes, redirect the user to the welcome form

# If certain things don't pass, reject and redirect

#


#....
#@app.route('/welcome', methods=['POST'])
#def welcome():
#    user_name = request.form['user_name']
#    return render_template('welcome.html', user_name=user_name)

app.run()