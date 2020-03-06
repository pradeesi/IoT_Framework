from db.dht22_reports import DHT22_Reports
from db.bmp180_reports import BMP180_Reports



obj= DHT22_Reports()
print obj.get_Todays_Min()
del obj


obj= BMP180_Reports()
print obj.get_Todays_Min()
del obj