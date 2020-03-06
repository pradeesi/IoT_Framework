
userInput = raw_input('WARNING: This script will re-initialize the Sqlite Database and DELETE all the Data. Do you want to continuw? [Y/n]')

if len(userInput) == 1 and userInput == 'Y':
	print 'Script will now delete all the Data and re-initialize Database'
	import db.initialize_DB_Tables
else:
	print 'Script will quit without performing any operation on Database.'
	


