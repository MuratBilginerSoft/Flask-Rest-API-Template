# region Import Lib

from App.A3_ModelBase import *

# endregion

# region ResetPasswords Table

class ResetPasswords(BaseModel, db.Model):

    __tablename__ = "resetpasswords"

    Id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    UserId = db.Column(db.String(300))
    Email = db.Column(db.String(100))
    Token = db.Column(db.String(300))
    Status = db.Column(db.Integer)
    CreatedBy = db.Column(db.String(300))
    CreatedAt = db.Column(db.String(30))
    ChangedBy = db.Column(db.String(300))
    ChangedAt = db.Column(db.String(30))
    Revision = db.Column(db.Integer)
    DeleteFlag = db.Column(db.Integer)

    def __init__(self, UserId, Email, Token, Status, CreatedBy, CreatedAt, ChangedBy, ChangedAt, Revision, DeleteFlag):

        self.UserId = UserId
        self.Email = Email
        self.Token = Token
        self.Status = Status
        self.CreatedBy = CreatedBy
        self.CreatedAt = CreatedAt
        self.ChangedBy = ChangedBy
        self.ChangedAt = ChangedAt
        self.Revision = Revision
        self.DeleteFlag = DeleteFlag

# endregion
