# region Import Packages

from P3_Scorpius.S1_App.Router.BluePrintQuee import BluePrintQuee

# endregion

# region Router Class

class Router:

    # region Main Function

    def main(self,app):

        # ["BluePrintName", "ClassName", "routeUrl"]

        bluePrintParameter =  {

            "home" : ["home", "Home", "/"],
            "signup" : ["signup", "SignUp", "/auth/signup"],
            "signin" : ["signin", "SignIn", "/auth/signin"],
            "dashboard" : ["dashboard", "Dashboard", "/dashboard"],
            "confirm" : ["confirm", "Confirm", "/confirm"],
            "signout" : ["signout", "SignOut", "/auth/signout"],

            "site"  : ["site", "Site", "/sites"],
            "sitedata"  : ["sitedata", "Site", "/site"],
            "siteadd"   : ["siteadd", "Site", "/site/add"],
            "siteupdate" : ["siteupdate", "Site", "/site/update/<id>"],
            "sitedelete" : ["sitedelete", "Site", "/site/delete/<id>"],
            "sitedetail" : ["sitedetail", "Site", "/site/detail/<id>"],

        }

        for data in bluePrintParameter.values():

            bluePrint = BluePrintQuee(data[0])
            bluePrint.createBluePrint(data[0], data[2], data[1])

            app.register_blueprint(bluePrint.BluePrintBps)

    # endregion

# endregion
