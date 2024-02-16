from flask import Blueprint, request
from config import db
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask import jsonify
from flask import request
team_blueprint = Blueprint('team_blueprint', __name__)

@team_blueprint.route('/')
def test():

    return "team route"

@team_blueprint.route('/')
def test():
    return "team route"


@team_blueprint.route('/assign_lead', methods=["PUT"])
def assign_lead():

    cursor = db.connection.cursor()

    data = request.get_json()
    team_id = data.get('team_id')
    team_lead_id = data.get('team_lead_id')

    
    cursor.execute("SELECT * FROM Team_Lead WHERE team_id = %s", (team_id,))
    existing_lead = cursor.fetchone()

    if existing_lead:
        cursor.close()
        return jsonify({"message": "Lead is already assigned to the team."})


    cursor.execute("INSERT INTO Team_Lead (team_id, member_id) VALUES (%s, %s)",
                    (team_id, team_lead_id))
    db.connection.commit()
    cursor.close()

    return jsonify({"message": "Lead assigned successfully to the team."})


@team_blueprint.route('/teams', methods=['POST'])
def create_team():

    cursor = db.connection.cursor()

    
    team_name = request.json['name']

    query = "INSERT INTO Team (team_name) VALUES (%s)"
    values = (team_name,)

    cursor.execute(query, values)
    db.connection.commit()

    return jsonify({
        'message': 'Team created successfully',
    })


@team_blueprint.route('/view_team', methods=['POST'])
def view_team():
    cursor = db.connection.cursor()
    
    team_id = request.json.get('id')  

    query = "SELECT * FROM All_teams WHERE team_id = (%s)"
    values = (team_id,)

    cursor.execute(query, values)
    
    team_data = cursor.fetchall()

    if team_data:
        return jsonify({
            'message': 'Team information retrieved successfully',
            'team_data': team_data
        })
    else:
        return jsonify({
            'message': 'Team not found'
        })


@team_blueprint.route('/delete_team', methods=['POST'])
def delete_team():
    cursor = db.connection.cursor()
    
    team_id = request.json.get('id')  # Use get to avoid potential KeyError

    query = "DELETE FROM Team WHERE team_id = (%s)"
    values = (team_id,)

    cursor.execute(query, values)
    
    return jsonify({
            'message': 'Team deleted successfully'
        })
   
    

@team_blueprint.route('/update_team', methods=["POST"])
def update_team():
    cursor = db.connection.cursor()
    
    data = request.get_json()
    team_id = data.get('team_id')
    new_team_name = data.get('new_team_name')

    existing_team = cursor.execute("SELECT * FROM Team WHERE team_id = :team_id", {"team_id": team_id}).fetchone()

    if not existing_team:
        return jsonify({"message": "Team not found."})

    cursor.execute("UPDATE Team SET team_name = :new_team_name WHERE team_id = :team_id",
                {"new_team_name": new_team_name, "team_id": team_id})

    return jsonify({"message": "Team updated successfully."})

      
@team_blueprint.route('/remove_lead', methods=["DELETE"])
def remove_lead():

    data = request.get_json()
    team_id = data.get('team_id')

    cursor = db.connection.cursor()

    cursor.execute("SELECT * FROM Team_Lead WHERE team_id = %s", (team_id,))
    existing_lead = cursor.fetchone()

    if not existing_lead:
        cursor.close()
        return jsonify({"message": "No team lead found for the specified team."})

    cursor.execute("DELETE FROM Team_Lead WHERE team_id = %s", (team_id,))
    db.connection.commit()
    cursor.close()

    return jsonify({"message": "Team lead removed successfully."})

    
