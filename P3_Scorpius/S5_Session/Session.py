# region Import Packages

import uuid
import os

from P3_Scorpius.S4_Logix.H5_GetDate.GetDate import GetDate
from P3_Scorpius.S6_Utils.Mapping.Menu import Menu

# endregion

# region Session Class

class Session:

    date = GetDate().currentDate()
    counter = 0

    signInId    = uuid.uuid3(uuid.NAMESPACE_DNS, date)
    userId      = "dbcb312e-5895-3f5d-9713-611a9c0c254e"
    email       = None
    status = True
    name = "Admin"
    surname = "Admin"
    company = "Company"
    role = "Manager"
    sidebarMenu = Menu.sidebarMenu
    userCount = 1
    subscriptionId = "2fcd0716-130c-3304-afbe-c5559286813e"

    userFolderPath = os.path.join(os.getcwd(), "Assets", "Users")

    formId = 1
    
# endregion