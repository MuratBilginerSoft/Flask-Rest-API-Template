# region import Packages

from P2_Sirius.S1_Models.M3_Entities.AuthenticationLogs import AuthenticationLogs
from P2_Sirius.S1_Models.M3_Entities.Authentications import Authentications
from P2_Sirius.S1_Models.M3_Entities.Users import Users
from P2_Sirius.S1_Models.M3_Entities.Mails import Mails
from P2_Sirius.S1_Models.M3_Entities.Sites import Sites
from P2_Sirius.S1_Models.M3_Entities.SiteMail import SiteMails
from P2_Sirius.S1_Models.M3_Entities.SitesSchedule import SiteSchedules


from P2_Sirius.S1_Models.M1_DataContext.GeneralQuery import GeneralQuery
from P2_Sirius.S1_Models.M1_DataContext.AlchemyEngine import AlchemyEngine

from P3_Scorpius.S4_Logix.H5_GetDate.GetDate import GetDate

# endregion

# region InsertQueryData Class


class InsertQueryData:

    # region 0 Init

    def __init__(self) -> None:

        # region Create Object

        self.GeneralQueries = GeneralQuery()
        self.GetDates = GetDate()

        # endregion

        # region Variables

        self.__date = self.GetDates.currentDate()

        # endregion

    # endregion

    # region 1 Authentication

    def insertAuthentication(self, userId, email, cryptPassword, token, commitStatus=False):

        insertData = Authentications(UserId=userId, Email=email, Password=cryptPassword, Token=token, ConfirmStatus=1, CreatedBy=userId, CreatedAt=self.__date, ChangedBy=userId, ChangedAt=self.__date, Revision=0, DeleteFlag=0)

        self.GeneralQueries.insertData(insertData, AlchemyEngine.session, commitStatus)

    # endregion

    # region 2 User

    def insertUser(self, userId, email, name="Admin", surname="Admin", company="CheckerMan", role="Admin", imagePath="None", commitStatus=False):

        insertData = Users(UserId=userId, Email=email, Name=name, Surname=surname, Company=company, Role=role, ImagePath=imagePath, CreatedBy=userId, CreatedAt=self.__date, ChangedBy=userId, ChangedAt=self.__date, Revision=0, DeleteFlag=0)

        self.GeneralQueries.insertData(
            insertData, AlchemyEngine.session, commitStatus)

    # endregion

    # region 3 AuthenticationLogs

    def insertAuthenticationLog(self, userId, status, commitStatus=False):

        insertData = AuthenticationLogs(UserId=userId, Status=status, ChangeStatusAt=self.__date, CreatedBy=userId, CreatedAt=self.__date, ChangedBy=userId, ChangedAt=self.__date, Revision=0, DeleteFlag=0)

        self.GeneralQueries.insertData(
            insertData, AlchemyEngine.session, commitStatus)

    # endregion

    # region 3 AuthenticationLogs

    def insertMail(self, userId, email, status, commitStatus=False):

        insertData = Mails(UserId=userId, Email=email, Status=status,  CreatedBy=userId, CreatedAt=self.__date, ChangedBy=userId, ChangedAt=self.__date, Revision=0, DeleteFlag=0)  

        self.GeneralQueries.insertData(insertData, AlchemyEngine.session, commitStatus)

    # endregion

    # region 4 Insert Site

    def insertSite(self, userId, name, status, commitStatus=False):

        insertData = Sites(UserId=userId, Name=name, Status=status,  CreatedBy=userId, CreatedAt=self.__date, ChangedBy=userId, ChangedAt=self.__date, Revision=0, DeleteFlag=0)  

        self.GeneralQueries.insertData(insertData, AlchemyEngine.session, commitStatus)

    # endregion

    # region 5 Insert Site Email

    def insertSiteEmail(self, userId, siteId, email, commitStatus=False):

        insertData = SiteMails(UserId=userId, SiteId=siteId, Email=email,  CreatedBy=userId, CreatedAt=self.__date, ChangedBy=userId, ChangedAt=self.__date, Revision=0, DeleteFlag=0)  

        self.GeneralQueries.insertData(insertData, AlchemyEngine.session, commitStatus)

    # endregion

    # region 5 Insert Site Schedule

    def insertSiteSchedule(self, userId, siteId, scheduleDate, commitStatus=False):

        insertData = SiteSchedules(UserId=userId, SiteId=siteId, ScheduleDate=scheduleDate, CreatedBy=userId, CreatedAt=self.__date, ChangedBy=userId, ChangedAt=self.__date, Revision=0, DeleteFlag=0)  

        self.GeneralQueries.insertData(insertData, AlchemyEngine.session, commitStatus)

    # endregion

# endregion
