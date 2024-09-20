# region Import Packages

import traceback

from sqlalchemy import create_engine, text, or_, and_
from sqlalchemy.orm import Session

from Entity.DbConfig.DbConfig import dbUrl

# endregion

# region SelectQuery Class

class SelectQuery():

    # region Init Function

    def __init__(self):
        
        self.__engine = create_engine(dbUrl, echo=True, future = True)
        self.__session = Session(self.__engine)
    
    # endregion

    # region Get Table FirstData AnyFilter

    def getTableFirstDataAnyFilter(self,tableName,kwargs):

        try:
            result = tableName.query.filter_by(**kwargs).first()
            return result
        
        except Exception as e:

            traceback.print_exc()
            return str(e)

    # endregion

    # region Get Table AllData AnyFilter

    def getTableAllDataAnyFilter(self,tableName,kwargs):

        try:
            
            result = tableName.query.filter_by(**kwargs).all()
            return result

        except Exception as e:

            traceback.print_exc()
            return str(e)

    # endregion

    # region Get Table FirstData Any Filter Descanding

    def getTableFirstDataAnyFilterDescanding(self, tableName, kwargs):

        try:
            oneRecord = tableName.query.filter_by(**kwargs).order_by(tableName.Id.desc()).first()
            return oneRecord, 200
        except:
            return False, 400

    # endregion

    # region Get Table FirstData Any Filter Ascending

    def getTableFirstDataAnyFilterAscending(self, tableName, kwargs):

        try:
            oneRecord = tableName.query.filter_by(**kwargs).order_by(tableName.Id.asc()).first()
            return oneRecord, 200
        except:
            return False, 400

    # endregion


    # region GetGirisYönetici

    def getGirisYönetici(self, statuOne, statuTwo):

        try:
            query = text("Select * From Giriş where Statü=:x or Statü=:y and SilinmeDurumu=0").bindparams(x=str(statuOne).strip(), y = str(statuTwo).strip())
            result = self.__session.execute(query).all()
            return result,200

        except Exception as e:
            traceback.print_exc()
            return 0,400
    
    # endregion

    pass

#endregion