# region Import Packages

from flask import request, redirect, url_for
import traceback
import sys

from P2_Sirius.S1_Models.M1_DataContext.AlchemyEngine import AlchemyEngine

from P3_Scorpius.S1_App.Router.EndPointClass import EndPointClass
from P3_Scorpius.S1_App.Router.RoutePages import *
from P3_Scorpius.S5_Session.Session import Session

# endregion

# region Run Class

class Run():

    # region Inıt Function

    def __init__(self) -> None:
        
        self.AlchemyEngines = AlchemyEngine()

    # endregion

    def starter(self, className, urlName, **kwargs):

        try:

            userId =  Session.userId
            self.AlchemyEngines.createEngine()
            self.AlchemyEngines.snapEngine()

            methot = request.method.upper()
            className = str(EndPointClass.endpointClass[className][methot])
            classOne = getattr(sys.modules[__name__], className)()

            
            return classOne.main(urlName, methot, userId = userId, **kwargs)
        
        except:
            traceback.print_exc()
            return redirect(url_for("home.page"))
 
# endregion


