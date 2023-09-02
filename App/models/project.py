from App.database import db

class Project(db.model):
    __tablename__ = 'projects'
    projectId = db.Column(db.Integer, primary_key=True)
    projectName = db.Column(db.String, nullable=False)
    projectDescription = db.Column(db.String)
    
    # one-to-many relationship with Stage
    stages = db.relationship('Stage', back_populates='project')
    
    # one-to-many relationship with User
    userId = db.Column(db.Integer, db.ForeignKey('users.userId'),nullable=False)
    user = db.relationship('User', back_populates='projects')

    def __init__(self, projectId, projectName, projectDescription, userId):
        self.projectId = projectId
        self.projectName = projectName
        self.projectDescription = projectDescription
        self.userId = userId

    def get_json(self):
        return{
            'id': self.projectId,
            'name': self.projectName,
            'description':self.projectDescription,
            'username': self.user.username
        }
    

        