from camera.video_stream_encoder import capture_MP4_Video
from db.db_operations import DatabaseManager
from datentime.datentime import dt
import threading, json

#Read Settings
from settings.parseSettings import get_Settings
Motion_Sensor_Settings = get_Settings('PIR')
PIR_MOTION_STATUS_HOLD_TIME = int(Motion_Sensor_Settings['MOTION_STATUS_HOLD_TIME'])

Camera_Settings = get_Settings('CAMERA')
Video_Upload_Location = (Camera_Settings['VIDEO_UPLOAD_AT']).upper()


#====================================================================================
def capture_and_add_to_upload_queue(motion_Start_Json_Data):
	
	#Read Sensor Data
	json_Dict = json.loads(motion_Start_Json_Data)
	SensorID = json_Dict['sid']
	Motion_Event_Date = json_Dict['dt']
	
	#Generate Video File Name
	DateObj = dt()
	File_Name = DateObj.get_Video_Name_datetime_str(Motion_Event_Date)
	del DateObj
	
	#Start Capturing Video
	File_Path = capture_MP4_Video(File_Name, int(PIR_MOTION_STATUS_HOLD_TIME)-2)

	#Insert record in upload queue
	File_Name = File_Name + r".mp4"
	db_Obj = DatabaseManager()
	db_Obj.add_del_update_db_record("insert into PiCamera_File_Upload_Temp_Data (SensorID, Motion_Event_Date_n_Time, FileName, FilePath, Upload_Status, No_Of_Upload_Retries, Upload_At) values (?,?,?,?,?,?,?)",[SensorID, Motion_Event_Date, File_Name, File_Path, 'Pending', 0, Video_Upload_Location])
	del db_Obj
	
	return
#====================================================================================	


# Call this Function from other module 
def start_Video_Capture(motion_Start_Json_Data):
	time_Lapse_Thread = threading.Thread(target=capture_and_add_to_upload_queue, args=[motion_Start_Json_Data])
	time_Lapse_Thread.start()
	return