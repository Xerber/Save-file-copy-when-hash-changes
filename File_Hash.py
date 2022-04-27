import hashlib
import os
from shutil import copy
from time import sleep
from datetime import datetime


#def wich calc hash_sum
def md5(fname):
  hash_md5 = hashlib.md5()
  with open(fname, "rb") as f:
    for chunk in iter(lambda: f.read(4096), b""):
      hash_md5.update(chunk)
  return hash_md5.hexdigest()
#---

path = input("Enter the path to the file: ")
end_path = input("Enter the path for backup directory: ")
if not os.path.exists(end_path):
  os.makedirs(end_path)
  print("End_path was missing but I will create :)")

filename = path.split('\\')[-1]
copy(path, f'{end_path}\startfile_{filename}')

mind = md5(path)#saving start hash_sum
while True:
  date = datetime.now().strftime('%d%m.%H%M%S')
  if(md5(path)==mind):
      sleep(1)
  else:
    copy(path, f'{end_path}\{date}{filename}')
    mind = md5(path)
