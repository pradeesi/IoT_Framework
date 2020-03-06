drop table if exists BMP180_Data;
create table BMP180_Data (
  id integer primary key autoincrement,
  SensorID text,
  Date_n_Time text,
  Pressure text,
  Pressure_At_Sea_Level text,
  Altitude text,
  Temperature text
);

drop table if exists DHT22_Data;
create table DHT22_Data (
  id integer primary key autoincrement,
  SensorID text,
  Date_n_Time text,
  Temperature text,
  Humidity text
);

drop table if exists LIGHT_Data;
create table LIGHT_Data (
  id integer primary key autoincrement,
  SensorID text,
  Date_n_Time text,
  Light text
);

drop table if exists Sensors;
create table Sensors (
  SensorID text primary key,
  SensorType text,
  ControllerID text,
  Location text,
  Capabilities text,
  Remarks text
);

drop table if exists Controllers;
create table Controllers (
  ControllerID text primary key,
  ControllerType text,
  Location text,
  OperatingSystem text,
  Capabilities text,
  Remarks text
);

drop table if exists PiCamera_File_Upload_Temp_Data;
create table PiCamera_File_Upload_Temp_Data (
  id integer primary key autoincrement,
  SensorID text,
  Motion_Event_Date_n_Time text,
  FileName text,
  FilePath text,
  Upload_Status text,
  No_Of_Upload_Retries integer,
  Upload_At text
);
