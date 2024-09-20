# region Import Packages

from flask import redirect, url_for, flash
import traceback

from P3_Scorpius.S4_Logix.H4_Message.Message import Message

# endregion

# Exception Class

class Exception:

    # region Init Function
    
    def __init__(self):

        self.Messages = Message()

    # endregion

    # region Main Error Function

    def mainError(self,messageCode, urlFor="error.noneAuth", **kwargs):

        traceback.print_exc()

        flash(self.Messages.messagesTr[str(messageCode)]["message"])
        return redirect(url_for(urlFor))
    
    # endregion

# endregion