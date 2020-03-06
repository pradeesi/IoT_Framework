drop table if exists StdTitle;
create table StdTitle (
	TitleCode text,
	Title text
);
INSERT INTO StdTitle (TitleCode, Title) VALUES ("T0", "Mr");
INSERT INTO StdTitle (TitleCode, Title) VALUES ("T0", "Mrs");
INSERT INTO StdTitle (TitleCode, Title) VALUES ("T0", "Miss");
INSERT INTO StdTitle (TitleCode, Title) VALUES ("T0", "Master");


drop table if exists StdPartsOfHouse;
create table StdPartsOfHouse (
	LocationCode text,
	Location text
);
INSERT INTO StdPartsOfHouse (LocationCode, Location) VALUES ("L0", "Master Bedroom");
INSERT INTO StdPartsOfHouse (LocationCode, Location) VALUES ("L1", "Guest Bedroom");
INSERT INTO StdPartsOfHouse (LocationCode, Location) VALUES ("L2", "Bedroom");
INSERT INTO StdPartsOfHouse (LocationCode, Location) VALUES ("L3", "Living Room");
INSERT INTO StdPartsOfHouse (LocationCode, Location) VALUES ("L4", "Dining Room");
INSERT INTO StdPartsOfHouse (LocationCode, Location) VALUES ("L5", "Bathroom");
INSERT INTO StdPartsOfHouse (LocationCode, Location) VALUES ("L6", "Kitchen");
INSERT INTO StdPartsOfHouse (LocationCode, Location) VALUES ("L7", "Study");
INSERT INTO StdPartsOfHouse (LocationCode, Location) VALUES ("L8", "Garage");
INSERT INTO StdPartsOfHouse (LocationCode, Location) VALUES ("L9", "Balcony");
INSERT INTO StdPartsOfHouse (LocationCode, Location) VALUES ("L10", "Utility Area");
INSERT INTO StdPartsOfHouse (LocationCode, Location) VALUES ("L11", "Foyer");
INSERT INTO StdPartsOfHouse (LocationCode, Location) VALUES ("L12", "Foyer");


drop table if exists StdControllerTypes;
create table StdControllerTypes (
  ControllerCode text,
  ControllerType text,
  ControllerImage text
);
INSERT INTO StdControllerTypes (ControllerCode, ControllerType) VALUES ("c0", "Raspberry Pi");
INSERT INTO StdControllerTypes (ControllerCode, ControllerType) VALUES ("c1", "Arduino");
INSERT INTO StdControllerTypes (ControllerCode, ControllerType) VALUES ("c2", "ESP8266");



drop table if exists StdControllerOS;
create table StdControllerOS (
  ControllerCode text,
  OperatingSystemCode text,
  OperatingSystem text
);
INSERT INTO StdControllerOS (ControllerCode, OperatingSystemCode, OperatingSystem) VALUES ("c0", "os0", "Raspbian");
INSERT INTO StdControllerOS (ControllerCode, OperatingSystemCode, OperatingSystem) VALUES ("c0", "os1",  "Arc Linux");
INSERT INTO StdControllerOS (ControllerCode, OperatingSystemCode, OperatingSystem) VALUES ("c0", "os2",  "Windows 10");
INSERT INTO StdControllerOS (ControllerCode, OperatingSystemCode, OperatingSystem) VALUES ("c1", "os3",  "Arduino");
INSERT INTO StdControllerOS (ControllerCode, OperatingSystemCode, OperatingSystem) VALUES ("c2", "os4",  "NodeMCU");
INSERT INTO StdControllerOS (ControllerCode, OperatingSystemCode, OperatingSystem) VALUES ("c2", "os5",  "AT Firmware");



drop table if exists StdSensorTypes;
create table StdSensorTypes (
  SensorCode text,
  SensorType text,
  SensorImage text
);
INSERT INTO StdSensorTypes (SensorCode, SensorType) VALUES ("s0", "Temperature and Humidity Sensor: DHT22");
INSERT INTO StdSensorTypes (SensorCode, SensorType) VALUES ("s1", "Pressure Sensor: BMP180");
INSERT INTO StdSensorTypes (SensorCode, SensorType) VALUES ("s2", "Light Sensor: LDR");
INSERT INTO StdSensorTypes (SensorCode, SensorType) VALUES ("s3", "Door-Windows Sensor");
INSERT INTO StdSensorTypes (SensorCode, SensorType) VALUES ("s4", "Motion Sensor");
INSERT INTO StdSensorTypes (SensorCode, SensorType) VALUES ("s5", "Noise Sensor");
INSERT INTO StdSensorTypes (SensorCode, SensorType) VALUES ("s6", "Rain Sensor");
INSERT INTO StdSensorTypes (SensorCode, SensorType) VALUES ("s7", "Camera");


drop table if exists StdApplianceTypes;
create table StdApplianceTypes (
  ApplianceCode text,
  ApplianceType text,
  ApplianceImage text
);
INSERT INTO StdApplianceTypes (ApplianceCode, ApplianceType) VALUES ("a0", "Light");
INSERT INTO StdApplianceTypes (ApplianceCode, ApplianceType) VALUES ("a1", "Fan");
INSERT INTO StdApplianceTypes (ApplianceCode, ApplianceType) VALUES ("a2", "Geyser");
INSERT INTO StdApplianceTypes (ApplianceCode, ApplianceType) VALUES ("a2", "TV");
INSERT INTO StdApplianceTypes (ApplianceCode, ApplianceType) VALUES ("a2", "Coffee Machine");



drop table if exists StdSensorDataUnit;
create table StdSensorDataUnit (
  SensorCode text,
  DataUnit text,
  UnitSymbol text
);
INSERT INTO StdSensorDataUnit (SensorCode, DataUnit, UnitSymbol) VALUES ("s0", "Centigrade", "C");
INSERT INTO StdSensorDataUnit (SensorCode, DataUnit, UnitSymbol) VALUES ("s0", "Fahrenheit", "F");
INSERT INTO StdSensorDataUnit (SensorCode, DataUnit, UnitSymbol) VALUES ("s1", "Pascal", "Pa");
INSERT INTO StdSensorDataUnit (SensorCode, DataUnit, UnitSymbol) VALUES ("s2", "Lux", "Lx");


drop table if exists StdDevicePlacement;
create table StdDevicePlacement (
  PlacementCode text,
  Placement text
);
INSERT INTO StdDevicePlacement (PlacementCode, Placement) VALUES ("p0", "Indoor");
INSERT INTO StdDevicePlacement (PlacementCode, Placement) VALUES ("p1", "Outdoor");


drop table if exists HouseMaster;
create table HouseMaster(
	HouseID INTEGER AUTO_INCREMENT PRIMARY KEY,
	Alias text,
	Locality text,
	HouseNumber text,
	Block text,
	FloorNo text,
	AddLine1 text,
	AddLine2 text,
	City text,
	State text,
	Country text,
	PostalCode text,
	RecCreationDate text,
	RecCreatedBy text,
	RecUpdationDate text,
	RecUpdatedBy text
);


drop table if exists HouseOwnerMaster;
create table HouseOwnerMaster(
	OwnerID INTEGER AUTO_INCREMENT PRIMARY KEY,
	HouseID text,
	TitleCode text,
	FirstName text,
	MiddleName text,
	LastName text,
	Gender text,
	Email text,
	MobileNo text,
	PhoneNo text,
	Address text,
	RecCreationDate text,
	RecCreatedBy text,
	RecUpdationDate text,
	RecUpdatedBy text,
	FOREIGN KEY(HouseID) REFERENCES HouseMaster(HouseID),
	FOREIGN KEY(TitleCode) REFERENCES StdTitle(TitleCode)
);


drop table if exists FloorPlanMaster;
create table FloorPlanMaster(
	LocationID INTEGER AUTO_INCREMENT PRIMARY KEY,
	HouseID text,
	LocationCode text,
	Alias text
	RecCreationDate text,
	RecCreatedBy text,
	RecUpdationDate text,
	RecUpdatedBy text,
	FOREIGN KEY(HouseID) REFERENCES HouseMaster(HouseID),
	FOREIGN KEY(LocationCode) REFERENCES StdPartsOfHouse(LocationCode)
);


drop table if exists ControllerMaster;
create table ControllerMaster(
	ControllerID INTEGER AUTO_INCREMENT PRIMARY KEY,
	Name text,
	ControllerCode text,
	LocationID text,
	PlacementCode text,
	Description text,
	Model text,
	HW_Revision text,
	HW_SerialNumber text,
	DateManufactured text,
	HostName text,
	OperatingSystemCode text,
	IPAssignment text,
	IPAdd text,
	SubMask text,
	MAC text,
	KeepAliveInterval text,
	Status text,
	Error text,
	LastMessage text,
	RecCreationDate text,
	RecCreatedBy text,
	RecUpdationDate text,
	RecUpdatedBy text,
	FOREIGN KEY(LocationID) REFERENCES FloorPlanMaster(LocationID),
	FOREIGN KEY(ControllerCode) REFERENCES StdControllerTypes(ControllerCode),
	FOREIGN KEY(PlacementCode) REFERENCES StdDevicePlacement(PlacementCode),
	FOREIGN KEY(OperatingSystemCode) REFERENCES StdControllerOS(OperatingSystemCode)
);


drop table if exists SensorMaster;
create table SensorMaster(
	SensorID INTEGER AUTO_INCREMENT PRIMARY KEY,
	Name text,
	SensorCode text,
	ControllerID text,
	LocationID text,
	Description text
	KeepAliveInterval text,
	Status text,
	Error text,
	LastMessage text,
	RecCreationDate text,
	RecCreatedBy text,
	RecUpdationDate text,
	RecUpdatedBy text,
	FOREIGN KEY(ControllerID) REFERENCES ControllerMaster(ControllerID),
	FOREIGN KEY(SensorCode) REFERENCES StdSensorTypes(SensorCode),	
	FOREIGN KEY(LocationID) REFERENCES FloorPlanMaster(LocationID)
);


drop table if exists ApplianceMaster;
create table ApplianceMaster(
	ApplianceID INTEGER AUTO_INCREMENT PRIMARY KEY,
	Name text,
	ApplianceCode text,
	ControllerID text,
	LocationID text,
	Description text
	KeepAliveInterval text,
	Status text,
	Error text,
	LastMessage text,
	RecCreationDate text,
	RecCreatedBy text,
	RecUpdationDate text,
	RecUpdatedBy text,
	FOREIGN KEY(ControllerID) REFERENCES ControllerMaster(ControllerID),
	FOREIGN KEY(ApplianceCode) REFERENCES StdApplianceTypes(ApplianceCode),
	FOREIGN KEY(LocationID) REFERENCES FloorPlanMaster(LocationID)
);




drop table if exists TemperatureData;
create table TemperatureData (
	SensorID text,
	Date_n_Time text,
	Temperature,
	FOREIGN KEY(SensorID) REFERENCES SensorMaster(SensorID)
);


drop table if exists HumidityData;
create table HumidityData (
	SensorID text,
	Date_n_Time text,
	Humidity,
	FOREIGN KEY(SensorID) REFERENCES SensorMaster(SensorID)
);


drop table if exists LightData;
create table LightData (
	SensorID text,
	Date_n_Time text,
	Light,
	FOREIGN KEY(SensorID) REFERENCES SensorMaster(SensorID)
);


drop table if exists PressureData;
create table PressureData (
	SensorID text,
	Date_n_Time text,
	Pressure,
	FOREIGN KEY(SensorID) REFERENCES SensorMaster(SensorID)
);


drop table if exists NoiseData;
create table NoiseData (
	SensorID text,
	Date_n_Time text,
	NoiseLevel,
	FOREIGN KEY(SensorID) REFERENCES SensorMaster(SensorID)
);

