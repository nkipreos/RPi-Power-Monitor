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
  print line
  serial_port.flushInput()