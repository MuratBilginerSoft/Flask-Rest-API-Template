# region Import Packages

from flask import Flask

from P3_Scorpius.S1_App.Starter.FlaskStart import FlaskStart

# endregion

# region Create Project Flask Class

app = Flask(__name__)

# endregion

# region Start Project

FlaskStart().starter(app, __name__)

# endregion