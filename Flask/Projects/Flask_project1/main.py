from flask import Flask,render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def handle_data():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')
    return render_template('registration.html')

if __name__ == '__main__':
    app.run(debug=True)