# region Import Packages

import random
import uuid
import time
import re
import os

from itsdangerous import URLSafeTimedSerializer
from passlib.hash import sha256_crypt

from P3_Scorpius.S4_Logix.H5_GetDate.GetDate import GetDate

from P3_Scorpius.S5_Session.Session import Session

from P3_Scorpius.S6_Utils.Mapping.Configuration import Configuration

# endregion

# region HeroKit Class

class HeroKit:

    # region Init

    def __init__(self):

        self.GetDates = GetDate()

        self.__userFolderPath = Configuration.appConfig["userFolderPath"]

        self.__date = self.GetDates.currentDate()
        
    # endregion
    
    # region Set Db Url
        
    def setDbUrl(self, databaseType, databaseName, host=None, userName=None, password=None):

        dbUrl = None

        if databaseType == "SQLite":

            dbUrl = self.dbUrl = 'sqlite:///{}'.format(databaseName)

        elif databaseType == "MySQL":

            dbUrl = 'mysql+pymysql://{user}:{pw}@{url}/{db}'.format(user=userName, pw=password, url=host, db=databaseName)
    
        return dbUrl
        
    # endregion

    # region Create SignIn Id

    def createSignInId(self):

        now = str(time.time()) + str(random.randint(1, 1000000))
        return uuid.uuid3(uuid.NAMESPACE_DNS, now)

    # endregion

    # region Create User Id

    def createUserId(self, email):

        return str(uuid.uuid3(uuid.NAMESPACE_DNS, email))

    # endregion

    # region Create InstanceId

    def createInstanceId(self):

        return str(uuid.uuid3(uuid.NAMESPACE_DNS, self.__date))

    # endregion

    # region Create Token

    def createToken(self, email):

        safeUrl = URLSafeTimedSerializer(email)
        token = safeUrl.dumps(email, salt=email)

        return token

    # endregion

    # region Encrypt Password

    def encryptPassword(self, password):

        return sha256_crypt.encrypt(password)
    
    # endregion

    # region Password Check

    def passwordCheck(self, password, authPassword):

        return sha256_crypt.verify(password, authPassword)

    # endregion

    # region Set Sessions

    def setSessions(self, email=None, userId="Test"):

        Session.signInId = self.createSignInId()
        Session.email = email

        if userId is None or userId == "Test":
            Session.userId = self.createSignInId()
        else:
            Session.userId = userId

    # endregion
    
    # region Set Dynamic Folder Path

    def setDynamicFolderPath(self, userId, FolderName):

        userIdFolderPath = os.path.join(self.__userFolderPath, userId)
        dynamicFolderPath = os.path.join(userIdFolderPath, FolderName)

        return dynamicFolderPath
    
    # endregion

    # region Set Core Folder Path
    
    def setCoreFolderPath(self, userId):

        userIdFolderPath = os.path.join(self.__userFolderPath, userId)
        datasetFolderPath = os.path.join(userIdFolderPath, "Dataset")
        resultFolderPath = os.path.join(userIdFolderPath, "Result")
        tempFolderPath = os.path.join(userIdFolderPath, "Temp")
        
        return datasetFolderPath, resultFolderPath, tempFolderPath
    
    # endregion

    # region Set All Folder Path
    
    def setAllFolderPath(self, userId):

        userIdFolderPath = os.path.join(self.__userFolderPath, userId)
        logFolderPath = os.path.join(userIdFolderPath, "Log")
        imageFolderPath = os.path.join(userIdFolderPath, "Image")
        
        return userIdFolderPath, logFolderPath, imageFolderPath
    
    # endregion

    # region Set Url Path

    def setUrlPath(self, className, classTrName, classDetail=None):

        if className == "company":
            listUrlPath = f"/dashboard/companies"

        else:
            listUrlPath = f"/dashboard/{className}s"

        addUrlPath = f"/dashboard/{className}/add"
        listButtonTitle = f"{classTrName} Listesi"
        detailButtonTitle = f"Güncelle"

        pathUpdate = f"/dashboard/{className}/update"
        pathDelete = f"/dashboard/{className}/delete"
        pathDetail = f"/dashboard/{className}/detail"

        pathSubDetail = f"/dashboard/{classDetail}"

        return addUrlPath, listUrlPath, listButtonTitle, pathUpdate, pathDelete, pathDetail, pathSubDetail, detailButtonTitle

    # endregion

    # region Set Filter Data

    def setFilterData(self, dataList=[], filterSearchDataStatus=False,  filterSearchDataColumnName=None, filterSearchDataDisplayName=None, filterRadioButtonStatus = False, filterRadioButtonColumnName = None, filterRadioButtonDisplayName = None, tableModalStatus = False):

        filterDDStatus = filterSearchDataStatus
        filterRBStatus = filterRadioButtonStatus

        if filterDDStatus == True:

            filterDDColumnData = [item[str(filterSearchDataColumnName)] for item in dataList]
            filterDDColumn = str(filterSearchDataDisplayName)
        
        else:
            filterDDColumnData = False
            filterDDColumn = None
        
        if filterRBStatus == True:

            filterRBColumnData = [item[str(filterRadioButtonColumnName)] for item in dataList]
            filterRBColumn = str(filterRadioButtonDisplayName)
        
        else:
            filterRBColumnData = False
            filterRBColumn = None

        filterDict = {"filterDDColumnData": filterDDColumnData, "filterDDStatus": filterDDStatus, "filterDDColumn": filterDDColumn, "filterRBStatus": filterRBStatus, "filterRBColumn": filterRBColumn, "filterRBColumnData": filterRBColumnData, "tableModalStatus": tableModalStatus}

        return filterDict
    
    # endregion

    # region Creator Blue Print Name And Class List
    
    def creatorBluePrintNameAndClassList(self, name):

        bluePrintNameList = [name, f"{name}data", f"{name}delete", f"{name}update", f"{name}detail", f"{name}add"]

        bluePrintClassList = [f"Get{name.capitalize()}List", f"Get{name.capitalize()}Data", f"{name.capitalize()}Delete", f"{name.capitalize()}Update", f"{name.capitalize()}Detail", f"{name.capitalize()}Add"]

        return bluePrintNameList, bluePrintClassList
    
    # endregion
    
    # region Cleat Meta Data
    
    def clearMetaData(self, dataList):

        keys_to_remove = ['metadata', 'query']

        for item in dataList:
            for key in keys_to_remove:
                if key in item:
                    del item[key]

        return dataList

    # endregion
    
    # region Create Company Name From Email

    def createCompanyName(self, email, characterStatus = "Capitialize"):

        companyName = re.search(r'@(.+?)\.', email) 
        companyName = companyName.group(1)

        if characterStatus == "Capitialize":
            companyName = companyName.capitalize()
        elif characterStatus == "Lower":
            companyName = companyName.lower()
        elif characterStatus == "Upper":
            companyName = companyName.upper()
        
        return companyName

    # endregion

    # region Create Dictionary

    def createDictionary(self, **kwargs):

        return kwargs
    
    # endregion

    # region Translate Turkish Characters

    def translateTrChar(self, text):

        tr_chars = "ğĞıİöÖüÜşŞçÇ"
        en_chars = "gGiIoOuUsScC"

        trans_table = str.maketrans(tr_chars, en_chars)

        text = text.translate(trans_table)

        text = text.encode(
            'ascii', errors='replace').decode()

        return text

    # endregion
    
    # region Create SignIn Id

    def createSignInId(self):

        now = str(time.time()) + str(random.randint(1, 1000000))
        return uuid.uuid3(uuid.NAMESPACE_DNS, now)

    # endregion

    # region Create User Id

    def createUserId(self, email):

        return str(uuid.uuid3(uuid.NAMESPACE_DNS, email))

    # endregion

    # region Create Token

    def createToken(self, email):

        safeUrl = URLSafeTimedSerializer(email)
        token = safeUrl.dumps(email, salt=email)

        return token

    # endregion

    # region Encrypt Password

    def encryptPassword(self, password):

        return sha256_crypt.encrypt(password)
    
    # endregion

    # region Password Check

    def passwordCheck(self, password, authPassword):

        return sha256_crypt.verify(password, authPassword)

    # endregion

    # region Set Sessions

    def setSessions(self, email=None, userId="Test"):

        Session.signInId = self.createSignInId()
        Session.email = email

        if userId is None or userId == "Test":
            Session.userId = self.createSignInId()
        else:
            Session.userId = userId

    # endregion
    
    # region Set Dynamic Folder Path

    def setDynamicFolderPath(self, userId, FolderName):

        userIdFolderPath = os.path.join(self.__userFolderPath, userId)
        dynamicFolderPath = os.path.join(userIdFolderPath, FolderName)

        return dynamicFolderPath
    
    # endregion

    # region Set Core Folder Path
    
    def setCoreFolderPath(self, userId):

        userIdFolderPath = os.path.join(self.__userFolderPath, userId)
        datasetFolderPath = os.path.join(userIdFolderPath, "Dataset")
        resultFolderPath = os.path.join(userIdFolderPath, "Result")
        tempFolderPath = os.path.join(userIdFolderPath, "Temp")
        imageFolderPath = os.path.join(userIdFolderPath, "Image")
        
        return datasetFolderPath, resultFolderPath, tempFolderPath, imageFolderPath
    
    # endregion

    # region Set All Folder Path
    
    def setAllFolderPath(self, userId):

        userIdFolderPath = os.path.join(self.__userFolderPath, userId)
        datasetFolderPath = os.path.join(userIdFolderPath, "Dataset")
        resultFolderPath = os.path.join(userIdFolderPath, "Result")
        tempFolderPath = os.path.join(userIdFolderPath, "Temp")
        imageFolderPath = os.path.join(userIdFolderPath, "Image")
        
        return userIdFolderPath, datasetFolderPath, resultFolderPath, tempFolderPath, imageFolderPath
    
    # endregion

# endregion

