# OLD MAIN.PY - FROM NOV 28 2:07

# from flask import Flask, request, redirect, render_template
# import cgi
# import os

# app = Flask(__name__)
# app.config['DEBUG'] = True


# # Show the user the signup form
# @app.route('/')
# def index():
#     # user_name = request.form['user_name']
#     # password = request.form['password']
#     # verify_password = request.form['verify_password']
#     # user_email = request.form['user_email']

# #    if len(user_name) < 3 or len(user_name) < 1:
#     return render_template('index.html')

# # Show the user the Welcome Form when signup is successful
# @app.route('/welcome', methods=['POST'])
# def welcome():
#     user_name = request.form['user_name']
#     return render_template('welcome.html', user_name=user_name)


# @app.route('/validation', methods=["POST"])
# def validation():
#     return "Validation Page"
# #render_template('validation.html', user_name=user_name, password=password, verify_password=verify_password, user_email=user_email)


# app.run()


# # If everything passes, redirect the user to the welcome form
# # If certain things don't pass, reject and redirect

# # user_name = request.form['user_name']
# # password = request.form['password']
# # verify_password = request.form['verify_password']
# # user_email = request.form['user_email']

# # error_spaces
# # error_characters
# # error_empty
# # error_no_match

# # VALIDATE USER NAME --
# #   if any spaces detected, redirect and show error msg NO SPACES
# #   if length of entry < 3, redirect and show error msg MUST BE AT LEAST 4 CHARACTERS
# #   if field empty, redirect and show error EMPTY
    
# # VALIDATE PASSWORD
# #   if any spaces detected, redirect and show error msg NO SPACES
# #   if length of entry < 3, redirect and show error msg MUST BE AT LEAST 4 CHARACTERS
# #   if field empty, redirect and show error EMPTY

# # VALIDATE VERIFY PASSWORD
# #   if matches password entered, pass
# #   if field empty, redirect and show error EMPTY
# #   if field does not match password, redirect and show error NO MATCH

# # VALIDATE EMAIL (OPTIONAL SUBMISSION FOR USER)
# #   if field empty, pass
# #   if field contains email, pass 

# # If no errors, send to welcome page
# ------------------------------------------------

# #common to all inputs
# error_empty = 'Empty... please supply requested information'
# error_spaces = 'Sorry, no spaces allowed'
# error_length = 'Please use more than 3 characters and less than 20'

# #unique to password_verify and email inputs
# error_no_match = "Does not match first entry or not between 3 and 20 characters"
# error_symbols = 'Enter a valid email (one "@", one ".", no spaces)'

# @app.route('/')
# def display_signup():
#     return render_template('index.html')

# @app.route('/', methods = ['POST'])
# def validate_username():
#     user_name = request.form['user_name']
#     empty_error_user_name = ''

# def validate_password():
#     password = request.form['password']
#     verify_password = request.form['verify_password']
#     empty_error_password = ''
#     empty_error_verify_password = ''
#     match_error = ''

# def validate_email():
#     user_email = request.form['user_email']
#     empty_error_user_email = ''
#     email_error = ''




# FUNCTIONS OR ERROR RETURNS
# Empty field - username, password+v
# No spaces - username, password+v, email
# More than 3, less than 20 characters - username, password+v, email

# unique:
# password verify no match
# email no @ or . or more than one of error_no_match



#     if user_name == '':
#         empty_error_user_name = 'Empty field...'
#     elif len(user_name) < 3 or len(user_name) > 20:
#         empty_error_user_name = 'Need more than 3 characters, less than 20'
#     elif ' ' in user_name:
#         empty_error_user_name = 'No spaces allowed'

#     if password == '':
#         empty_error_password = 'Empty field...'
#         password = ''
#     elif len(password) < 3 or len(password) > 20:
#         empty_error_password = 'Need more than 3 characters, less than 20'
#         password = ''
#     elif ' ' in password:
#         empty_error_password = 'No spaces allowed'
#         password = ''
#     if password == '':
#         empty_error_verify_password = 'Empty field...'
#         password == ''
#     elif verify_password != password:
#         match_error = "Does not match first entry or not between 3 and 20 characters"
#         password = ''
    
#     if user_email == '':
#         email_error = ''
#     elif ' ' in user_email:
#         email_error = 'No spaces allowed'
#     elif len(user_email) > 0 and len(user_email) < 3 or len(user_email) > 20:
#         email_error = 'Email must be between 3 and 20 characters'
#     elif '@' not in user_email or '.' not in user_email or user_email.count('@') > 1 or user_email.count('.') > 1:
#         email_error = 'Enter a valid email (one "@", one ".", no spaces)'
    


#     if empty_error_user_name == '' and empty_error_password == '' and match_error == '' and empty_error_verify_password == '' and email_error == '':
#         return render_template('welcome.html', user_name=user_name)
#     else:
#         return render_template('index.html', empty_error_user_name=empty_error_user_name, 
#         empty_error_password=empty_error_password, match_error=match_error, 
#         empty_error_verify_password=empty_error_verify_password, user_name=user_name, 
#         user_email=user_email, email_error=email_error, password=password)

# app.run()



# {#
#     begin comment
#     {% extends "base.html" %}
#     {% block content %}
#     {% if user_name > 1 or user_name > 3 %}
#     {% else %}
#     {% endif %}
#     {% if verify_password != password %}
#     {% if " " in user_name %}
#     {% if email}
#     {% endblock %}
#     end comment
# #}