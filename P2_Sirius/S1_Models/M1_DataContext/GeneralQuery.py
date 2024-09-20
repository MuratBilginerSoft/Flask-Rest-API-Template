# region Import Packages

import traceback

from sqlalchemy import create_engine, text, or_, and_

from P2_Sirius.S1_Models.M1_DataContext.AlchemyEngine import AlchemyEngine   
from P3_Scorpius.S4_Logix.H5_GetDate.GetDate import GetDate
from P3_Scorpius.S5_Session.Session import Session

# endregion

# region GeneralQuery Class

class GeneralQuery:

    # region 0 Global Variables
    
    insertStatus = 400
    updateStatus = 400
    deleteStatus = 400

    # endregion

    # region 1 Init

    def __init__(self):

        # region Create Instances

        self.AlchemyEngines = AlchemyEngine() 
        self.GetDates = GetDate()

        # endregion

    # endregion
        
    # region 2 Select Query General

    # region 1 Get Data Any Table With Any Filter

    def getDataAnyTableAnyFilter(self, table, session = None, **kwargs):

        session = self.AlchemyEngines.sessionControl(session)

        return session.query(table).filter_by(**kwargs).first() # type: ignore

    # endregion

    # region 2 Get Data Any Table With Any Filter Sort

    def getDataAnyTableAnyFilterSort(self, table, sort = "Desc", session = None, **kwargs):

        session = self.AlchemyEngines.sessionControl(session)

        if sort == "Desc" or sort != "Asc":

            return session.query(table).filter_by(**kwargs).order_by(table.Id.desc()).first() # type: ignore
            
        elif sort == "Asc":

            return session.query(table).filter_by(**kwargs).order_by(table.Id.asc()).first() # type: ignore
    
    # endregion
    
    # region 3 Get Datas Any Table Any Filter Sort

    def getDatasAnyTableAnyFilterSort(self, table, sort = "Desc", session = None, **kwargs):

        session = self.AlchemyEngines.sessionControl(session)

        if sort == "Desc" or sort != "Asc":

            result = session.query(table).filter_by(**kwargs).order_by(table.Id.desc()).all() # type: ignore
            
        elif sort == "Asc":

            result = session.query(table).filter_by(**kwargs).order_by(table.Id.asc()).all() # type: ignore
        
        dataList = [table._to_dict() for table in result]

        return dataList
    
    # endregion
    
    # region 4 Get Limit Datas Any Table Any Filter Sort

    def getLimitDatasAnyTableAnyFilterSort(self, table, sort="Desc", limit=5, session=None, **kwargs):

        session = self.AlchemyEngines.sessionControl(session)

        if sort == "Desc" or sort != "Asc":

            result = session.query(table).filter_by(**kwargs).order_by(table.Id.desc()).limit(limit).all() # type: ignore
            
        elif sort == "Asc":

            result =  session.query(table).filter_by(**kwargs).order_by(table.Id.asc()).limit(limit).all() # type: ignore
        
        dataList = [table._to_dict() for table in result]

        return dataList

    # endregion

    # region 5 Get Table Data Count Any Filter

    def getDataCountAnyTableListAnyFilter(self, table, session = None, **kwargs):

        resData = {}

        session = self.AlchemyEngines.sessionControl(session)

        if type(table) == list:

            for table in table:

                name = str(table).split('.')[-1].replace("'", "").replace(">", "")
                resData[f"{name}Count"] = session.query(table).filter_by(**kwargs).count() # type: ignore
        
        else:

            name = str(table).split('.')[-1].replace("'", "").replace(">", "")
            resData[f"{name}Count"] = session.query(table).filter_by(**kwargs).count() # type: ignore

        return resData
    
    # endregion
    
    # region 6 Get Table Data Count Any Filter

    def getDataCountAnyTableAnyFilter(self, table, session = None, **kwargs):

        session = self.AlchemyEngines.sessionControl(session)

        return session.query(table).filter_by(**kwargs).count() # type: ignore

    # endregion

    # endregion

    # region 3 Select Query Private

    # region 1 Get Data Any Table With Id
    
    def getDataAnyTableWithId(self, table, id, session = None):

        session = self.AlchemyEngines.sessionControl(session)

        return session.query(table).filter_by(Id = id, DeleteFlag = 0).first() # type: ignore

    # endregion

    
    # region 4 Get Data Any Table With UserId
    
    def getDataAnyTableWithUserId(self, table, userId, session = None):

        session = self.AlchemyEngines.sessionControl(session)

        return session.query(table).filter_by(UserId = userId, DeleteFlag = 0).first() # type: ignore

    # endregion

    # region 5 Get Data Any Table With SubscriptionId
    
    def getDataAnyTableWithSubscriptionId(self, table, subscriptionId, session = None):

        session = self.AlchemyEngines.sessionControl(session)

        return session.query(table).filter_by(SubscriptionId = subscriptionId, DeleteFlag = 0).first() # type: ignore

    # endregion

    # region 6 Get Data Any Table With Email
    
    def getDataAnyTableWithEmail(self, table, email, session = None):

        session = self.AlchemyEngines.sessionControl(session)

        return session.query(table).filter_by(Email = email, DeleteFlag = 0).first() # type: ignore

    # endregion

    # region 6 Get Data Any Table With Email UserId
    
    def getDataAnyTableWithEmailUserId(self, table, userId, email, session = None):

        session = self.AlchemyEngines.sessionControl(session)

        return session.query(table).filter_by(UserId = userId, Email = email, DeleteFlag = 0).first() # type: ignore

    # endregion

    # region 7 Get Datas Any Table With UserId Sort
    
    def getDatasAnyTableWithUserIdSort(self, table, userId, sort = "Desc", session = None):

        session = self.AlchemyEngines.sessionControl(session)

        if sort == "Desc" or sort != "Asc":

            result = session.query(table).filter_by(UserId = userId, DeleteFlag = 0).order_by(table.Id.desc()).all() # type: ignore
            
        elif sort == "Asc":

            result = session.query(table).filter_by(UserId = userId,DeleteFlag = 0).order_by(table.Id.asc()).all() # type: ignore
        
        dataList = [table._to_dict() for table in result]

        return dataList
        
    # endregion
    
    # endregion

    # region 4 Insert Query

    def insertData(self, data, session = None, commitStatus = False):

        try:

            session = self.AlchemyEngines.sessionControl(session)
            session.add(data)
            GeneralQuery().insertStatus = 200

            if commitStatus:
                session.commit()
                session.close()
      
        except:
            session.rollback()  # type: ignore
            GeneralQuery().insertStatus = 400
            traceback.print_exc()
            
    # endregion
            
    # region 5 Update Query
        
    def updateData(self, data, session=None, commitStatus=False, **kwargs):
        
        try:
        
            if data:

                session = self.AlchemyEngines.sessionControl(session)
                date = self.GetDates.currentDate()

                for columnName, value in kwargs.items():

                    setattr(data, columnName, value)

                data.Revision = data.Revision + 1
                data.ChangedAt = date
                data.ChangedBy = Session.userId

                session.add(data)

                if commitStatus:
                    session.commit()
                    session.close()
                
                GeneralQuery.updateStatus = 200
            
            else:
                GeneralQuery.updateStatus = 400
        except:
            GeneralQuery.updateStatus = 400
            traceback.print_exc()   

    # endregion
    
    # region 6 Delete Query
            
    # region 1 Delete Data

    def deleteData(self, data, session = None, commitStatus = False):

        session = self.AlchemyEngines.sessionControl(session)
        
        try:
            session.delete(data)

            if commitStatus:
                session.commit()

            AlchemyEngine.deleteStatus = 200 # type: ignore

        except Exception:

            session.rollback()
            AlchemyEngine.deleteStatus = 400 # type: ignore
            traceback.print_exc()

    # endregion
        
    # region 2 Delete Datas

    def deleteDatas(self, datas, session = None, commitStatus = False):

        session = self.AlchemyEngines.sessionControl(session)

        try:

            if datas:
            
                for data in datas:

                    session.delete(data)

                if commitStatus:
                    session.commit()

            AlchemyEngine.deleteStatus = 200 # type: ignore

        except Exception:

            session.rollback()
            AlchemyEngine.deleteStatus = 400 # type: ignore
            traceback.print_exc()

    # endregion

    # endregion

    # region 7 Delete To Update Query

    def deleteToUpdateData(self, datas, session):

        try:
            if datas:

                count = len([datas])

                if count == 1:

                    self.columnUpdate(session, datas)
                
                elif count > 1:

                    for data in datas:

                        self.columnUpdate(session, data)
                
                session.commit()    
                GeneralQuery.updateStatus = 200
            
            else:
                GeneralQuery.updateStatus = 400
            
        except:
            GeneralQuery.updateStatus = 400

    def columnUpdate(self, session, data):

        date = self.GetDates.currentDate()

        data.Revision = data.Revision + 1
        data.ChangedAt = date
        data.ChangedBy = Session.userId
        data.DeleteFlag = 1
                    
        session.add(data)
        
    # endregion  
            
# endregion