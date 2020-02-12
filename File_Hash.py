import hashlib
import os
from shutil import copy
from time import sleep

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
    
mind = md5(path)#saving start hash_sum
i=0#variable to exclude spam
while True:
    if(md5(path)==mind):
        sleep(5)
        if i==0:
            i+=1
            print('Listening..')
        else:
            pass
    else:
        i=0
        s = path.split('\\')
        copy(path, end_path+'\\'+s[-1])
        mind = md5(path)
        print("reWrite")

