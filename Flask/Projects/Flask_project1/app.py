from flask import Flask, request, redirect
from flask.templating import render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, migrate

app = Flask(__name__)
app.debug = True

# adding configuration for using a sqlite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

# Creating an SQLAlchemy instance
db = SQLAlchemy(app)

# Settings for migrations
migrate = Migrate(app, db)

# Models
class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=False, nullable=False)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f"Name : {self.name}, Username: {self.username}"

@app.route('/')
def index(): 
    profiles = Profile.query.all()
    return render_template('index.html', profiles=profiles)


@app.route('/add_data')
def add_data():
    return render_template('add_profile.html')

@app.route('/delete/<int:id>')
def erase(id):
    # Deletes the data on the basis of unique id and
    # redirects to home page
    data = Profile.query.get(id)
    db.session.delete(data)
    db.session.commit()
    return redirect('/')

# function to add profiles
@app.route('/add', methods=["POST"])
def profile():
    
    # In this function we will input data from the
    # form page and store it in our database.
    # Remember that inside the get the name should
    # exactly be the same as that in the html
    # input fields
    name = request.form.get("name")
    username = request.form.get("username")
    password = request.form.get("password")

    # create an object of the Profile class of models
    # and store data as a  row in our datatable
    if name != '' and username != '' and password != '':
        p = Profile(name=name, username=username, password=password)
        db.session.add(p)
        db.session.commit()
        return redirect('/')
    else:
        return redirect('/')


if __name__ == '__main__':
    app.run()
