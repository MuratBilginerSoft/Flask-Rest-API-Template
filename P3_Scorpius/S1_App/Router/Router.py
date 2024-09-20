# region Import Packages

from P3_Scorpius.S1_App.Router.BluePrintQuee import BluePrintQuee

# endregion

# region Router Class

class Router:

    # region Main Function

    def main(self,app):

        # ["BluePrintName", "UrlKey", "ClassName", "routeUrl"]

        bluePrintParameter =  {

            "home" : ["home", "home", "Home", "/"],
            "signup" : ["signup", "signup", "SignUp", "/auth/signup"],
            "signin" : ["signin", "signin", "SignIn", "/auth/signin"],
            "dashboard" : ["dashboard", "dashboard", "Dashboard", "/dashboard"],
            "confirm" : ["confirm", "confirm", "Confirm", "/confirm"],
            "signout" : ["signout", "signout", "SignOut", "/auth/signout"],

            "site"  : ["site", "site", "Site", "/sites"],
            "sitedata"  : ["sitedata", "sitedata", "Site", "/site"],
            "siteadd"   : ["siteadd",  "siteadd",  "Site", "/site/add"],
            "siteupdate" : ["siteupdate", "siteupdate", "Site", "/site/update/<id>"],
            "sitedelete" : ["sitedelete", "sitedelete", "Site", "/site/delete/<id>"],
            "sitedetail" : ["sitedetail", "sitedetail", "Site", "/site/detail/<id>"],

        }

        for data in bluePrintParameter.values():

            bluePrint = BluePrintQuee(data[0])
            bluePrint.createBluePrint(data[0], data[3], data[2], data[1])

            app.register_blueprint(bluePrint.BluePrintBps)

    # endregion

# endregion
