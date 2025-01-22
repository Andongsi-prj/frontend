from .site_route import site_route
from .pipe_route import pipe_route


blueprints = [
   (site_route,"/"),
   (pipe_route,"/api/pipe"),
   
]


def register_blueprints(app):
    for blueprint,prefix in blueprints:
        app.register_blueprint(blueprint,url_prefix=prefix)