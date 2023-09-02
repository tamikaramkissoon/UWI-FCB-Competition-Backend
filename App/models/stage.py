from App.database import db

class Stage(db.model):
    __tablename__ = 'stages'
    stageId = db.Column(db.Integer, primary_key=True)
    stageName = db.Column(db.String,nullable=False)
    stageDescription = db.Column(db.String)
    projectId = db.Column(db.Integer, db.ForeignKey('projects.projectId'))
    
    # many-to-one relationship with Project
    project = db.relationship('Project', back_populates='stages')
    
    # one-to-many relationship with Task
    tasks = db.relationship('Task', back_populates='stage')


    def __init__ (self, stageId, stageName, stageDescription, projectId ):
        self.stageId = stageId
        self.stageName = stageName
        self.stageDescription = stageDescription
        self.projectId = projectId


    def get_json(self):
        return{
            'id': self.stageId,
            'name': self.stageName,
            'description':self.stageDescription,
            'project': self.project.projectName,
            'task': self.tasks.taskName
        }

