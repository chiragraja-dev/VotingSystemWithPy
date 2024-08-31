from app.routes.users import user_blueprint

def register_routes(app):
    app.register_blueprint(user_blueprint, url_prefix="/api/users")