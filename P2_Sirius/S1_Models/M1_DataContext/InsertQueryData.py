# region import Packages

from P2_Sirius.S1_Models.M3_Entities.Authentications import Authentications
from P2_Sirius.S1_Models.M3_Entities.Users import Users

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

# endregion
