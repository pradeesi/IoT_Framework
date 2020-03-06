from db.db_operations import DatabaseManager


class DHT22_Reports:
	
	def __init__(self):
		self.db_Obj = DatabaseManager()
		
#==== TODAY ====================================================================================
	def get_Todays_Records(self):
		Records, Columns = self.db_Obj.query_records("select * from DHT22_Data where date(Date_n_Time) == date('now')")
		return Records, Columns
				
	def get_Todays_Max(self):
		Records, Columns = self.db_Obj.query_records("select max(Temperature), max(Humidity) from DHT22_Data where date(Date_n_Time) == date('now')")
		return Records, Columns		

	def get_Todays_Min(self):
		Records, Columns = self.db_Obj.query_records("select min(Temperature), min(Humidity) from DHT22_Data where date(Date_n_Time) == date('now')")
		return Records, Columns		
		
	def get_Todays_Avg(self):
		Records, Columns = self.db_Obj.query_records("select avg(Temperature), avg(Humidity) from DHT22_Data where date(Date_n_Time) == date('now')")
		return Records, Columns	
		
		
#==== ON PREVIOUS DAYS(Data on a particular Day, back from Current Day) ==========================
	def get_Records_On_Past_Day(self, no_Of_Days_Back_From_Today):
		no_Of_Days_Back_From_Today = "-" + str(no_Of_Days_Back_From_Today) + ' Day'
		Records, Columns = self.db_Obj.query_records("select * from DHT22_Data where (date(Date_n_Time) = date('now', ?))", [no_Of_Days_Back_From_Today])
		return Records, Columns

	def get_Max_On_Past_Day(self, no_Of_Days_Back_From_Today):
		no_Of_Days_Back_From_Today = "-" + str(no_Of_Days_Back_From_Today) + ' Day'
		Records, Columns = self.db_Obj.query_records("select avg(Temperature), avg(Humidity) from DHT22_Data where (date(Date_n_Time) = date('now', ?))", [no_Of_Days_Back_From_Today])
		return Records, Columns		
		
	def get_Min_On_Past_Day(self, no_Of_Days_Back_From_Today):
		no_Of_Days_Back_From_Today = "-" + str(no_Of_Days_Back_From_Today) + ' Day'
		Records, Columns = self.db_Obj.query_records("select avg(Temperature), avg(Humidity) from DHT22_Data where (date(Date_n_Time) = date('now', ?))", [no_Of_Days_Back_From_Today])
		return Records, Columns		
	
	def get_Avg_On_Past_Day(self, no_Of_Days_Back_From_Today):
		no_Of_Days_Back_From_Today = "-" + str(no_Of_Days_Back_From_Today) + ' Day'
		Records, Columns = self.db_Obj.query_records("select avg(Temperature), avg(Humidity) from DHT22_Data where (date(Date_n_Time) = date('now', ?))", [no_Of_Days_Back_From_Today])
		return Records, Columns
		
		
#==== FROM PREVIOUS DAY TILL TODAY (Data From a particular Day (all days from that day), back from Current Day) ===============
	def get_Records_From_Back_Day(self, no_Of_Days_Back_From_Today):
		no_Of_Days_Back_From_Today = "-" + str(no_Of_Days_Back_From_Today) + ' Day'
		Records, Columns = self.db_Obj.query_records("select * from DHT22_Data where (date(Date_n_Time) >= date('now', ?))", [no_Of_Days_Back_From_Today])
		return Records, Columns

	def get_Max_From_Past_Day(self, no_Of_Days_Back_From_Today):
		no_Of_Days_Back_From_Today = "-" + str(no_Of_Days_Back_From_Today) + ' Day'
		Records, Columns = self.db_Obj.query_records("select avg(Temperature), avg(Humidity) from DHT22_Data where (date(Date_n_Time) >= date('now', ?))", [no_Of_Days_Back_From_Today])
		return Records, Columns
		
	def get_Min_From_Past_Day(self, no_Of_Days_Back_From_Today):
		no_Of_Days_Back_From_Today = "-" + str(no_Of_Days_Back_From_Today) + ' Day'
		Records, Columns = self.db_Obj.query_records("select avg(Temperature), avg(Humidity) from DHT22_Data where (date(Date_n_Time) >= date('now', ?))", [no_Of_Days_Back_From_Today])
		return Records, Columns
		
	def get_Avg_From_Past_Day(self, no_Of_Days_Back_From_Today):
		no_Of_Days_Back_From_Today = "-" + str(no_Of_Days_Back_From_Today) + ' Day'
		Records, Columns = self.db_Obj.query_records("select avg(Temperature), avg(Humidity) from DHT22_Data where (date(Date_n_Time) >= date('now', ?))", [no_Of_Days_Back_From_Today])
		return Records, Columns
#====================================================================================================	
		
	def __del__(self):
		del self.db_Obj
