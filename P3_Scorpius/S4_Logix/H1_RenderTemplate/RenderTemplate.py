from flask import render_template

from P3_Scorpius.S1_App.Router.RouteUrl import RouteUrl

class RenderTemplate:

    def page(self, urlName, **kwargs):

        return render_template(RouteUrl().routeUrl[urlName], **kwargs)
    
    def partial(self, partialString, **kwargs):
        
        return render_template(partialString, **kwargs)
    
    