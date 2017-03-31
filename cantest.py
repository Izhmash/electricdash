import can
import socket
import struct

fmt = "<IB3x8s"

can_interface = 'can0'
bus = can.interface.Bus(can_interface, bustype='socketcan_ctypes')

message1 = bus.recv()
message2 = bus.recv()

id1 = message1.arbitration_id
id2 = message2.arbitration_id

print message1
print(id1)
print message2
print(id2)

if id1 > id2:
	temp = message1
	message1 = message2
	message2 = temp
	
rpm = (message1.data[1]*256) + message1.data[0] # rpm data attempt
print 'RPM: ', rpm, ' rev/min'

amps = (message1.data[3]*256) + message1.data[2]/10.0 # current data attempt
print 'Current: ', amps, ' amps'

volts = ((message1.data[5]*256) + message1.data[4])/10.0 # current data attempt
print 'Voltage: ', volts, ' volts'
