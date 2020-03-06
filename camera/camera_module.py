import picamera
from datetime import datetime, date
import time

from settings.parseSettings import get_Settings
Camera_Settings = get_Settings('CAMERA')


class camera_module:
	
	def __init__(self):
		#Initialize Camera Object
		self.Camera_Obj = picamera.PiCamera()
		
		#Set Camera Settings
		self.Camera_Obj.resolution = tuple([int(s) for s in Camera_Settings['RESOLUTION'].split(',')])
		self.Camera_Obj.sharpness = int(Camera_Settings['SHARPNESS'])
		self.Camera_Obj.contrast = int(Camera_Settings['CONTRAST'])
		self.Camera_Obj.brightness = int(Camera_Settings['BRIGHTNESS'])
		self.Camera_Obj.saturation = int(Camera_Settings['SATURATION'])
		self.Camera_Obj.ISO = int(Camera_Settings['ISO'])
		self.Camera_Obj.video_stabilization = True if (Camera_Settings['VIDEO_STABILIZATION']).title() == 'True' else False
		self.Camera_Obj.exposure_compensation = int(Camera_Settings['EXPOSURE_COMPENSATION'])
		self.Camera_Obj.exposure_mode = Camera_Settings['EXPOSURE_MODE']
		self.Camera_Obj.meter_mode = Camera_Settings['METER_MODE']
		self.Camera_Obj.awb_mode = Camera_Settings['AWB_MODE']
		self.Camera_Obj.image_effect = Camera_Settings['IMAGE_EFFECT']
		self.Camera_Obj.color_effects = None if (Camera_Settings['COLOR_EFFECTS']).title() == 'None' else Camera_Settings['COLOR_EFFECTS']
		self.Camera_Obj.rotation = int(Camera_Settings['ROTATION'])
		self.Camera_Obj.hflip =  True if (Camera_Settings['HFLIP']).title() == 'True' else False
		self.Camera_Obj.vflip =  True if (Camera_Settings['VFLIP']).title() == 'True' else False
		self.Camera_Obj.crop = tuple([float(s) for s in Camera_Settings['CROP'].split(',')])
		return


	def get_Camera_File_Name(self):
		base_path = Camera_Settings['CAMERA_DATA_PATH']
		file_Path = (datetime.today()).strftime('%d_%b_%Y_%H_%M_%S_%f')
		return file_Path

	
	def capture_Image(self):
		file_Name = self.get_Camera_File_Name() + '.jpg'
		self.Camera_Obj.capture(file_Name)
		return file_Name

	
	def capture_Video(self, duration_in_sec):
		file_Name = self.get_Camera_File_Name() + '.h264'
		self.Camera_Obj.start_recording(file_Name)
		time.sleep(duration_in_sec)
		self.Camera_Obj.stop_recording()
		return file_Name		
		
	def __del__(self):
		del self.Camera_Obj
		return
