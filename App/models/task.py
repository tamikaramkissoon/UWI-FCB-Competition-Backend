from App.database import db

class Task(db.model):
    __tablename__ = 'tasks'
    taskId = db.Column(db.Integer, primary_key=True)
    taskName = db.Column(db.String,nullable=False)
    taskDescription = db.Column(db.String)
    stageId = db.Column(db.Integer, db.ForeignKey('stages.stageId'))
    
    # many-to-one relationship with Stage
    stage = db.relationship('Stage', back_populates='tasks')
    
    # one-to-many relationship with TaskRiskAssessment
    taskRiskAssessments = db.relationship('TaskRiskAssessment', back_populates='task')


    def __init__(self, taskId, taskName, taskDescription, stageId):
        self.taskId = taskId
        self.taskName = taskName
        self.taskDescription = taskDescription
        self.stageId = stageId


    def get_json(self):
        return{
            'id': self.taskId,
            'name': self.taskName,
            'description':self.taskDescription,
            'stage': self.stage.stageName,
            'taskRiskAssessments': self.taskRiskAssessments.assessmentName
        }   