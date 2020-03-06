--- Connection Initialization ---
LoginRequest=net.createConnection(net.TCP, 0) 

--- HTTP Response ---
LoginRequest:on("receive", function(conn, payload)
    print("Response recieved...")
    print(payload)
    end) 

--- Disconnection ---
LoginRequest:on("disconnection", function(conn,payload)
     print("disconnecting now...")
     conn:close()
     collectgarbage();
end)

--- HTTP Request Sent ---
LoginRequest:on("sent", function(conn,payload)
     print("data sent...")
end)

--- Send HTTP Data on Connection ---
LoginRequest:on("connection", function(conn,payload)
     print("sending GET request...")
     conn:send("GET /api/2.1/rest/local_login?username=pradeep&password=inNovat1ve\r\n")     
     conn:send("HEAD / HTTP/1.0\r\n") 
     conn:send("Accept: */*\r\n") 
     conn:send("User-Agent: Mozilla/4.0 \r\n") 
     conn:send("\r\n")     
end)

--- Open HTTP Connection ----
print ("Opening HTTP Connection")
LoginRequest:connect(80,"10.0.1.5") 

--- Clear Connection Object ---
LoginRequest = nil
