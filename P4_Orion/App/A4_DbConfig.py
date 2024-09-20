# region Import Packages

import os
import shutil

# endregion

# region Class DbConfig

class DbConfig:

    # region Global Variables

    dbUrl = None

    # endregion

    # region Init
    
    def __init__(self, index):

        self.__dirPath = os.getcwd()

        self.__index = index

        self.__dataBases = ['devdb', 'proddb',]

        self.__migrationFolderList = ["migrationsDev", "migrationsPro"]

        self.__host = 'prowthdb.mysql.database.azure.com'
        self.__userName = 'muratbilginer'
        self.__password = "Tj_G{z=<4$'3qg-#"
        self.__database = self.__dataBases[index]

        self.__database = self.__dataBases[index]

        print("Database: ", self.__database)

        self.main()
    
    # endregion

    # region Main
        
    def main(self):

        self.changeFolder()
        self.createDbUrl()
        
    # endregion
        
    # region Change Folder

    def changeFolder(self):

        migrationsFolders = [folderName for folderName in os.listdir(self.__dirPath) if folderName.startswith("migrations")]

        print(migrationsFolders)

        diff_val = next((x for x in self.__migrationFolderList if x not in migrationsFolders), None)

        print(diff_val)
        
        self.renameFolder(diff_val, "migrations")
        self.renameFolder("migrations", self.__migrationFolderList[self.__index])

    # endregion
        
    # region createDbUrl

    def createDbUrl(self):

        print("Database URL: ", self.__database)

        DbConfig.dbUrl = 'mysql+pymysql://{user}:{pw}@{url}/{db}'.format(user=self.__userName, pw=self.__password, url=self.__host, db=self.__database)

    # endregion
        
    # region renameFolder
   
    def renameFolder(self, newName, oldName):

        shutil.move(os.path.join(self.__dirPath, oldName), 
                  os.path.join(self.__dirPath, newName))
    
    # endregion

# endregion