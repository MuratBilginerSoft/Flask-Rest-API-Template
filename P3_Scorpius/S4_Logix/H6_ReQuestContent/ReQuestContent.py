# region Import Packages

from flask import request
import json
import ast

# endregion

# region RequestContent Class

class ReQuestContent:

    # region Init

    def __init__(self):
        pass

    # endregion

    # region Logix

    # region Form

    def form(self, contentText, variableType, booleanType="int"):

        # region Get Form Content

        self.__formContent = request.form

        # endregion

        # region Such A ContentText

        if contentText in self.__formContent:

            # region Int

            if variableType == "int":
                if self.__formContent[contentText]:
                    return int(self.__formContent[contentText])
                else:
                    return None

            # endregion

            # region Float

            elif variableType == "float":

                if self.__formContent[contentText]:
                    return float(self.__formContent[contentText])
                else:
                    return None
            
            # endregion

            # region Str

            elif variableType == "str":
                    
                if self.__formContent[contentText]:
                    return str(self.__formContent[contentText]).strip()
                else:
                    return ""

            # endregion
                
            # region List

            elif variableType == "list":
                    
                if self.__formContent[contentText]:
                    return ast.literal_eval(self.__formContent[contentText]) 
                else:
                    return []
            
            # endregion
                
            # region List

            elif variableType == "dict":
                    
                if self.__formContent[contentText]:

                    strDict = self.__formContent[contentText]
                    jsonDict = json.loads(strDict)
                    
                    return jsonDict
                else:
                    return []
            
            # endregion

            # region Any

            else:
                
                if self.__formContent[contentText]:
                    return self.__formContent[contentText]
                else:
                    return None
            
            # endregion

        # endregion

        # region Not Such A ContentText

        else:
            return None
        
        # endregion

    # endregion

    # region Json

    def json(self, contentText, variableType, booleanType="int"):

        # region Get JsonContent

        self.__jsonContent = request.get_json() # type: ignore
        
        # endregion

        # region Such A ContentText

        if self.__jsonContent != None:

            if contentText in self.__jsonContent:

                # region Int

                if variableType == "int":

                    if self.__jsonContent[contentText]:
                        return int(self.__jsonContent[contentText])
                    else:
                        return None
                
                # endregion

                # region Float

                elif variableType == "float":
                        
                    if self.__jsonContent[contentText]:
                        return float(self.__jsonContent[contentText])
                    else:
                        return 0
                        
                # endregion
                
                # region Str

                elif variableType == "str":

                    if self.__jsonContent[contentText]:
                        return str(self.__jsonContent[contentText]).strip()
                    else:
                        return ""
                
                # endregion

                # region Bool

                elif variableType == "bool":
                        
                    if self.__jsonContent[contentText]:
                        return 1 if self.__jsonContent[contentText] == True else 0
                    else:
                        return 0

                # endregion

                # region List

                elif variableType == "list":
                        
                    if self.__jsonContent[contentText]:
                        return self.__jsonContent[contentText]
                    else:
                        return []
                
                # endregion
                
                # region Dict

                elif variableType == "dict":
                        
                    if self.__jsonContent[contentText]:
                        return self.__jsonContent[contentText]
                    else:
                        return {}
                    
                # endregion

                # region Any

                else:

                    if self.__jsonContent[contentText]:
                        return self.__jsonContent[contentText]
                    else:
                        return None
                
                # endregion

            # endregion

            # region Not Such A ContentText

            else:

                if variableType == "int" or variableType == "float":

                    return None
                
                elif variableType == "str":
                        
                    return ""
                
                elif variableType == "bool":

                    return 0
                
                elif variableType == "list":

                    return []
                
                elif variableType == "dict":

                    return {}
                
                else:

                    return None
            
            # endregion

        else:

            if variableType == "int" or variableType == "float":

                return None
            
            elif variableType == "str":
                    
                return ""
            
            elif variableType == "bool":

                return 0
            
            elif variableType == "list":

                return []
            
            elif variableType == "dict":

                return {}
            
            else:

                return None

    # endregion

    # region File

    def file(self):

        fileInfo = request.files

        return fileInfo
    
    # endregion

    # region Params

    def params(self, variable, variableType, booleanType="int"):

        if str(variable) in request.args:

            if variableType == "str":
                return str(request.args.get(variable)).strip()  # type: ignore

            elif variableType == "int":
                return int(request.args.get(variable)) # type: ignore

            elif variableType == "float":

                return float(request.args.get(variable)) # type: ignore
            
            elif variableType == "bool":

                return 1 if request.args.get(variable) == True else 0 # type: ignore
            
            elif variableType == "list":

                return ast.literal_eval(request.args.get(variable)) # type: ignore
            
        else:
            if variableType == "str":
                return ""
            elif variableType == "int":
                return 0
            elif variableType == "float":
                return 0.0
            elif variableType == "bool":
                return 0
            elif variableType == "list":
                return []
        
    # endregion

    # endregion
            
    def generalBody(self, bodyJson):

        responseData = {}

        for variableName, bodyList in bodyJson.items():

            if bodyList[0] == "form":

                if len(bodyList) == 3:
                    data = self.form(variableName, bodyList[1], booleanType=bodyList[2])
                
                else:
                    data = self.form(variableName, bodyList[1])

                responseData[variableName] = data
                
            elif bodyList[0] == "json":

                if len(bodyList) == 3:
                    data = self.json(variableName, bodyList[1], booleanType=bodyList[2])
                
                else:
                    data = self.json(variableName, bodyList[1])

                responseData[variableName] = data
                
            elif bodyList[0] == "params":

                if len(bodyList) == 3:
                    data = self.params(variableName, bodyList[1], booleanType=bodyList[2])
                
                else:
                    data = self.params(variableName, bodyList[1])

                responseData[variableName] = data
            
            elif bodyList[0] == "file":
                data = self.file()
                responseData[variableName] = data
            
            else:
                return {"error" : "Body type is not valid"}
           
        return responseData
    
    def generalBodyV2(self, bodyJson):

        responseData = {}
        type = bodyJson["type"]
        del bodyJson["type"]

        if type == "form":

            for variableName, bodyList in bodyJson.items():

                if len(bodyList) == 2:

                    if bodyList[1] == "file":
                        data = self.file()
                        responseData[variableName] = data
                    else:
                        data = self.form(variableName, bodyList[0], booleanType=bodyList[1])
                
                else:

                    if bodyList[0] == "file":
                        data = self.file()
                        responseData[variableName] = data
                    else:
                        data = self.form(variableName, bodyList[0])

                responseData[variableName] = data
        
        elif type == "json":

            for variableName, bodyList in bodyJson.items():

                if len(bodyList) == 2:
                    data = self.json(variableName, bodyList[0], booleanType=bodyList[1])
                
                else:
                    data = self.json(variableName, bodyList[0])

                responseData[variableName] = data

        elif type == "params":

            for variableName, bodyList in bodyJson.items():

                if len(bodyList) == 2:
                    data = self.params(variableName, bodyList[0], booleanType=bodyList[1])
                
                else:
                    data = self.params(variableName, bodyList[0])

                responseData[variableName] = data
            
        else:
            return {"error" : "Body type is not valid"}

        return responseData
# endregion