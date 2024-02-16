from flask import Blueprint

team_blueprint = Blueprint('team_blueprint', __name__)

@team_blueprint.route('/')
def test():
    return "team route"