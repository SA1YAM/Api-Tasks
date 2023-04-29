import os
import sys

current = os.path.dirname(os.path.realpath(__file__))
#print(current)

parentt = os.path.dirname(current)
#print(parentt)

parent = os.path.dirname(parentt)
#print(parent)

sys.path.append(parent)
sys.path.append(parentt)



from flask_sqlalchemy import SQLAlchemy 
from flask_login import UserMixin 

# instantiationg the SQLAlchemy object
db = SQLAlchemy() 
        
# defing the user model for database
class Event(db.Model, UserMixin):
    __tablename__ = 'event'
    id = db.Column(db.Integer(), primary_key = True, autoincrement = True)
    type = db.Column(db.String(), nullable = False)
    uid = db.Column(db.Integer(), nullable = False)
    name = db.Column(db.String(), nullable = False)
    tagline = db.Column(db.String(), nullable = False)
    schedule = db.Column(db.DateTime(), nullable = False)
    description = db.Column(db.String(), nullable = False)
    image = db.Column(db.LargeBinary(), nullable = False)
    moderator = db.Column(db.String(), nullable = False)
    category = db.Column(db.String(), nullable = False)
    sub_category = db.Column(db.String(), nullable = False)
    rigor_rank = db.Column(db.String(), nullable = False)
    attendees = db.relationship('User', backref = 'event', cascade = "all, delete", lazy = True)
    
 #defining the appointment model for database   
class User(db.Model):
    __tablename__ = 'user'
    user_id = db.Column(db.Integer(), primary_key = True, autoincrement = True)
    username = db.Column(db.String(), unique = True, nullable = False)
    event_id = db.Column(db.Integer(), db.ForeignKey('event.id'), nullable = False)
