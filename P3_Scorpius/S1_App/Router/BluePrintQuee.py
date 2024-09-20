# region Import Packages

from flask import Blueprint

from P3_Scorpius.S1_App.Starter.Starter import Starter

# endregion

# region BluePrintQuee

class BluePrintQuee():

    # region Init Function

    def __init__(self, bluePrintName):

        self.Starters = Starter()
        self.BluePrintBps = Blueprint(bluePrintName, __name__)

        self.__requestMethods = ["GET","POST","PATCH","DELETE","PUT", "get","post","patch","delete","put"]
    
    # endregion
        
    # region Create BluePrint

    def createBluePrint(self, bluePrintName, endPointName, className, urlName, **kwargs):
        @self.BluePrintBps.route(f"{endPointName}", methods=self.__requestMethods)
        def page(id = None, productId = None, token=None):

            return self.Starters.start(className, urlName,bluePrintName=bluePrintName, id=id, productId=productId, token=token, **kwargs)

    # endregion

# endregion