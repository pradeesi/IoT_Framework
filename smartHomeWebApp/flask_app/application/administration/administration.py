from flask import Blueprint, current_app, request, render_template, session

from flask_login import login_required


# Initialize Authentication Blueprint
bp_Administration = Blueprint('bp_Administration', __name__)


############################################################
######## HOUSE SECTION
############################################################

#=================== HOUSE TAB ======================
@bp_Administration.route('/tab_House', methods=['GET'])
@login_required
def tab_House():
	error = None
	if request.method == 'GET':
		return render_template('administration/house/tab_House.htm', error=error)
#=====================================================	
	

#=================== ADD HOUSE ======================
@bp_Administration.route('/add_House', methods=['GET', 'POST'])
def add_House():
	error = None
	if request.method == 'GET':
		Operation="add"
		return render_template('administration/house/add_House.htm', Operation=Operation, error=error)
#=====================================================	

#=================== DELETE HOUSE ======================
@bp_Administration.route('/del_House', methods=['GET', 'POST'])
def del_House():
	error = None
	if request.method == 'GET':
		Operation="del"
		return render_template('administration/house/add_House.htm', Operation=Operation, error=error)
		
#=====================================================	

#=================== VIEW HOUSE ======================
@bp_Administration.route('/view_House', methods=['GET', 'POST'])
def view_House():
	error = None
	if request.method == 'GET':
		Operation="view"
		return render_template('administration/house/add_House.htm', Operation=Operation, error=error)
		
#=====================================================	

#=================== EDIT HOUSE ======================
@bp_Administration.route('/edit_House', methods=['GET', 'POST'])
def edit_House():
	error = None
	if request.method == 'GET':
		Operation="edit"
		return render_template('administration/house/add_House.htm', Operation=Operation, error=error)
		
#=====================================================	


############################################################		


############################################################
######## OWNER SECTION
############################################################

#=================== OWNER TAB ======================
@bp_Administration.route('/tab_Owner', methods=['GET'])
def tab_Owner():
	error = None
	if request.method == 'GET':
		return render_template('administration/owner/tab_Owner.htm', error=error)
#=====================================================	
	

#=================== ADD OWNER ======================
@bp_Administration.route('/add_Owner', methods=['GET', 'POST'])
def add_Owner():
	error = None
	if request.method == 'GET':
		return render_template('administration/house/add_House.htm', error=error)
#=====================================================		



############################################################



