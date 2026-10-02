import pyads

CLIENT_NETID = "192.168.56.1.1.1"
CLIENT_IP = "192.168.1.14"
TARGET_AMS_ID = "169.254.28.176.1.1"
TARGET_USERNAME = "Administrator"
TARGET_PASSWORD = "1"
ROUTE_NAME = "routeA"


#pyads.add_route_to_plc(CLIENT_NETID, CLIENT_IP, TARGET_IP, TARGET_USERNAME, TARGET_PASSWORD, route_name=ROUTE_NAME)
pyads.open_port()
pyads.set_local_address(CLIENT_NETID)
pyads.close_port()
plc = pyads.Connection(TARGET_AMS_ID, 851)

# connect to plc and open connection
#plc = pyads.Connection('169.254.28.176.1.1', 851)
plc.open()



value = plc.read_by_name("GVL_Data.fDataA")
print(value)


plc.close()