# region Import Packages

import traceback
from flask import render_template, redirect, url_for, flash, request, Response

from P3_Scorpius.S1_App.Router.RouteUrl import RouteUrl

from P3_Scorpius.S4_Logix.H2_Response.Response import Response
from P3_Scorpius.S4_Logix.H3_Exception.Exception import Exception
from P3_Scorpius.S4_Logix.H4_Message.Message import Message
from P3_Scorpius.S4_Logix.H5_GetDate.GetDate import GetDate
from P3_Scorpius.S4_Logix.H6_ReQuestContent.ReQuestContent import ReQuestContent

from P3_Scorpius.S6_Utils.Mapping.Configuration import Configuration

from P3_Scorpius.S3_HeroKit.HeroKit import HeroKit

from P2_Sirius.S1_Models.M1_DataContext.InsertQueryData import InsertQueryData
from P2_Sirius.S1_Models.M1_DataContext.AlchemyEngine import AlchemyEngine
from P2_Sirius.S1_Models.M1_DataContext.GeneralQuery import GeneralQuery

from P3_Scorpius.S5_Session.Session import Session

# endregion

# region SignUp Class

class ConfirmPage:

    # region Init Function

    def __init__(self):

        # region Create Object

        self.InsertQueryDatas = InsertQueryData()
        self.ReQuestContents = ReQuestContent()
        self.AlchemyEngines = AlchemyEngine()
        self.GeneralQueries = GeneralQuery()
        self.Exceptions = Exception() 
        self.Responses = Response()
        self.Messages = Message()
        self.GetDates = GetDate()
        self.HeroKits = HeroKit()
        
        # endregion

        # region Class Variables

        self.__userId = None

        # endregion

    # endregion
    
    # region Main
        
    def main(self, urlName, method, **kwargs):

        self.__urlName = urlName

        if method == "GET":
            return self.get(**kwargs)
        
        elif method == "POST":
            return self.post(**kwargs)

        else:
            return self.Responses.main("000", urlFor="home.page")
    
    # endregion

    #region Get Function

    def get(self,**kwargs):

        try:

            self.AlchemyEngines.closeEngine()
            return render_template(RouteUrl().routeUrl[self.__urlName])

        except Exception as e:
            traceback.print_exc()
            return self.Responses.error(412, self.__class__)

    #endregion

    # region Post Function

    def post(self,**kwargs):

        try:

            self.AlchemyEngines.closeEngine()
            return self.Responses.main("000", urlFor="home.page")

        except Exception as e:

            traceback.print_exc()
            return self.Responses.error("412", urlFor="home.page")

    # endregion

    # region Logix
    
    # region Get Variables
        
    def getVariables(self, **kwargs):
        
        pass
    
    # endregion

    # endregion
        
    # region Data Manipulation
        
    # endregion
        

#endregion
