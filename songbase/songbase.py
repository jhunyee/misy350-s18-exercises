import os
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

# setup SQLAlchemy use for final project
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
db = SQLAlchemy(app)

#define database tables
class Artist(db.Model):
    __tablename__ = 'artists'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    about = db.Column(db.Text)

class Song(db.Model):
    __tablename__ = 'songs'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256))
    year = db.Column(db.Integer)
    lyrics = db.Column(db.Text)

@app.route('/')
def index():
    #return "hello World"
    return render_template('index.html')

@app.route('/artists')
def all_artists():
    artists = Artist.query.all()
    return render_template('all-artists.html', artists=artists)

@app.route('/form', methods=['GET', 'POST'])
def form():

    if request.method == 'GET':
        #first_name = request.args.get('first_name')
        return render_template('form.html')

    if request.method == 'POST':
        first_name = request.form["first_name"]
        return render_template('form.html', first_name=first_name)

@app.route('/users/<string:username>')
def users(username):
    #return "<h1>hello %s</h1>" % username
    return render_template('user.html', uname=username)

@app.route('/artist/edit/<int:id>')
def artist_edit(id):
    artist = Artist.query.filter_by(id=id).first()
    artist.about = "this is harry wang"
    db.session.commit()

    return "this is artist %d updated" % id
    #return render_template('all-artists.html')



@app.route('/user')
def user():
    return "this is the page for users"


if __name__ == '__main__':
    app.run()
