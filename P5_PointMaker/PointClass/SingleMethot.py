# region Import Packages

import traceback

from P3_Scorpius.S4_Logix.H3_Exception.Exception import Exception
from P3_Scorpius.S5_Session.Session import Session

# endregion

# region YourClassName Class

class YourClassName:

    # region Inıt Function

    def __init__(self):
        
        self.Exceptions = Exception()

    # endregion

    def main(self, method, **kwargs):

        # region Try

        if method == "YourMethod":

            try:
                
                return "YourMessage", 200

            # endregion

            # region Except

            except Exception as e:
                traceback.print_exc()
                return self.Exceptions.mainError("000")

            # endregion
        
        else:
            return self.Exceptions.mainError("000")


#endregion