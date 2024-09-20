# region Import Packages

import shutil
import os

from P3_Scorpius.S3_HeroKit.HeroKit import HeroKit

# endregion

# region FolderOS Class
class FolderOS:
    
    # region Init  

    def __init__(self, userId):

        self.HeroKits = HeroKit() 

        self.HeroKits.setAllFolderPath(userId)  

        self.__userIdFolderPath, self.__logFolderPath, self.__imageFolderPath = self.HeroKits.setAllFolderPath(userId)  
        
    # endregion

    # region Logix Algorithm

    # region General Create Folder

    def generalCreateFolder(self, folderPath=None, folderName=None):

        if folderName != None:

            folderPath = os.path.join(folderPath, folderName)

        if not os.path.exists(folderPath):
            os.mkdir(folderPath)

    # endregion

    # region General Rename Folder

    def generalRenameFolder(self, folderPath, oldFolderName, newFolderName):

        oldFolderPath = os.path.join(folderPath, oldFolderName)
        newFolderPath = os.path.join(folderPath, newFolderName)

        if os.path.exists(oldFolderPath) == True:
            os.rename(oldFolderPath, newFolderPath)

    # endregion

    # region General Delete Folder Tree Function
        
    def generalDeleteFolder(self, folderPath, newFolderName):

        deleteFolderPath = os.path.join(folderPath, newFolderName)

        if os.path.exists(deleteFolderPath):
            shutil.rmtree(deleteFolderPath)
    
    # endregion

    # region Create Workspace Folder

    def createWorkspaceFolder(self, workspaceName):

        self.generalCreateFolder(self.__datasetFolderPath, workspaceName)
        self.generalCreateFolder(self.__resultFolderPath, workspaceName)
        self.generalCreateFolder(self.__tempFolderPath, workspaceName)

    # endregion
        
    # region Create Dataset And Result Folder
        
    def createDatasetAndResultFolder(self, workspaceName):

        self.generalCreateFolder(self.__datasetFolderPath, workspaceName)
        self.generalCreateFolder(self.__resultFolderPath, workspaceName)
    
    # endregion

    # region Create User Main Folder

    def createUserMainFolder(self):

        self.generalCreateFolder(self.__userIdFolderPath)
        self.generalCreateFolder(self.__logFolderPath)
        self.generalCreateFolder(self.__imageFolderPath)
        
    # endregion

    # region Rename Workspace Folder

    def renameWorkspaceFolder(self, oldWorkspaceName, newWorkspaceName):

        self.generalRenameFolder(self.__resultFolderPath, oldWorkspaceName, newWorkspaceName)
        self.generalRenameFolder(self.__datasetFolderPath, oldWorkspaceName, newWorkspaceName)
    
    # endregion

    # region Delete Workspace Folder

    def deleteWorkspaceFolder(self, workspaceName):

        self.generalDeleteFolder(self.__resultFolderPath, workspaceName)
        self.generalDeleteFolder(self.__datasetFolderPath, workspaceName)
    
    # endregion

    # endregion

# endregion