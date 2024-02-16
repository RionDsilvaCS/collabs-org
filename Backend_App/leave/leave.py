from flask import Blueprint
from config import db
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask import jsonify
from flask import request
leave_blueprint = Blueprint('leave_blueprint', __name__)

@leave_blueprint.route('/')
def test():
    cursor = db.connection.cursor()
    username = request.json.get("registration-num", None)
    password = request.json.get("email-id", None)
    
    print(username)
    return "leave route"

@leave_blueprint.route('/create-leave-mem')
def create():
    cursor = db.connection.cursor()
    mem_id = request.json.get("mem_id", None)
    Start_date = request.json.get("Start_date", None)
    end_date = request.json.get("end_date", None)
    start_time = request.json.get("start_time", None)
    end_time = request.json.get("end_time", None)
    cursor.execute("Select * from leaves WHERE member_id = %s;"
                   "UPDATE Leaves"
                   "SET 'Approved_Request' = 'Not Approved';", (mem_id,))
    for c in cursor:
        print(c)

@leave_blueprint.route('/delete-leave-mem')
def delete_mem():
    cursor = db.connection.cursor()
    mem_id = request.json.get("mem_id", None)
    leave_id = request.json.get("leave_id", None)
    cursor.execute("Select * from leaves WHERE member_id = %s;"
                   "UPDATE Leaves"
                   "SET 'Approved_Request' = 'Not Approved';", (mem_id,))
    for c in cursor:
        print(c)

    
    return "delete route"

@leave_blueprint.route('/delete-leave-lead')
def delete_lead():
    cursor = db.connection.cursor()
    mem_id = request.json.get("mem_id", None)
    leave_id = request.json.get("leave_id", None)
    cursor.execute("Select * from leaves WHERE mem_id = %s;"
                   "UPDATE Leaves"
                   "SET 'Approved_Request' = 'Not Approved';", (mem_id,))
    for c in cursor:
        print(c)

    
    return "delete route"

@leave_blueprint.route('/approve-leave-lead')
def approve_lead():
    cursor = db.connection.cursor()
    mem_id = request.json.get("mem_id", None)
    leave_id = request.json.get("leave_id", None)
    cursor.execute("Select * from leaves WHERE member_id = %s;"
                   "UPDATE Leaves"
                   "SET 'Approved_Request' = 'Progress';", (mem_id,))
    for c in cursor:
        print(c)

    

    return "approve-leave"

@leave_blueprint.route('/approve-leave-admin')
def approve_admin():
    cursor = db.connection.cursor()
    mem_id = request.json.get("mem_id", None)
    leave_id = request.json.get("leave_id", None)
    
    cursor.execute("Select * from leaves WHERE member_id = %s;"
                   "SET 'Approved_Request' = 'Progress';"
                   "UPDATE Leaves", (mem_id,))
    for c in cursor:
        print(c)
        
    

    return "approve-leave"

@leave_blueprint.route('/reject-leave-lead', methods=['POST'])
def reject_lead():
    cursor = db.connection.cursor()
    mem_id = request.json.get("mem_id", None)
    leave_id = request.json.get("leave_id", None)
    cursor.execute("Select * from leaves WHERE member_id = %s;"
                   
                   "SET 'Approved_Request' = 'Not Approved';"
                   "UPDATE Leaves", (mem_id,))
    for c in cursor:
        print(c)

    return "reject-leave"
@leave_blueprint.route('/reject-leave-admin', methods=['POST'])
def reject_admin():
    cursor = db.connection.cursor() 
    mem_id = request.json.get("mem_id", None)
    leave_id = request.json.get("leave_id", None)
    
    cursor.execute("Select * from leaves WHERE member_id = %s;"
                   "UPDATE Leaves"
                   "SET 'Approved_Request' = 'Not Approved';", (mem_id,))
    for c in cursor:
        print(c)

    return "reject-leave"

@leave_blueprint.route('/display-leave-mem', methods=['POST'])
def display_leave_mem():
    cursor = db.connection.cursor()
    
    mem_id = request.json.get("mem_id", None)
    cursor.execute("Select * from leaves WHERE member_id = %s;"
                   "UPDATE Leaves"
                   "SET 'Approved_Request' = 'Progress';", (mem_id,))
    for c in cursor:
        print(c)

    
    return "display-leave"
@leave_blueprint.route('/display-leave-lead', methods=['POST'])
def display_leave_lead():
    cursor = db.connection.cursor()
    
    team_id = request.json.get("team_id", None)
    print(team_id)
    cursor.execute("Select * from leaves WHERE member_id = %s;"
                   "UPDATE Teams SET 'Approved_request' = 'Progress'", (team_id,))
    for c in cursor:
        print(c) 
    return "display-leave"



