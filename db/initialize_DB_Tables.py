import sqlite3
import inspect, os
from settings.parseSettings import get_Settings

#Fetch DB Settings
DB_Settings = get_Settings('DATABASE')

#DB Path
DB_Dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) 
DB_Path =  os.path.join(DB_Dir, DB_Settings['DB_NAME'])

#Table Definition File Path
Table_Schema_Path = os.path.join(DB_Dir, DB_Settings['TABLE_SCHEMA_FILE'])

#Read Table Schema into a Variable
TableSchema=""
with open(Table_Schema_Path, 'r') as SchemaFile:
	TableSchema=SchemaFile.read().replace('\n', '')

#Connect or Create DB File
conn = sqlite3.connect(DB_Path)
curs = conn.cursor()

#Create Tables
sqlite3.complete_statement(TableSchema)
curs.executescript(TableSchema)

#Close DB
curs.close()
conn.close()