from flask import Flask, render_template
app = Flask(__name__)

@app.route('/result')
def result():
	dict = {'phy':56,'maths':45,'chem':67}
	return render_template('result.html', result = dict)

if __name__ == '__main__':
	app.run(debug=True)

