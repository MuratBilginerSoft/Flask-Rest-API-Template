# region Import Packages

import traceback

from flask import Flask
from flask_mail import Mail, Message

from P3_Scorpius.S6_Utils.Mapping.Configuration import Configuration

# endregion

# region MailSender Class

class MailSender:

    # region Init

    def __init__(self):

        self.__messages = None
        self.__mail = None
        self.__app = None

    # endregion

    # region Starter

    def starter(self, email, title, htmlContent):

        try:

            self.createMailSender()
            self.sender(email, title, htmlContent)

            return 200

        except Exception:

            traceback.print_exc()
            return 400

    # endregion

    # region Logix Algorithm

    # region Create Mail Sender

    def createMailSender(self):

        self.__app = Flask(__name__)

        self.setMailConfig()
        
        self.__mail = Mail(self.__app)
        self.__mail.init_app(self.__app)
    
    # endregion

    # region Set Mail Config

    def setMailConfig(self):

        self.__app.config['MAIL_SERVER'] = str(Configuration.mailConfig["server"])
        self.__app.config['MAIL_USERNAME'] = str(Configuration.mailConfig["email"])
        self.__app.config['MAIL_PASSWORD'] = str(Configuration.mailConfig["password"])
        self.__app.config['MAIL_PORT'] = int(Configuration.mailConfig["port"])
        self.__app.config['MAIL_DEFAULT_SENDER'] = str(Configuration.mailConfig["email"])
        self.__app.config['MAIL_ASCII_ATTACHMENTS'] = False
        self.__app.config['MAIL_MAX_EMAILS'] = None
        self.__app.config['MAIL_USE_SSL'] = True
        self.__app.config['MAIL_TESTING'] = False
        self.__app.config['MAIL_USE_TLS'] = False
        
    # endregion

    # region Sender

    def sender(self, email, title, htmlContent):

        self.__messages = Message(title, sender=str(Configuration.mailConfig["email"]), recipients=[email])
        self.__messages.html = htmlContent
        self.__mail.send(self.__messages)
        
    # endregion

    # endregion
    
# endregion