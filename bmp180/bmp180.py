import json
from settings.parseSettings import get_Settings
from datentime.datentime import dt
import Adafruit_BMP.BMP085 as BMP085

BMP180_Settings = get_Settings('BMP180')

def read_BMP180():
	dt_Obj = dt()	
	data = {}
	
	sensor = BMP085.BMP085()
	
	data['sid'] = str(BMP180_Settings['SENSOR_ID'])
	data['dt'] = dt_Obj.get_DB_datetime_str()
	data['pres'] = format(sensor.read_pressure())
	data['pres_at_sea_level'] = '{0:0.2f}'.format(sensor.read_sealevel_pressure())
	data['alti'] = '{0:0.2f}'.format(sensor.read_altitude())
	data['temp'] = '{0:0.2f}'.format(sensor.read_temperature())
	
	json_data = json.dumps(data)
	del dt_Obj
	return json_data