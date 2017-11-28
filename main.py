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

@app.route('/welcome', methods=['POST'])
def welcome():
    user_name = request.form['user_name']
    return render_template('welcome.html', user_name=user_name)

app.run()