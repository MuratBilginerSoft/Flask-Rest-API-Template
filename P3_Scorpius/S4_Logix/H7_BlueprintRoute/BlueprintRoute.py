# region Import Packages

import traceback
import sys

from P3_Scorpius.S4_Logix.H7_BlueprintRoute.BluePrintRoutePages import *

# endregion

# region BlueprintRoute Class

class BlueprintRoute:

    # region Route

    def route(self, method, status, urlName, bluePrintNameX,bluePrintNameList, bluePrintClassList, **kwargs):

        try:

            classInstance = self.createBlueprintClassInstance(bluePrintClassList)

            if method == "GET" and status == True:
                    
                if bluePrintNameX == bluePrintNameList[0]:
                    return classInstance[0].main(urlName, **kwargs)
                
                elif bluePrintNameX == bluePrintNameList[1]:
                    return classInstance[1].main(**kwargs)
                
                elif bluePrintNameX == bluePrintNameList[2]:
                    return classInstance[2].main(**kwargs)
                
                elif bluePrintNameX == bluePrintNameList[3]:

                    return classInstance[3].get(**kwargs)
                
                elif bluePrintNameX == bluePrintNameList[4]:

                    return classInstance[4].main(**kwargs)
                    
            elif method == "POST" and status == True:
                    
                if bluePrintNameX == bluePrintNameList[3]:
                    return classInstance[3].update(**kwargs)
                
                if bluePrintNameX == bluePrintNameList[0]:
                    return classInstance[0].main(urlName, **kwargs)
                
                elif bluePrintNameX == bluePrintNameList[5]:
                    return classInstance[5].main(**kwargs)
                
            else:
                return bluePrintClassList[6].main(**kwargs)
            
        except Exception:
            traceback.print_exc()
            return classInstance[1].main(**kwargs)

    # endregion

    # region Create Blueprint Class

    def createBlueprintClassInstance(self, bluePrintClassList):

        sysModules = sys.modules[__name__]
        classInstance = []

        for i in range(len(bluePrintClassList)):
            
            classInstance.append(getattr(sysModules, bluePrintClassList[i])())

        return classInstance
    
    # endregion

# endregion