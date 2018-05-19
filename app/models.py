from . import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),unique = True, index=True)
    hash_pass = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True, index = True)
    profile_pic_path = db.Column(db.String(255))
    bio = db.Column(db.String(255))

    pitches = db.relationship('Pitch',backref='user',lazy='dynamic')

    @property
    def password(self):
        raise AttributeError("You cannot read password attribute")

    @password.setter
    def password(self,password):
        self.hash_pass = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.hash_pass,password)
    
    def __repr__(self):
        return f'User {self.username}'

class Category(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer,primary_key = True)
    categ = db.Column(db.String(255))

    pitches = db.relationship('Pitch',backref='category',lazy='dynamic')

    def save_category(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'Category {self.categ}'

class Pitch(db.Model):
    __tablename__ = 'pitches'

    id = db.Column(db.Integer,primary_key = True)
    pitch_content = db.Column(db.String())
    category_id = db.Column(db.Integer,db.ForeignKey('categories.id'))
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))

    def save_pitch(self):
        db.session.add(self)
        db.session.commit()
    
    @classmethod
    def get_pitch(cls,id):
        pitches = Pitch.query.filter_by(id=id).all()
        return pitches