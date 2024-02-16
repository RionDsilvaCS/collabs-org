from config import app, db
from auth.auth import auth_blueprint
from leave.leave import leave_blueprint
from task.task import task_blueprint
from team.team import team_blueprint
from warn.warn import warn_blueprint

app.register_blueprint(auth_blueprint, url_prefix='/user')
app.register_blueprint(task_blueprint, url_prefix='/task')
app.register_blueprint(team_blueprint, url_prefix='/team')
app.register_blueprint(leave_blueprint, url_prefix='/leave')
app.register_blueprint(warn_blueprint, url_prefix='/warn')

app.run(host='localhost', port=5000)