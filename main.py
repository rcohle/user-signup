from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True


# Show the user the signup form
@app.route('/')
def display_signup():
    return render_template('index.html')

# display form AND any errors
@app.route('/', methods = ['POST'])
def validate_signup():
    #gets info from user's submission in form
    user_name = request.form['user_name']
    empty_error = ''

    if user_name == '':
        empty_error = 'Empty field...'
        user_name = ''
    elif len(user_name) < 3:
        empty_error = 'Need more than 3 characters'
        user_name = ''
    else:
        if ' ' in user_name:
            empty_error = 'No spaces allowed'
            user_name = ''
    
    if empty_error == '':
        return render_template('welcome.html', user_name=user_name)
    else:
        return render_template('index.html', empty_error=empty_error, user_name=user_name)

app.run()
