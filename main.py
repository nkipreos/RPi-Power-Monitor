import ConfigParser
import os
import serial

#####################
# Get Config Values #
#####################

path = os.getcwd()
conf_file = path + '/config/config.ini'
conf = ConfigParser.ConfigParser()
conf.read(conf_file)
remote_device_id = conf.get("Config", "remote_device_id")
ch1_id = conf.get("Config", "stream1_id")
ch2_id = conf.get("Config", "stream2_id")

######################
# Config Serial Port #
######################

serial_port = serial.Serial("/dev/ttyAMA0", 9600, timeout = 1)

#############
# Main Loop #
#############

while 1:
  serial_port.flushInput()
  while serial_port.inWaiting() == 0:
    pass
  line = serial_port.readline()
  data = line.split(" ")
  node_id = data[1]
  a = int(data[2])
  b = int(data[3])
  c = int(data[4])
  d = int(data[5])
  e = int(data[6])
  f = int(data[7])
  g = int(data[8])
  h = int(data[9])
  i = int(data[10])
  j = int(data[11])
  k = int(data[12])
  l = int(data[13])
  print str(a + b*255)
  serial_port.flushInput()