from db.db_operations import DatabaseManager
from datentime.datentime import dt
import threading, json, time, os
from datetime import datetime, date
from decimal import Decimal
import picamera

#Read Settings
from settings.parseSettings import get_Settings
Motion_Sensor_Settings = get_Settings('PIR')
PIR_MOTION_STATUS_HOLD_TIME = int(Motion_Sensor_Settings['MOTION_STATUS_HOLD_TIME'])

Camera_Settings = get_Settings('CAMERA')
IMAGE_FOLDER_PATH = Camera_Settings['CAMERA_DATA_PATH']

#===============================================================================
class Time_Lapse_Photo:
	
	def __init__(self):
		# Initialize Objects
		self.db_Obj = DatabaseManager()
		self.dt_Obj = dt()
		
	def get_Camera_File_Name(self):
		file_name = ((datetime.today()).strftime('%d_%b_%Y_%H_%M_%S_%f'))  + '.jpg'
		return file_name

	def capture_Frame(self, file_name):
		with picamera.PiCamera() as cam:
			time.sleep(Decimal(Camera_Settings['CAMERA_INITIALIZATION_WAIT_TIME']))
			cam.capture(file_name)
			return
		
	def start_Capture(self, motion_Start_Json_Data):
			json_Dict = json.loads(motion_Start_Json_Data)
			motion_Event_Time = self.dt_Obj.convert_DB_datetime_str_to_dateObj(json_Dict['dt'])
			No_Of_Pictures_Captured = 0
			while True:
				time_Diff = (self.dt_Obj.get_datetime()) - (motion_Event_Time)
				if int(time_Diff.seconds) < (int(PIR_MOTION_STATUS_HOLD_TIME) - Decimal(Camera_Settings['TIME_LAPSE_INTERVAL'])):	
					Image_Name = self.get_Camera_File_Name()
					Image_Path =  os.path.join(IMAGE_FOLDER_PATH, Image_Name)
					if No_Of_Pictures_Captured < int(Camera_Settings['MAX_PIC_COUNT_PER_EVENT']):
						self.capture_Frame(Image_Path)
					# Stop Capturing if MAX_PIC_COUNT_PER_EVENT has reached
					else:
						break
					No_Of_Pictures_Captured = No_Of_Pictures_Captured + 1
					self.db_Obj.add_del_update_db_record("insert into PiCamera_File_Upload_Temp_Data (SensorID, Motion_Event_Date_n_Time, FileName, FilePath, Upload_Status, No_Of_Upload_Retries, Upload_At) values (?,?,?,?,?,?,?)",[json_Dict['sid'], json_Dict['dt'], Image_Name, Image_Path, 'Pending', 0, 'GoogleDrive'])
					# Sleep for some time
					time.sleep(Decimal(Camera_Settings['TIME_LAPSE_INTERVAL']))
				else:
					break
			return

	def __del__(self):
		# Delete Objects
		del self.db_Obj
		del self.dt_Obj
#===============================================================================


def Time_Lapse_Capture_Thread(motion_Start_Json_Data):
	Obj = Time_Lapse_Photo()
	Obj.start_Capture(motion_Start_Json_Data)
	del Obj
	

# Call this Function from other module 
def start_Time_Lapse_Photo_Capture(motion_Start_Json_Data):
	time_Lapse_Thread = threading.Thread(target=Time_Lapse_Capture_Thread, args=[motion_Start_Json_Data])
	time_Lapse_Thread.start()
	return
