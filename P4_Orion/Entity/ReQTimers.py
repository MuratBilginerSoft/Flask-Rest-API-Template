# region Import Lib

from App.A3_ModelBase import *

# endregion

# region ReQTimers Table

class ReQTimers(BaseModel, db.Model):

    __tablename__ = "reqtimers"

    Id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    UserId = db.Column(db.String(300))
    SessionId = db.Column(db.String(300))
    FunctionName = db.Column(db.String(100))
    StartTime = db.Column(db.String(30))
    EndTime = db.Column(db.String(30))
    CompletionTime = db.Column(db.Float())
    Status = db.Column(db.String(10))
    CreatedBy = db.Column(db.String(300))
    CreatedAt = db.Column(db.String(30))
    ChangedBy = db.Column(db.String(300))
    ChangedAt = db.Column(db.String(30))
    Revision = db.Column(db.Integer)
    DeleteFlag = db.Column(db.Integer)

    def __init__(self, UserId, SessionId, FunctionName, StartTime, EndTime, CompletionTime, Status, CreatedBy, CreatedAt, ChangedBy, ChangedAt, Revision, DeleteFlag):

        self.UserId = UserId
        self.SessionId = SessionId
        self.FunctionName = FunctionName
        self.StartTime = StartTime
        self.EndTime = EndTime
        self.CompletionTime = CompletionTime
        self.Status = Status
        self.CreatedBy = CreatedBy
        self.CreatedAt = CreatedAt
        self.ChangedBy = ChangedBy
        self.ChangedAt = ChangedAt
        self.Revision = Revision
        self.DeleteFlag = DeleteFlag


# endregion
