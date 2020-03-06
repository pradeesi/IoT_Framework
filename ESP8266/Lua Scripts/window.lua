-----------------------------------------------
--- WIFI CONFIGURATION ---
WIFI_SSID = "joker"
WIFI_PASSWORD = "avengers"
WIFI_SIGNAL_MODE = wifi.PHYMODE_N

--- IP CONFIG (Leave blank to use DHCP) ---
ESP8266_IP=""
ESP8266_NETMASK=""
ESP8266_GATEWAY=""

--- Define GPIO Pin # ---
local int GPIO_PIN1 = 5
-----------------------------------------------

-- Connect to the wifi network
wifi.setmode(wifi.STATION) 
wifi.setphymode(WIFI_SIGNAL_MODE)
wifi.sta.config(WIFI_SSID, WIFI_PASSWORD) 
wifi.sta.connect()

if ESP8266_IP ~= "" then
    wifi.sta.setip({ip=ESP8266_IP,netmask=ESP8266_NETMASK,gateway=ESP8266_GATEWAY})
end

-----------------------------------------------

-- Interrupt Call/Function (For Posting Status of GPIO Pin)
function onChange()
    print('Pin Status Changed '.. gpio.read(GPIO_PIN1))
end

-- Configure GPIO Interrupt for GPIO_PIN1
gpio.mode(GPIO_PIN1, gpio.INT, gpio.PULLUP)
gpio.trig(GPIO_PIN1, 'both' , onChange)

-----------------------------------------------

-- Web Server GET Function (For Polling GPIO Status over HTTP)
srv=net.createServer(net.TCP) 
srv:listen(80,function(conn) 
    conn:on("receive",function(client,request) 
    client:send(tostring(gpio.read(GPIO_PIN1)));
    client:close();
    collectgarbage();
    end) 
end)

-----------------------------------------------