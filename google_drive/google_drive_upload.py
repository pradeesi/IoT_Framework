import inspect, os
from sys import platform as _platform
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

from settings.parseSettings import get_Settings
GOOGLE_DRIVE_Settings = get_Settings('GOOGLE_DRIVE')

class gDrive:

#================================================================================
#Get Google Drive Authentication Token
#================================================================================
	def get_GoogleAuth(self):
		gauth = GoogleAuth()
		
		#Locate File in this directory.
		Dir_Path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) 
		Credentials_File =  os.path.join(Dir_Path, 'gDriveCred.txt')
		
		# Try to load saved client credentials
		gauth.LoadCredentialsFile(Credentials_File)

		if gauth.credentials is None:
			# Authenticate if they're not there
			if (_platform == "win32") or (_platform == "darwin"):
				#Use Web Browser to Authenticate
				gauth.LocalWebserverAuth()
			else:
				#Use CLI to Authenticate
				gauth.CommandLineAuth() 
				
			# Save the current credentials to a file
			gauth.SaveCredentialsFile(Credentials_File)
			
			#Invoke the function again (recursion)
			gauth = get_GoogleAuth()
			
		elif gauth.access_token_expired:
			# Refresh them if expired
			gauth.Refresh()
		else:
			# Initialize the saved creds
			gauth.Authorize()
			
		#return object	
		return gauth
#================================================================================


	def __init__(self):
		gAuth = self.get_GoogleAuth()
		self.gDrive = GoogleDrive(gAuth)
#================================================================================


			
	#Pass Folder id 'root' if you want to see folders in root
	def get_GDrive_Folder_List(self, gDrive_Parent_folder_ID=None):
		if gDrive_Parent_folder_ID != None:
			gDrive_Query = {'q': "'" + gDrive_Parent_folder_ID + "'" + """ in parents and trashed=false and mimeType='application/vnd.google-apps.folder'""", 'fields': 'items/id, items/title'}
		else:
			gDrive_Query = {'q': """trashed=false and mimeType='application/vnd.google-apps.folder'""", 'fields': 'items/id, items/title'}
			
		file_list = self.gDrive.ListFile(gDrive_Query).GetList()
		for file1 in file_list:
			print('title: %s, id: %s' % (file1['title'], file1['id']))
#================================================================================	
		
		
	def get_GDrive_Folder_ID(self, gDrive_Folder_Name, gDrive_Parent_folder_ID=None):
		if gDrive_Parent_folder_ID != None:
			gDrive_Query = {'q': "'" + gDrive_Parent_folder_ID + "'" + """ in parents and trashed=false and mimeType='application/vnd.google-apps.folder' and title='""" + gDrive_Folder_Name + "'", 'fields': 'items/id, items/title' }

		else:
			gDrive_Query = {'q': """trashed=false and mimeType='application/vnd.google-apps.folder' and title='""" + gDrive_Folder_Name + "'", 'fields': 'items/id, items/title' }

		file_list = self.gDrive.ListFile(gDrive_Query).GetList()
		
		for file in file_list:
			if gDrive_Folder_Name == file['title']:
				return file['id']
				break
		return None
#================================================================================


	def create_GDrive_Folder(self, Folder_Name, Parent_Folder_ID='root'):
		#check if Folder already Exists or not
		gDrive_Folder_ID = self.get_GDrive_Folder_ID(Folder_Name, Parent_Folder_ID)
		
		if gDrive_Folder_ID == None:
			#Create Folder if it doesn't exists
			gDrive_Folder = self.gDrive.CreateFile({'title': Folder_Name, 
									"parents":  [{"id": Parent_Folder_ID}], 
									"mimeType": "application/vnd.google-apps.folder"})
			gDrive_Folder.Upload()
			return gDrive_Folder['id']
		else:
			#return folder ID
			return gDrive_Folder_ID
#================================================================================		


	def get_GDrive_File_List(self, gDrive_Parent_folder_ID=None):
		if gDrive_Parent_folder_ID != None:
			gDrive_Query = {'q': "'" + gDrive_Parent_folder_ID + "'" + """ in parents and trashed=false and mimeType!='application/vnd.google-apps.folder'""", 'fields': 'items/id, items/title, items/mimeType'}
		else:
			gDrive_Query = {'q': """trashed=false and mimeType!='application/vnd.google-apps.folder'""", 'fields': 'items/id, items/title, items/mimeType'}
			
		file_list = self.gDrive.ListFile(gDrive_Query).GetList()
		for file in file_list:
			print('title: %s, id: %s , type: %s' % (file['title'], file['id'], file['mimeType']))
#================================================================================


	def get_GDrive_File_ID(self, gDrive_File_Name, gDrive_Parent_folder_ID=None):
		if gDrive_Parent_folder_ID != None:
			gDrive_Query = {'q': "'" + gDrive_Parent_folder_ID + "'" + """ in parents and trashed=false and mimeType!='application/vnd.google-apps.folder' and title='""" + gDrive_File_Name + "'", 'fields': 'items/id, items/title'}

		else:
			gDrive_Query = {'q': """trashed=false and mimeType!='application/vnd.google-apps.folder' and title='""" + gDrive_File_Name + "'", 'fields': 'items/id, items/title' }

		file_list = self.gDrive.ListFile(gDrive_Query).GetList()
		
		for file in file_list:
			if gDrive_File_Name == file['title']:
				return file['id']
				break
		return None
#================================================================================


	def upload_File(self, file_Name, file_Path, Parent_Folder_ID='root'):
		File_Attrib = {}
		File_Attrib['title']=file_Name   #os.path.basename(file_Name)
		File_Attrib['parents']=[{"kind": "drive#fileLink","id": Parent_Folder_ID}]
		
		#file_Path = os.path.join(GOOGLE_DRIVE_Settings['LOCAL_DIR_PATH'],file_Name)
		file = self.gDrive.CreateFile(File_Attrib)
		file.SetContentFile(file_Path)
		file.Upload()
		return file['id']

#================================================================================

	def __del__(self):
		del self
#================================================================================	

