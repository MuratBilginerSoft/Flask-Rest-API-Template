# region Import Packages

import traceback

from BackEnd.Q1_BlueWhale.B2_Management.M2_Offices.O2_GetOfficeList import GetOfficeList
from BackEnd.Q1_BlueWhale.B2_Management.M2_Offices.O3_GetOfficeAdd import GetOfficeAdd
from BackEnd.Q1_BlueWhale.B2_Management.M2_Offices.O4_OfficeAdd import OfficeAdd

from P3_Scorpius.S5_Session.Session import Session

# endregion

# region Offices Class

class Offices:

    # region Init Function

    def __init__(self):

        # region Create Object

        self.GetOfficeLists = GetOfficeList()   
        self.GetOfficeAdds = GetOfficeAdd()
        self.OfficeAdds = OfficeAdd()
        
        # endregion

        # region Class Variables

        self.__bluePrintName = None
        self.__userId = None

        # endregion

    # endregion
    
    # region Main
        
    def main(self, urlName, method, **kwargs):

        try:

            self.__urlName = urlName
            self.__bluePrintName = kwargs["bluePrintName"]

            if method == "GET" and Session.status == True:

                if self.__bluePrintName == "officelist":
                    return self.GetOfficeLists.main(self.__urlName, **kwargs)
                
                elif self.__bluePrintName == "officesadd":
                    return self.GetOfficeAdds.main(self.__urlName, **kwargs)
            
            elif method == "POST" and Session.status == True:

                return self.OfficeAdds.main(self.__urlName, **kwargs)

            elif method == "PUT" and Session.status == True:
                pass
            
            elif method == "DELETE" and Session.status == True:
                pass

            else:
                return self.GetOfficeLists.main(self.__urlName, **kwargs)
        
        except Exception:
            traceback.print_exc()
            return self.GetOfficeLists.main(self.__urlName, **kwargs)
    
    # endregion
    
#endregion
