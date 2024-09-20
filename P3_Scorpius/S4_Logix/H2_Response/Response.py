# region Import Packages

from flask import redirect,url_for,flash

from P3_Scorpius.S4_Logix.H4_Message.Message import Message

# endregion

# region Class Response

class Response():

    # region Init Function

    def __init__(self):
        
        self.Messages = Message()

    # endregion

    # region main Function
    
    def main(self,messageCode="201", urlFor="home.page", **kwargs):

        flash(self.Messages.messagesTr[str(messageCode)]["message"])
        return redirect(url_for(urlFor))
        
    # endregion

    def success(self,messageCode="201", urlFor="home.page", **kwargs):

        flash(self.Messages.messagesTr[str(messageCode)]["message"])
        return redirect(url_for(urlFor))

    def error(self,messageCode="401", urlFor="home.page", **kwargs):

        flash(self.Messages.messagesTr[str(messageCode)]["message"])
        return redirect(url_for(urlFor))

# endregion