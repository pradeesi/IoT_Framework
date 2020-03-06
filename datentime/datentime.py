import time
from datetime import datetime, date
from settings.parseSettings import get_Settings

dt_Settings = get_Settings('DATE_TIME')

class dt:
	
	def __init__(self):
		pass
		
	def get_datetime_str(self):
		return (datetime.today()).strftime(dt_Settings['DATE_TIME_FORMAT'])
				
	def get_datetime(self):
		return datetime.today()
		
	def get_date_str(self):
		return (datetime.today()).strftime(dt_Settings['DATE_FORMAT'])
		
	def get_date(self):
		return date.today()
		
	def get_time_str(self):
		return (datetime.today()).strftime(dt_Settings['TIME_FORMAT'])
	
	def get_time(self):
		return time.time()
#============================================================================
# 	DB Date Entries
#============================================================================
	#Date Format Used for DB entries
	def get_DB_datetime_str(self):
		return (datetime.today()).strftime(dt_Settings['DB_DATE_FORMAT'])
#============================================================================
		
#============================================================================
#	Google Drive Upload
#============================================================================
	#Date Used for Google Drive Day Folder (RaPi Camera File Upload)
	def get_GDrive_Day_Folder_datetime_str(self, motion_Event_Date):
		motion_Date = datetime.strptime(motion_Event_Date, dt_Settings['DB_DATE_FORMAT'])
		return (motion_Date).strftime(dt_Settings['GOOGLE_DRIVE_DAY_FOLDER_NAME_FORMAT'])	
		
	#Date Used for Google Drive Motion Event Folder (RaPi Camera File Upload)
	def get_GDrive_Motion_Event_Folder_datetime_str(self, motion_Event_Date):
		motion_Date = datetime.strptime(motion_Event_Date, dt_Settings['DB_DATE_FORMAT'])
		return (motion_Date).strftime(dt_Settings['GOOGLE_DRIVE_MOTION_EVENT_FOLDER_NAME_FORMAT'])			
		
#============================================================================	

#============================================================================

	#Date Used for Video (YouTube and Google Drive) Motion Event
	def get_Video_Name_datetime_str(self, motion_Event_Date):
		motion_Date = datetime.strptime(motion_Event_Date, dt_Settings['DB_DATE_FORMAT'])
		return (motion_Date).strftime(dt_Settings['VIDEO_FILE_NAME_FORMAT'])			
		

#============================================================================
	
		
	def convert_datetime_str_to_dateObj(self,strDate):
		return datetime.strptime(strDate, dt_Settings['DATE_TIME_FORMAT'])
		
	def convert_DB_datetime_str_to_dateObj(self,strDate):
		return datetime.strptime(strDate, dt_Settings['DB_DATE_FORMAT'])		
		
	def get_date_str_from_datetime_str(self,strDate):
		return (self.convert_datetime_str_to_dateObj(strDate)).strftime(dt_Settings['DATE_FORMAT'])
	
	def get_time_str_from_datetime_str(self,strDate):
		return (self.convert_datetime_str_to_dateObj(strDate)).strftime(dt_Settings['TIME_FORMAT'])
		
	def datetime_diff(self, strDate1, strDate2):
		return self.convert_datetime_str_to_dateObj(strDate1) - self.convert_datetime_str_to_dateObj(strDate2)
	
	def datetime_compare(self, strDate1, strDate2):
		if self.convert_datetime_str_to_dateObj(strDate1) > self.convert_datetime_str_to_dateObj(strDate2):
			return strDate1
		else:
			return strDate2
			
	def __del__(self):
		pass