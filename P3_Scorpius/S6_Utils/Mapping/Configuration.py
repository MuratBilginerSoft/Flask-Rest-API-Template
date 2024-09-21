# region Import Packages

import os

# endregion


# region Configuration Class

class Configuration:

    # region App Config

    appConfig = {
        
        "staticFolder"      : "P1_Assets",
        "secretKey"         : "FlaskTemplate",
        "userFolderPath"    : os.path.join(os.getcwd(),"P1_Assets","Users"),
        "appPort"           : 6001,
        "rootUrl" : "http://localhost:6001",
    }

    # endregion

    # region FolderNames

    folderNames ={

        "Log" : "Log",
        "Temp"    : "Temp",
        "Image"   : "Image",
    }

    # endregion

    # region Mail Config

    # endregion
    
    # region DatabaseConfig

    dbConfig = {
        
        "dbType": "MySQL",
        "database": "devdb",
        "host": "prowthdb.mysql.database.azure.com",
        "user": "muratbilginer",
        "password": "Tj_G{z=<4$'3qg-#",
        "port": "3306",
        "dbUrl" : None
    }

    # endregion

    # region Mail Config

    mailConfig = {

        "email"     : "mbilginer@brainytech.net",
        "password"  : "nqybvwitviwpefnw",
        "server"    : "smtp.yandex.com.tr",
        "port"      : 465,
    }

    # endregion

    # region ClassConfig

    classConfig = {

        "confirmMailTitle" : "CheckerMan E-Mail Onaylama",
        "confirmMailUrlSuffix" : "auth/confirm-mail/{}",
    }

    # endregion

    # endregion

# endregion

