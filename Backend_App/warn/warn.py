from flask_mail import Mail, Message 
from config import app
from flask import Blueprint


warn_blueprint = Blueprint('warn_blueprint', __name__)

@warn_blueprint.route("/test") 
def test(): 
     
    return 'test warn'


@warn_blueprint.route("/push-msg") 
def push_msg(): 
    
    msg = Message( 
                'Hello', 
                sender ='puneethreddy1575@gmail.com', 
                recipients = ['dsilvarion@gmail.com'] 
                ) 
    msg.body = 'Hello Flask message sent from Flask-Mail'
    # mail.send(msg) 
    return 'Sent'