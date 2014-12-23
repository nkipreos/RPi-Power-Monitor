import hashlib
import os
import uuid
import ConfigParser

path = os.getcwd()
conf_file = path + '/config/config.ini'
conf = ConfigParser.ConfigParser()
conf.read(conf_file)

if conf.get("Config","deviceexists") == 'False':
  conf.set("Config","deviceexists","True")
  conf.set("Config","apikey",hashlib.sha256(str(uuid.uuid1())).hexdigest())
  conf.set("Config","streamid","<id_del_stream>")
  with open(conf_file, 'wb') as configfile:
    conf.write(configfile)
else:
  print conf.get("Config", "apikey") 
