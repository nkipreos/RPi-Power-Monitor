import hashlib
import os
import uuid

path = os.getcwd()
keys_file = path + '/keys.txt'

if not os.path.isfile(keys_file):
  f = open(keys_file, 'w+')
  f.write(hashlib.sha256(str(uuid.uuid1())).hexdigest())
  f.close()
else:
  f = open(keys_file, 'r+')
  print f.readlines()
