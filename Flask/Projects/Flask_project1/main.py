from flask import Flask,render_template

app = Flask(__name__)

@app.route('/', methods=['POST'])
def handle_data():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')
    print(email)
    print(name)
    print(password)
    return render_template('registration.html')

if __name__ == '__main__':
    app.run(debug=True)