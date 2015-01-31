import ConfigParser
import os
import serial
import requests
import json
from time import gmtime, strftime

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
serial_port.write("4b\r\n") # Configures RF12 for 433 MHz

######################
# Get and Parse Data #
######################

def getAndParseData(data):
  return int(data[1]), int(data[2]) + int(data[3])*255, int(data[4]) + int(data[5])*255, int(data[6]) + int(data[7])*255, int(data[8]) + int(data[9])*255, int(data[10]) + int(data[11])*255, int(data[12]) + int(data[13])*255

#######################
# Send Data to Server #
#######################

def sendData(json_data, channel_id):
  headers = {'Content-Type': 'application/json', 'REMOTE-DEVICE-ID': remote_device_id, 'STREAM-ID': channel_id}
  req = requests.post("http://173.255.205.163:40500/api/new_data", data=json.dumps(json_data), headers=headers)
  return req.status_code


#############
# Main Loop #
#############

while 1:
  serial_port.flushInput()
  while serial_port.inWaiting() == 0:
    pass
  line = serial_port.readline()
  data = line.split(" ")
  node_id, ch1_data, ch2_data, ch3_data, ch4_data, ch5_data, ch6_data = getAndParseData(data)
  current_time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
  print sendData({'value': ch1_data, 'measured_at': current_time}, ch1_id)
  print str(ch1_data)
  serial_port.flushInput()