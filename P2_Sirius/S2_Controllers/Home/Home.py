# region Import Packages

from flask import render_template

import traceback

from P3_Scorpius.S4_Logix.H3_Exception.Exception import Exception
from P3_Scorpius.S5_Session.Session import Session

# endregion

# region Index Class

class Home:

    # region Inıt Function

    def __init__(self):
        
        self.Exceptions = Exception()

    # endregion

    def main(self, urlName, method, **kwargs):

        # region Try

        try:
            
            return "Success", 200

        # endregion

        # region Except

        except Exception as e:
            traceback.print_exc()
            return self.Exceptions.mainError("000")

        # endregion

#endregion


