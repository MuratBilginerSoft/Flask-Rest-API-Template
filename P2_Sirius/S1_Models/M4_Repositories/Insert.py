# region Import Package

import traceback

from P2_Sirius.S1_Models.M2_EntityBase.EntityBase import db

# endregion

#region InsertQuery Class

class InsertQuery():

    # region Init Function

    def __init__(self):
        
        self.__database =  db
    
    # endregion

   # region General Insert

    def generalInsert(self, tableName):

        # region Try

        try:
            self.__database.session.add_all(tableName)
            self.__database.session.commit()

            return 200

        # endregion

        # region Except

        except Exception:

            traceback.print_exc()
            return 400
        
        # endregion

    # endregion

    pass

#endregion