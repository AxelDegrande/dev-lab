import pyads

# connect to plc and open connection
plc = pyads.Connection('169.254.28.176.1.1', pyads.PORT_TC3PLC1)
plc.open()

# read int value by name
i = plc.read_by_name("GVL_Data.fDataA")
print(i)

# close connection
plc.close()