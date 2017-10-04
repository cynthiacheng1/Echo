
from flask import Flask, render_template, request

site = Flask(__name__)

@site.route('/')
def root():
	return render_template("form.html")

@site.route('/result', methods=['POST', 'GET'])
def result():
	name = 'blah'
	if request.method == 'POST':
		name = request.form['name']
	else:
		name = request.args['name']
	return render_template("result.html", input = name, method = request.method)

if __name__ == '__main__':
    site.debug = True
    site.run()