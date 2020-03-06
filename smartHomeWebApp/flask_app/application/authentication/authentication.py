from flask import Blueprint, current_app, request, render_template, session, redirect, url_for



# Initialize Authentication Blueprint
bp_Authentication = Blueprint('bp_Authentication', __name__)


#=================== LOGIN SECTION ======================
@bp_Authentication.route('/login', methods=['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':		
		if request.form['username'] != current_app.config['USERNAME']:
			error = 'Invalid username'
		elif request.form['password'] != current_app.config['PASSWORD']:
			error = 'Invalid password'
		else:
			session['logged_in'] = True
			session['User'] = request.form['username']
			return render_template('administration/master_Administration.htm', error=error)
	
	return render_template('authentication/login.htm', error=error)

	
#=================== LOGOUT SECTION ======================
@bp_Authentication.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('bp_Authentication.login'))

	
#=================== Redirection ======================
@bp_Authentication.route('/')
def redirect_to_login_page():
	if session.get('logged_in'):
		return "Logged in"		
	else:
		return render_template('authentication/login.htm',error=None)

