# region Import Packages

from App.A3_ModelBase import *

# endregion

# region Users Table

class Users(BaseModel, db.Model):

    __tablename__ = "users"

    Id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    UserId = db.Column(db.String(300), unique=True)
    Email = db.Column(db.String(100), unique=True)
    Name = db.Column(db.String(30))
    Surname = db.Column(db.String(30))
    Company = db.Column(db.String(100))
    Role = db.Column(db.String(100))
    ImagePath = db.Column(db.String(500))
    CreatedBy = db.Column(db.String(300))
    CreatedAt = db.Column(db.String(30))
    ChangedBy = db.Column(db.String(300))
    ChangedAt = db.Column(db.String(30))
    Revision = db.Column(db.Integer)
    DeleteFlag = db.Column(db.Integer)

    def __init__(self, UserId, Email, Name, Surname, Company, Role, ImagePath, CreatedBy, CreatedAt, ChangedBy, ChangedAt, Revision, DeleteFlag):

        self.UserId = UserId
        self.Email = Email
        self.Name = Name
        self.Surname = Surname
        self.Company = Company
        self.Role = Role
        self.ImagePath = ImagePath
        self.CreatedBy = CreatedBy
        self.CreatedAt = CreatedAt
        self.ChangedBy = ChangedBy
        self.ChangedAt = ChangedAt
        self.Revision = Revision
        self.DeleteFlag = DeleteFlag

# endregion
