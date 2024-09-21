# region Import Packages

import os
import shutil

# endregion

# region Creator Class

class Creator:
    
    # region Constructor
    
    def __init__(self) -> None:
        pass
    
    # endregion
    
    # region Main
    
    def main(self):
        
        self.className = input("Enter the class name: ")
        self.routeUrl = f'/{input("Enter the route url: ")}' 
        self.singleMethodStatus = input("Enter the single method status (T/F):").upper()
        self.blueprintName = self.className.lower()
        
        self.folderPathDefine()
        
        if self.singleMethodStatus == "T":
            
            self.singleMethodCreator()
            
            newEntryEndpointClass = f'\n        "{self.className}": {{"{self.methodName}": "{self.className}"}},'
            self.endpointClassFileUpdate(newEntryEndpointClass)
            self.routePagesFileUpdate()
            self.routerFileUpdate()
        
    # endregion

    # region folderPathDefine

    def folderPathDefine(self):
        
        self.controllerPath = os.path.join("P2_Sirius", "S2_Controllers", self.className)
        self.endPointClassFilePath = os.path.join("P3_Scorpius", "S1_App", "Router", "EndPointClass.py")
        self.routePagesPath = os.path.join("P3_Scorpius", "S1_App", "Router", "RoutePages.py")
        self.routerPath = os.path.join("P3_Scorpius", "S1_App", "Router", "Router.py")
        self.singleMethodSourceFilePath = os.path.join("P5_PointMaker", "PointClass", "SingleMethot.py")
        self.singleMethodDestinationFilePath = os.path.join(self.controllerPath, f"{self.className}.py")

    # endregion
    
    # region singleMethodCreator

    def singleMethodCreator(self):

        self.methodName = input("Enter the single method name: (GET || POST || PUT || PATCH || DELETE) ").upper()
        os.makedirs(self.controllerPath, exist_ok=True)
    
        shutil.copyfile(self.singleMethodSourceFilePath, self.singleMethodDestinationFilePath)

    # endregion
    
    # region endpointClassFileUpdate
    
    def endpointClassFileUpdate(self, newEntry):
        
        with open(self.endPointClassFilePath, 'r') as file:
            lines = file.readlines()
            
        start_index = None
        for i, line in enumerate(lines):
            if line.strip().startswith("endpointClass = {"):
                start_index = i
                break

        if start_index is not None:
            lines.insert(start_index + 1, newEntry)

        with open(self.endPointClassFilePath, 'w') as file:
            file.writelines(lines)  

    # endregion
    
    # region routePagesFileUpdate
     
    def routePagesFileUpdate(self):
        
        with open(self.routePagesPath, 'r') as file:
            lines = file.readlines()

        last_from_import_index = None
        for i, line in enumerate(lines):
            if line.startswith("from "):
                last_from_import_index = i

        if last_from_import_index is not None:
            new_import = f'from P2_Sirius.S2_Controllers.{self.className}.{self.className} import {self.className}'
            lines.insert(last_from_import_index + 1, new_import)

        with open(self.routePagesPath, 'w') as file:
            file.writelines(lines)
    
    # endregion
    
    # region routerFileUpdate
    
    def routerFileUpdate(self):
        
        with open(self.routerPath, 'r') as file:
            lines = file.readlines()

        start_index = None
        for i, line in enumerate(lines):
            if line.strip().startswith("bluePrintParameter = {"):
                start_index = i
                break

        if start_index is not None:
            new_entry = f'\n            "{self.blueprintName}": ["{self.blueprintName}", "{self.className}", "{self.routeUrl}"],'
            lines.insert(start_index + 1, new_entry)

        with open(self.routerPath, 'w') as file:
            file.writelines(lines)  


    # endregion

# endregion