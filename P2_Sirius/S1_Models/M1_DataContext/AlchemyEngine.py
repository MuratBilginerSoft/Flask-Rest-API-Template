# region Import Packages

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

from P3_Scorpius.S6_Utils.Mapping.Configuration import Configuration

# endregion

# region Alchemy Engine Class

class AlchemyEngine():

    # region Global Variables

    engine = None
    session = None
    snapSession = None

    # endregion

    # region 1 Session Control
        
    def sessionControl(self, session=None):

        if session is None: 
            session = self.snapEngine()
        
        elif session.is_active is False:
            session = self.snapEngine()
        
        return session

    # endregion

    # region 2 Session Close

    def sessionClose(self, session):

        if session and session.is_active:

            session.commit()
            session.close()

    # endregion
            
    # region 3 Create Engine

    def createEngine(self):

        AlchemyEngine.engine = create_engine(Configuration.dbConfig["dbUrl"])
        session = scoped_session(sessionmaker(bind=AlchemyEngine.engine))
        AlchemyEngine.session = session()

    # endregion

    # region 4 Random Engine

    def snapEngine(self):

        AlchemyEngine.engine = create_engine(Configuration.dbConfig["dbUrl"])
        session = scoped_session(sessionmaker(bind=AlchemyEngine.engine))
        AlchemyEngine.snapSession = session()

        return AlchemyEngine.snapSession

    # endregion

    # region 5 Close Engine

    def closeEngine(self):

        if AlchemyEngine.session and AlchemyEngine.session.is_active:

            AlchemyEngine.session.commit()
            AlchemyEngine.session.close()

        if AlchemyEngine.snapSession and AlchemyEngine.snapSession.is_active:
                
            AlchemyEngine.snapSession.commit()
            AlchemyEngine.snapSession.close()

    # endregion  

# endregion