from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db

class User(db.Model):
    __tablename__ = 'users'
    userId = db.Column(db.Integer, primary_key=True)
    username =  db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
 
    # one-to-many relationship with Project
    userProjects = db.relationship('UserProject', back_populates='user')

    def __init__(self, username, password, email):
        self.username = username
        self.set_password(password)
        self.email = email


    def get_json(self):
        return{
            'id': self.userId,
            'username': self.username,
            'email':self.email
        }

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password, method='sha256')
    
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

