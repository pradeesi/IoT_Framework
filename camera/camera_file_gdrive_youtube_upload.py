from db.db_operations import DatabaseManager
from google_drive.google_drive_upload import gDrive
from datentime.datentime import dt
import time, json, os, threading
from youtube.youtube_upload import upload_Video_On_YouTube

from settings.parseSettings import get_Settings
GOOGLE_DRIVE_Settings = get_Settings('GOOGLE_DRIVE')


#========================================================================
class Upload_Camera_Files:
	
	def __init__(self):
		#Initialize Objects
		self.gdObj = gDrive()
		self.DateObj = dt()
		self.db_Obj = DatabaseManager()
	

	def get_Motion_Event_Google_Drive_Folder_ID(self, sensor_ID, motion_Event_Date):
		#Get Camera File Root Folder ID from Google Drive (Create it if it doesn't exist)
		Root_Folder_Name = GOOGLE_DRIVE_Settings['ROOT_FOLDER_FOR_UPLOADED_CAMERA_FILES']
		Root_Folder_ID = self.gdObj.create_GDrive_Folder(Root_Folder_Name)
		
		#Create a Folder with Today's Date in Root Folder inside Root Folder(if it doesn't exists)
		Today_Folder_Name = self.DateObj.get_GDrive_Day_Folder_datetime_str(motion_Event_Date)
		Today_Folder_ID = self.gdObj.create_GDrive_Folder(Today_Folder_Name, Root_Folder_ID)
		
		#Create a Folder with Sensor ID (if it doesn't exists)
		Sensor_Folder_ID = self.gdObj.create_GDrive_Folder(sensor_ID, Today_Folder_ID)
		
		#Create a Folder with Motion Event Date inside Sensor Folder
		Motion_Event_Folder_Name = self.DateObj.get_GDrive_Motion_Event_Folder_datetime_str(motion_Event_Date)
		Motion_Event_Folder_ID = self.gdObj.create_GDrive_Folder(Motion_Event_Folder_Name, Sensor_Folder_ID)
		
		self.Motion_Event_Folder_ID = Motion_Event_Folder_ID
		return Motion_Event_Folder_ID
	

	def upload_RaPi_Camera_Files(self):
		#Fetch Records
		#Records, Columns = self.db_Obj.query_records("select FileName, FilePath, Upload_Status from PiCamera_File_Upload_Temp_Data where (SensorID == ?) AND (Motion_Event_Date_n_Time == ?)", [sensor_ID, motion_Event_Date])
		Records, Columns = self.db_Obj.query_records("select id, SensorID, Motion_Event_Date_n_Time, FileName, FilePath, Upload_Status, No_Of_Upload_Retries, Upload_At from PiCamera_File_Upload_Temp_Data order by datetime(Motion_Event_Date_n_Time)")
		#If we have Records in DB
		if len(Records) > 0:

			#Upload Files one by one
			for Record in Records:
				#Set Local Variables 
				Rec_ID = Record[0]
				Sensor_ID = Record[1]
				Motion_Event_Date = Record[2]
				File_Name = Record[3]
				File_Path = Record[4]
				Upload_Status = Record[5]
				Upload_Retry_Count = int(Record[6])
				Upload_AT = (Record[7]).upper()
				Motion_Event_Folder_ID = None
				
				# Continue with logic if file is not yet uploaded
				if (Upload_Status == "Pending") or (Upload_Status == "Failed"):
					try:
						if Upload_AT == 'GOOGLEDRIVE':
							#Get the Google Drive Parent Folder ID (Pass SensorID and Motion_Event_Date_n_Time values to this function)
							Motion_Event_Folder_ID = self.get_Motion_Event_Google_Drive_Folder_ID(Sensor_ID, Motion_Event_Date)
						
						# Update DB Record with Status as "Uploading"
						self.db_Obj.add_del_update_db_record('update PiCamera_File_Upload_Temp_Data set Upload_Status=? where id=?',['Uploading',Rec_ID])
						
						try:
							if Upload_AT == 'GOOGLEDRIVE':
								# Call Google Drive Upload File Function
								self.gdObj.upload_File(File_Name, File_Path, Motion_Event_Folder_ID)
					
							if Upload_AT == 'YOUTUBE':
								#Upload on YouTube
								upload_Video_On_YouTube(File_Path,File_Name)
					
							# Delete DB Record From Table
							self.db_Obj.add_del_update_db_record('delete from PiCamera_File_Upload_Temp_Data where id=?',[Rec_ID])						
							
							# Delete File from Local Directory
							os.remove(File_Path)
						
						except IOError:
							print "Inside IO Error Block"
							#File not Found Error. Could be because of invalid Path or the file is deleted/
							# Delete DB Record From Table
							self.db_Obj.add_del_update_db_record('delete from PiCamera_File_Upload_Temp_Data where id=?',[Rec_ID])						
							
						except Exception as e:
							print "Inside Exception Block"
							# Update DB Record with Status as "Failed"
							Upload_Retry_Count = Upload_Retry_Count + 1
							self.db_Obj.add_del_update_db_record('update PiCamera_File_Upload_Temp_Data set Upload_Status=?, No_Of_Upload_Retries=? where id=?',['Failed', Upload_Retry_Count, Rec_ID])
							
					except Exception as e:
						# Update DB Record with Status as "Failed"
						Upload_Retry_Count = Upload_Retry_Count + 1						
						self.db_Obj.add_del_update_db_record('update PiCamera_File_Upload_Temp_Data set Upload_Status=?, No_Of_Upload_Retries=?  where id=?',['Failed', Upload_Retry_Count, Rec_ID])
				
		else:
			return
	
	
	def __del__(self):
		del self.gdObj
		del self.DateObj
		del self.db_Obj
#========================================================================

		

#========================================================================
# This function should be started as service from Master Function
def piCam_File_Upload_Queue_Worker():
	while True:
		# Initiate Upload Process
		gd_obj = Upload_Camera_Files()
		gd_obj.upload_RaPi_Camera_Files()
		del gd_obj
		time.sleep(5)
		
#========================================================================
			
# This function should be called to start upload service 
def PiCam_GDrive_YouTube_Upload_Service():
	print "PiCam_GDrive_Upload_Service Started..."
	data_Upload_Thread = threading.Thread(target=piCam_File_Upload_Queue_Worker, args=[])
	data_Upload_Thread.start()
	return
	
#========================================================================	

# This function will return Google Drive Folder Path where files will be uploaded
# It can be used to post an event on Facebook / Twitter
def get_GDrive_PiCam_Data_Path(sensor_ID, motion_Event_Date):
	gd_obj = Upload_Camera_Files()
	Folder_ID = gd_obj.get_Motion_Event_Google_Drive_Folder_ID(sensor_ID, motion_Event_Date)
	del gd_obj
	return "https://drive.google.com/open?id=" + str(Folder_ID)

#========================================================================