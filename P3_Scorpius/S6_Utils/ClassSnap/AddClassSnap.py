# region Import Packages

import traceback

from P2_Sirius.S1_Models.M1_DataContext.InsertQueryData import InsertQueryData
from P2_Sirius.S1_Models.M1_DataContext.GeneralQuery import GeneralQuery
from P2_Sirius.S1_Models.M1_DataContext.AlchemyEngine import AlchemyEngine

from P3_Scorpius.S4_Logix.H6_ReQuestContent.ReQuestContent import ReQuestContent

# endregion

# region OfficeAdd Class

class OfficeAdd:

    # region Init

    def __init__(self):
            
        self.InsertQueryDatas = InsertQueryData()
        self.ReQuestContents = ReQuestContent()
        self.AlchemyEngines = AlchemyEngine()
        self.GeneralQueries = GeneralQuery()
    
    # endregion
        
    # region Main

    def main(self, **kwargs):

        try:

            self.getVariables(**kwargs)

            self.insertOffice()
        
        except Exception as ex:

            traceback.print_exc()   
            return 400

    # endregion

    # region Get Variables
        
    def getVariables(self, **kwargs):

        self.__userId = kwargs["userId"]
        
        self.__officeName = self.ReQuestContents.form("OfficeName", "str")
        self.__officeManager = self.ReQuestContents.form("OfficeManager", "str")
        self.__officeAddress = self.ReQuestContents.form("OfficeAddress", "str")
        self.__officePhone = self.ReQuestContents.form("OfficePhone", "str")
        self.__officeStatus = int(self.ReQuestContents.form("OfficeStatus", "str"))

    # endregion
        
    # region Insert Office

    def insertOffice(self):

        self.InsertQueryDatas.insertOffice(self.__userId, self.__officeName, self.__officeManager, self.__officeAddress, self.__officePhone, self.__officeStatus, True)
    
    # endregion
    
# endregion