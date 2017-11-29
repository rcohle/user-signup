    # Import necessary stuffs
from flask import Flask, request, redirect, render_template
import cgi
import os

    # Set up necessary stuffs
app = Flask(__name__)
app.config['DEBUG'] = True

    # Show the user the signup form
@app.route('/')
def display_signup():
    return render_template('index.html')
    # display form and input errors

@app.route('/', methods = ['POST'])
def validate_signup():

        # error messages for failed validation
    error_empty = 'Empty... please supply requested information'
    error_spaces = 'Sorry, no spaces allowed'
    error_length = 'Please use more than 3 characters and less than 20'
    error_no_match = "Does not match first entry or not between 3 and 20 characters"
    error_symbols = 'Enter a valid email (one "@", one ".", no spaces)'

        # user_name validation
    user_name = request.form['user_name']
    empty_error_user_name = ''
    if user_name == '':
        empty_error_user_name = error_empty
    elif len(user_name) < 3 or len(user_name) > 20:
        empty_error_user_name = error_length
    elif ' ' in user_name:
        empty_error_user_name = error_spaces

        # password validation
    password = request.form['password']
    empty_error_password = ''

    if password == '':
        empty_error_password = error_empty
        password = ''
    elif len(password) < 3 or len(password) > 20:
        empty_error_password = error_length
        password = ''
    elif ' ' in password:
        empty_error_password = error_spaces
        password = ''

        # verify_password validation
    verify_password = request.form['verify_password']
    match_error = ''
    empty_error_verify_password = ''

    if password == '':
        empty_error_verify_password = error_empty
        password == ''
    elif verify_password != password:
        match_error = error_no_match
        password = ''

        # user_email validation
    user_email = request.form['user_email']
    empty_error_user_email = ''
    email_error = ''

    if user_email == '':
        email_error = ''
    elif ' ' in user_email:
        email_error =error_spaces
    elif len(user_email) > 0 and len(user_email) < 3 or len(user_email) > 20:
        email_error = error_length
    elif '@' not in user_email or '.' not in user_email or user_email.count('@') > 1 or user_email.count('.') > 1:
        email_error = error_symbols

        # successful validation result
    if empty_error_user_name == '' and empty_error_password == '' and match_error == '' and empty_error_verify_password == '' and email_error == '':
        return render_template('welcome.html', user_name=user_name)

        # failed validation result
    else:
        return render_template('index.html', empty_error_user_name=empty_error_user_name, 
        empty_error_password=empty_error_password, match_error=match_error, 
        empty_error_verify_password=empty_error_verify_password, user_name=user_name, 
        user_email=user_email, email_error=email_error, password=password)

app.run()