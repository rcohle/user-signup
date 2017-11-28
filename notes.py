OLD MAIN.PY - FROM NOV 28 2:07

from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True


# Show the user the signup form
@app.route('/')
def index():
    # user_name = request.form['user_name']
    # password = request.form['password']
    # verify_password = request.form['verify_password']
    # user_email = request.form['user_email']

#    if len(user_name) < 3 or len(user_name) < 1:
    return render_template('index.html')

# Show the user the Welcome Form when signup is successful
@app.route('/welcome', methods=['POST'])
def welcome():
    user_name = request.form['user_name']
    return render_template('welcome.html', user_name=user_name)


@app.route('/validation', methods=["POST"])
def validation():
    return "Validation Page"
#render_template('validation.html', user_name=user_name, password=password, verify_password=verify_password, user_email=user_email)


app.run()


# If everything passes, redirect the user to the welcome form
# If certain things don't pass, reject and redirect

# user_name = request.form['user_name']
# password = request.form['password']
# verify_password = request.form['verify_password']
# user_email = request.form['user_email']

# error_spaces
# error_characters
# error_empty
# error_no_match

# VALIDATE USER NAME --
#   if any spaces detected, redirect and show error msg NO SPACES
#   if length of entry < 3, redirect and show error msg MUST BE AT LEAST 4 CHARACTERS
#   if field empty, redirect and show error EMPTY
    
# VALIDATE PASSWORD
#   if any spaces detected, redirect and show error msg NO SPACES
#   if length of entry < 3, redirect and show error msg MUST BE AT LEAST 4 CHARACTERS
#   if field empty, redirect and show error EMPTY

# VALIDATE VERIFY PASSWORD
#   if matches password entered, pass
#   if field empty, redirect and show error EMPTY
#   if field does not match password, redirect and show error NO MATCH

# VALIDATE EMAIL (OPTIONAL SUBMISSION FOR USER)
#   if field empty, pass
#   if field contains email, pass 

# If no errors, send to welcome page

