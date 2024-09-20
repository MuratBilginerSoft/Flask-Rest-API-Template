# region Import Packages

from P2_Sirius.S1_Models.M1_DataContext.GeneralQuery import GeneralQuery

# endregion

# region HelperQuery Class

class HelperQuery:

    # region Init

    def __init__(self):

        # region Create Objects

        self.GeneralQueries = GeneralQuery()
    
        # endregion

    # endregion

    # region 1 Get Data Table With Id

    def getDataTableWithId(self, table, Id, session = None):

        return self.GeneralQueries.getDataAnyTableWithId(table, Id, session=session)
        
    # endregion

    # region 2 Get Datas Table With UserId

    def getDatasTableWithUserId(self, table, userId, sort="Desc", session=None):

        return self.GeneralQueries.getDatasAnyTableWithUserIdSort(table, userId, sort=sort, session=session)

    # endregion

    # region 4 Get Datas Table Limitless With UserId SubscriptionId

    def getDatasLimitless(self, table, userId, subscriptionId, sort="Desc", limit=5, session=None):

        return self.GeneralQueries.getLimitDatasAnyTableAnyFilterSort(table, sort=sort, limit=limit, session=session, UserId=userId, SubscriptionId=subscriptionId, DeleteFlag=0)

    # endregion


# endregion