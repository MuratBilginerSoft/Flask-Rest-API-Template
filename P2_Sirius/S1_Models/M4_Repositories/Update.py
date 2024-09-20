# region Import Packages

import traceback
import datetime as dt

from P2_Sirius.S1_Models.M2_EntityBase.EntityBase import db

# endregion

# region UpdateQuery

class UpdateQuery():

    # region Init Function

    def __init__(self):
        
        self.__database = db
        self.__date = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # endregion

    # region General Update

    def generalUpdate(self,tableRecord,**kwargs):

        try:
            if tableRecord:

                for k,v in kwargs.items():

                    setattr(tableRecord,k,v)
                
                tableRecord.Revizyon = tableRecord.Revizyon + 1
                tableRecord.DeğiştirmeTarihi = self.__date
                
                self.__database.session.commit()

                return 200
            else:
                return 400

        except:
        
            return 400

    # endregion

    # region updateSignInWithToken()

    def updateSignInWithToken(self, tableRecord):

        try:
            if tableRecord:

                tableRecord.ConfirmStatus = 1
                self.__database.session.commit()

                return 200
            else:
                return 400

        except Exception:

            traceback.print_exc()
            return 400
            
    # endregion

    # region updateUser

    def updateUser(self, tableRecord,**kwargs):

        try:
            if tableRecord:

                tableRecord.Name = kwargs["name"]
                tableRecord.LastName = kwargs["lastName"]
                tableRecord.Phone = kwargs["phone"]
                tableRecord.UserPhotoName = kwargs["userPhotoName"]
                tableRecord.UserPhotoUrl = kwargs["userPhotoUrl"]
                tableRecord.Biography = kwargs["biography"]
                tableRecord.Birthday = kwargs["birthday"]
                tableRecord.UpdateAt = kwargs["updateAt"]
                tableRecord.Revision = tableRecord.Revision + 1
                
                self.__database.session.commit()

                return 200
            else:
                return 400

        except Exception:

            traceback.print_exc()
            return 400
            
    # endregion

    pass

#endregion