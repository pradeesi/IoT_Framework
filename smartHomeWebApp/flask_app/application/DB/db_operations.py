import sqlite3
import inspect, os
from settings.parseSettings import get_Settings

DB_Settings = get_Settings('DATABASE')

DB_Dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) 
DB_File = "UserDB"

class DatabaseManager():
	def __init__(self):
		self.conn = sqlite3.connect(DB_File)
		self.conn.execute('pragma foreign_keys = on')
		self.conn.commit()
		self.cur = self.conn.cursor()
		
	def query_records(self, sql_query, args=(), single_record=False):
		records = []
		self.cur.execute(sql_query, args)
		if single_record == True:
			records = self.cur.fetchone()
		else:
			records = self.cur.fetchall()			
		col_names = list(map(lambda x: x[0], self.cur.description))
		return records, col_names
		
	def add_del_update_db_record(self, sql_query, args=()):
		self.cur.execute(sql_query, args)
		self.conn.commit()
		return

	def __del__(self):
		self.cur.close()
		self.conn.close()
		

