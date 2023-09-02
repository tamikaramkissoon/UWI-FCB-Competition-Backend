from App.database import db

class UserProject(db.model):
    __tablename__ = 'user_project'
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, db.ForeignKey('users.userId'))
    projectId = db.Column(db.Integer, db.ForeignKey('projects.projectId'))
    
    # many-to-one relationship with User
    user = db.relationship('User', back_populates='userProjects')
    
    # many-to-one relationship with Project
    project = db.relationship('Project')

    def __init__(self, id, userId, ProjectId):
        self.id = id
        self.userId = userId
        self.projectId = ProjectId


    def get_json(self):
        return{
            'id': self.id,
            'user': self.user.username,
            'project':self.project.projectName
        }
