# region Import Package

import traceback

from P2_Sirius.S1_Models.M2_EntityBase.EntityBase import db

# endregion

# region DeleteQuery Class

class DeleteQuery():

    # region Init Function

    def __init__(self):
        
        self.__database =  db
    
    # endregion

    # region deleteGeneral

    def deleteGeneral(self,tableRecords):

        try:
            
            for item in tableRecords:
                self.__database.session.delete(item)

            self.__database.session.commit()

            return 200
        
        except:

            return 400

    # endregion

    # region Delete General

    def deleteGeneralOne(self,tableRecord):

        try:
            self.__database.session.delete(tableRecord)
            self.__database.session.commit()
            return 200

        except Exception:

            traceback.print_exc()
            return 400

    # endregion

    pass
  

# endregion