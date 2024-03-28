# import the Flask library
from flask import Flask, render_template, request


# Create the Flask instance and pass the Flask 
# constructor the path of the correct module
app = Flask(__name__)

# The URL 'localhost:5000/square' is mapped to
# view function 'squarenumber'
# The GET request will display the user to enter 
# a number (coming from squarenum.html page)


@app.route('/', methods=['GET'])
def squarenumber():
	# If method is GET, check if number is entered 
	# or user has just requested the page.
	# Calculate the square of number and pass it to 
	# answermaths method
	if request.method == 'GET':
# If 'num' is None, the user has requested page the first time
		if(request.args.get('num') == None):
			return render_template('squarenum.html')
		# If user clicks on Submit button without 
		# entering number display error
		elif(request.args.get('num') == ''):
			return "<html><body> <h1>Invalid number</h1></body></html>"
		else:
		# User has entered a number
		# Fetch the number from args attribute of 
		# request accessing its 'id' from HTML
			number = request.args.get('num')
			sq = int(number) * int(number)
			# pass the result to the answer HTML
			# page using Jinja2 template
			return render_template('answer.html', 
								squareofnum=sq, num=number)

@app.route('/login' , methods=['POST'])
def login():
	if request.method == 'POST':
		Fname = request.form.get('First-Name')
		Lname = request.form.get('Last-Name')

		return render_template('output_login.html' , Fname=Fname , Lname=Lname)
	
@app.route('/login' , methods = ['GET'])
def loginnew():
	if request.method == 'GET':
		return render_template('login.html')
# Start with flask web app with debug as
# True only if this is the starting page 
if(__name__ == "__main__"):
	app.run(debug=True)
