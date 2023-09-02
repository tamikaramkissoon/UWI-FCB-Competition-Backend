from App.database import db

class TaskRiskAssessment(db.model):
    __tablename__ = 'task_risk_assessments'
    taskRiskAssessmentId = db.Column(db.Integer, primary_key=True)
    assessmentName = db.Column(db.String,nullable=False)
    assessmentDetails = db.Column(db.String)
    taskId = db.Column(db.Integer, db.ForeignKey('tasks.taskId'))
    
    # many-to-one relationship with Task
    task = db.relationship('Task', back_populates='taskRiskAssessments')


    def __init__(self,taskRiskAssessmentId,assessmentName, assessmentDetails, taskId):
        self.taskRiskAssessmentId = taskRiskAssessmentId
        self.assessmentName = assessmentName
        self.assessmentDetails = assessmentDetails
        self.taskId = taskId

    def get_json(self):
        return{
            'id': self.taskRiskAssessmentId,
            'name': self.assessmentName,
            'description':self.assessmentDetails,
            'task': self.task.taskName
        }
