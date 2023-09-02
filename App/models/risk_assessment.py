from App.database import db

class RiskAssessment(db.model):
    __tablename__ = 'risk_assessments'
    riskAssessmentId = db.Column(db.Integer, primary_key=True)
    assessmentName = db.Column(db.String,nullable=False)
    assessmentDescription = db.Column(db.String)
    projectId = db.Column(db.Integer, db.ForeignKey('projects.projectId'))
    
    # one-to-one relationship with Project
    project = db.relationship('Project', back_populates='riskAssessment')

    def __init__(self,riskAssessmentId, assessmentName, assessmentDescription, projectId):
        self.riskAssessmentId = riskAssessmentId
        self.assessmentName = assessmentName
        self.assessmentDescription = assessmentDescription
        self.projectId = projectId
    

    def get_json(self):
        return{
            'id': self.riskAssessmentId,
            'name': self.assessmentName,
            'description':self.assessmentDescription,
            'project': self.project.projectName
        }