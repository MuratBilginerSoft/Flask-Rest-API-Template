# region Import Packages

from P3_Scorpius.S1_App.SystemConfig.PrepareSystem import PrepareSystem
from P3_Scorpius.S6_Utils.Mapping.Configuration import Configuration

# endregion

#region FlaskStart Class

class FlaskStart:

    # region Init

    def __init__(self):

        self.PrepareSystems = PrepareSystem()
    
    # endregion

    # region Starter

    def starter(self, app, __name__):

        self.PrepareSystems.starter(app)

        if __name__ == "__main__":

            app.run(host='0.0.0.0', port=Configuration.appConfig["appPort"], use_reloader=True)
    
    # endregion

#endregion