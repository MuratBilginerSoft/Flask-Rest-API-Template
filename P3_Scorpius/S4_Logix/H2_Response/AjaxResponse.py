# region Import Packages

from flask import jsonify

# endregion

# region Class Response

class AjaxResponse():

    # region main Function
    
    def general(self, statusCode=200, responseDict = {"message" : "Message"}, **kwargs):

        response = jsonify(responseDict)
        response.status_code = statusCode
        return response
        
    # endregion

    # region main Function
    
    def success(self, statusCode=200, responseDict = {"message" : "Message"}, **kwargs):

        response = jsonify(responseDict)
        response.status_code = statusCode
        return response
        
    # endregion


    def error(self, statusCode=401, responseDict = {"error": "Error"}, **kwargs):

        response = jsonify(responseDict)
        response.status_code = statusCode
        return response
    
    def errorSomethingWentWrong(self):

        return self.error(statusCode=400, responseDict={'error': 'Something went wrong'})
    
    def errorDataNotFound(self):

        return self.error(statusCode=400, responseDict={'error': 'Data not found'})
# endregion