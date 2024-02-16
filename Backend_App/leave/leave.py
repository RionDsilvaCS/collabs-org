from flask import Blueprint

leave_blueprint = Blueprint('leave_blueprint', __name__)

@leave_blueprint.route('/')
def test():
    return "leave route"
