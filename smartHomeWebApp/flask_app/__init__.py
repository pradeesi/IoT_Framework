# Import Packages
from flask import Flask, session


from application.authentication.authentication import bp_Authentication
from application.administration.administration import bp_Administration
	 
# Create application
app = Flask(__name__)


# Set App Config from settings file
app.config.from_pyfile("settings.cfg")

# flask-login
from flask_login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)


# Register Bluprints
app.register_blueprint(bp_Authentication)
app.register_blueprint(bp_Administration)


# Make session permanent 
#(Timeout Value and Session Refresh settings are in "settings.cfg" file)
@app.before_request
def make_session_permanent():
    session.permanent = True