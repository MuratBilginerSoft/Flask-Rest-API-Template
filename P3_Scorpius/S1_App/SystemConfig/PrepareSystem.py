#region Import Package

from flask_cors import CORS

from P2_Sirius.S1_Models.M2_EntityBase.EntityBase import db

from P3_Scorpius.S6_Utils.Mapping.Configuration import Configuration
from P3_Scorpius.S1_App.Router.Router import Router
from P3_Scorpius.S3_HeroKit.HeroKit import HeroKit 

#endregion

#region PrepareSystem Class

class PrepareSystem:

    # region Init

    def __init__(self):

        # region Create Object

        self.HeroKits = HeroKit()
        self.Routers = Router()

        # endregion
    
    # endregion

    # region Starter

    def starter(self, app):

        app.config['DEBUG'] = True

        dbUrl = self.HeroKits.setDbUrl(Configuration().dbConfig["dbType"], Configuration().dbConfig["database"], Configuration().dbConfig["host"], Configuration().dbConfig["user"], Configuration().dbConfig["password"])
        
        Configuration().dbConfig["dbUrl"] = dbUrl

        app.config['SQLALCHEMY_DATABASE_URI'] = dbUrl
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

        app.static_folder = Configuration().appConfig["staticFolder"]
        app.secret_key = Configuration().appConfig["secretKey"] 

        CORS(app, resources={r"/*": {"origins": "*"}})
        app.config['CORS_HEADERS'] = 'Content-Type'
        app.config['MAX_CONTENT_LENGTH'] = 1600 * 1000 * 1000

        db.init_app(app) 
        self.Routers.main(app)
    
    # endregion

#endregion