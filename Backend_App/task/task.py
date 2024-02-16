from flask import Blueprint
from config import db
from flask import request
from flask import jsonify

task_blueprint = Blueprint('task_blueprint', __name__)

def distribute_tasks(member, tasks):
    assignments = {}

    sorted_member = sorted(member, key=lambda x: (x["availability"], x["role"]), reverse=True)
    sorted_tasks = sorted(tasks, key=lambda x: x["role"])

    for task in sorted_tasks:
        for member in sorted_member:
            if member["availability"] >= task["time"] and member["role"] == task["role"]:
                if member["member_id"] in assignments:
                    assignments[member["member_id"]].append(task["task_id"])
                else:
                    assignments[member["member_id"]] = [task["task_id"]]
                member["availability"] -= task["time"]
                break

    return assignments

@task_blueprint.route('/')
def test():
    return "task route"

@task_blueprint.route('/auto-assign-task', methods=['POST'])
def auto_assign_task():
    member = []
    task = []
    cursor = db.connection.cursor()
    team_id = request.json.get("team_id", None)

    query = "SELECT * FROM all_team WHERE team_id = %s"
    arg = (team_id,)
    cursor.execute(query, arg)
    for c in cursor:
        print(c)
        emp = {
            "member_id":c[2],
            "availability": 1,
            "role": c[3]
        }
        member.append(emp)
    query = "SELECT * FROM tasks WHERE team_id = %s and member_id=null"
    arg = (team_id,)
    cursor.execute(query, arg)
    for c in cursor:
        t = {
            "task_id":c[0],
            "time": c[5],
            "role": c[2]
        }
        task.append(t)
    
    print(member)
    print(task)
    
    gen_task = distribute_tasks(member=member, tasks=task)
    print(gen_task)
    for member, task_list in gen_task.items():
        print(f"{member} is assigned to {task_list}")

    return "Success"


@task_blueprint.route('/member-tasks', methods=['POST'])
def member_tasks():
    task = []
    cursor = db.connection.cursor()
    member_id = request.json.get("member_id", None)

    query = "SELECT * FROM tasks WHERE member_id = %s"
    arg = (member_id,)
    cursor.execute(query, arg)
    for c in cursor:
        t = {
            "task_id":c[0],
            "task_name": c[1],
            "task_role": c[2],
            "start_time": c[3],
            "end_time": c[4],
            "task_done": c[8],
            "task_on_time": c[9],
        }
        task.append(t)


    return jsonify(tasks=task), 200

@task_blueprint.route('/lead-tasks', methods=['POST'])
def lead_tasks():
    task = []
    cursor = db.connection.cursor()
    team_id = request.json.get("team_id", None)

    query = "SELECT * FROM tasks WHERE team_id = %s"
    arg = (team_id,)
    cursor.execute(query, arg)
    for c in cursor:
        t = {
            "task_id":c[0],
            "task_name": c[1],
            "task_role": c[2],
            "start_time": c[3],
            "end_time": c[4],
            "member_id": c[7],
            "task_done": c[8],
            "task_on_time": c[9],
        }
        task.append(t)


    return jsonify(tasks=task), 200


