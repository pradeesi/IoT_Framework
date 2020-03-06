from flask_app import app
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template




############################################################
######## HOUSE SECTION
############################################################

#=================== HOUSE TAB ======================
@app.route('/tab_House', methods=['GET'])
def tab_House():
	error = None
	if request.method == 'GET':
		return render_template('house/tab_House.htm', error=error)
#=====================================================	
	

#=================== ADD HOUSE ======================
@app.route('/add_House', methods=['GET', 'POST'])
def add_House():
	error = None
	if request.method == 'GET':
		Operation="add"
		return render_template('house/add_House.htm', Operation=Operation, error=error)
#=====================================================	

#=================== DELETE HOUSE ======================
@app.route('/del_House', methods=['GET', 'POST'])
def del_House():
	error = None
	if request.method == 'GET':
		Operation="del"
		return render_template('house/add_House.htm', Operation=Operation, error=error)
		
#=====================================================	

#=================== VIEW HOUSE ======================
@app.route('/view_House', methods=['GET', 'POST'])
def view_House():
	error = None
	if request.method == 'GET':
		Operation="view"
		return render_template('house/add_House.htm', Operation=Operation, error=error)
		
#=====================================================	

#=================== EDIT HOUSE ======================
@app.route('/edit_House', methods=['GET', 'POST'])
def edit_House():
	error = None
	if request.method == 'GET':
		Operation="edit"
		return render_template('house/add_House.htm', Operation=Operation, error=error)
		
#=====================================================	


############################################################		


############################################################
######## OWNER SECTION
############################################################

#=================== OWNER TAB ======================
@app.route('/tab_Owner', methods=['GET'])
def tab_Owner():
	error = None
	if request.method == 'GET':
		return render_template('tab_Owner.htm', error=error)
#=====================================================	
	

#=================== ADD OWNER ======================
@app.route('/add_Owner', methods=['GET', 'POST'])
def add_Owner():
	error = None
	if request.method == 'GET':
		return render_template('add_House.htm', error=error)
#=====================================================		



############################################################





	


