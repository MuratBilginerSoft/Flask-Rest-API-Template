# region Import Packages

from datetime import datetime, timedelta
import datetime as dt 
import pytz
import time

# endregion

# region GetDate

class GetDate():

    # region Init

    def __init__(self):

        # region Variables

        self.__timeZone = pytz.timezone('Europe/Istanbul')

        # endregion

    # endregion

    # region Current

    def currentDate(self):

        date = dt.datetime.now(self.__timeZone).strftime("%Y-%m-%d %H:%M:%S")
        return date
    
    # endregion

    # region Current Time

    def currentTime(self):

        return time.time()
        
    # endregion

    # region Get Start And End Date

    def getStartAndEndDate(self, days):

        self.__startDate = datetime.strptime(self.currentDate(), '%Y-%m-%d %H:%M:%S')

        self.__endDate = str(self.__startDate + timedelta(days=days))

        return str(self.__startDate), str(self.__endDate)

    # endregion

# endregion