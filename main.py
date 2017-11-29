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
    password = request.form['password']
    user_email = request.form['user_email']
    verify_password = request.form['verify_password']
    user_email = request.form['user_email']
    empty_error_user_name = ''
    empty_error_password = ''
    empty_error_user_email = ''
    match_error = ''
    empty_error_verify_password = ''
    email_error = ''
    

    if user_name == '':
        empty_error_user_name = 'Empty field...'
    elif len(user_name) < 3 or len(user_name) > 20:
        empty_error_user_name = 'Need more than 3 characters, less than 20'
    else:
        if ' ' in user_name:
            empty_error_user_name = 'No spaces allowed'

    if password == '':
        empty_error_password = 'Empty field...'
        password = ''
    elif len(password) < 3 or len(password) > 20:
        empty_error_password = 'Need more than 3 characters, less than 20'
        password = ''
    else:
        if ' ' in password:
            empty_error_password = 'No spaces allowed'
            password = ''

    if password == '':
        empty_error_verify_password = 'Empty field...'
        password == ''
    elif verify_password != password:
        match_error = "Does not match first entry or too few/too many characters"
        password = ''

    if user_email == '':
        email_error = ''
    elif ' ' in user_email:
        email_error = 'No spaces allowed'
    elif len(user_email) > 0 and len(user_email) < 3 or len(user_email) > 20:
        email_error = 'Email must be between 3 and 20 characters'
    elif '@' or '.' not in user_email:
        email_error = 'Email needs 1 "@" and 1 "." in the entry'
    

    if empty_error_user_name == '' and empty_error_password == '' and match_error == '' and empty_error_verify_password == '' and email_error == '':
        return render_template('welcome.html', user_name=user_name)
    else:
        return render_template('index.html', empty_error_user_name=empty_error_user_name, 
        empty_error_password=empty_error_password, match_error=match_error, 
        empty_error_verify_password=empty_error_verify_password, user_name=user_name, 
        user_email=user_email, email_error=email_error, password=password)

app.run()
