from .site_route import site_route
from .pipe_route import pipe_route
from .data_route import data_route
from .login_route import login_route
from .loginck_route import loginck_route

blueprints = [
   (site_route,"/"),
   (pipe_route,"/api/pipe"),
   (data_route,"/api/data"),
   (login_route,"/api/login"),
   (loginck_route,"/api/loginck")
]


def register_blueprints(app):
    app.secret_key = 'your-secret-key-here'
    for blueprint,prefix in blueprints:
        app.register_blueprint(blueprint,url_prefix=prefix)