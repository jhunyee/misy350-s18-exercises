from flask_script import Manager
from songbase import app, db, Artist

manager = Manager(app)

@manager.command
def deploy():
    print "resetting database..."
    db.drop_all()
    db.create_all()

    print "inserting initial data..."
    coldplay = Artist(name="coldplay", about="this is coldplay")
    maroon5 = Artist(name="maroon 5", about="this is maroon 5")
    db.session.add(coldplay)
    db.session.add(maroon5)

    db.session.commit()

if __name__ == '__main__':
    manager.run()
