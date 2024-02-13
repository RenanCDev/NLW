from flask import Flask as fl
from src.main.routes.tag_routes import tags_routes_bp

app = fl(__name__)

app.register_blueprint(tags_routes_bp)

