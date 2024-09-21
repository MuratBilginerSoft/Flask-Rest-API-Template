# region Import Packages

from flask import request

from P3_Scorpius.S1_App.Run.Run import Run

from P3_Scorpius.S4_Logix.H2_Response.Response import Response

# endregion

# region Starter Class

class Starter:

    # region Init
    
    def __init__(self):

        # region Create Objects

        self.Responses = Response()
        self.Runs = Run()

        # endregion

        # region Variables

        self.__requestMethods = ["GET","POST","PATCH","DELETE","PUT", "get","post","patch","delete","put"]

        # endregion

    # endregion

    # region Starter

    def start(self, className, **kwargs):

        if request.method in self.__requestMethods:

            return self.Runs.starter(className, **kwargs)

        else:
            return self.Responses.main("201")

    # endregion

# endregion