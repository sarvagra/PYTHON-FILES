# TO CREATE A FILE , SYNTAX : open("file name with extension",'w')

from msilib.schema import File


fl= open("mf1.txt",'w')
fl.close

# TO WRITE A FILE , SYNTAX : write("text to be written")

fl.write("THIS IS MY FIRST FILE")      #'w' mode replaces the existing data with new data
fl.close()

# TO CHANGE THE DIRECTORY , USE : cd <directory name>

cd newdir #type:ignore

# TO APPEND A FILE USE : write("file name with extension",'a')

fl.write("THIS TEXT IS TO BE APPENDED IN THE FILE",'a')  #'a' mode adds without replacing existing data
fl.close()

#TO READ A FILE , use read()

fl.read()

# TO READ DATA LINE BY LINE , USE : readline()

fl.readline()
fl.seek(0)    #reads full data line by line from 0th position.

# USING FOR LOOP TO READ DATA LINE BY LINE 

d= open("mf1.txt",'r')
for i in d :
    print(i)

# TO GET SIZE OF A FILE , IMPORT OS , THEN USE : os.path.getsize("file name with extension")

import os 
os.path.getsize("mf1.txt")

# TO DELETE A FILE , USE : os.remove("file name with extension")

os.remove("mf1.txt")

# TO RENAME A FILE , USE : os.rename("old file name with extension", "new file name with extension")

os.rename("mf1.txt","mf2.txt")

# TO CREATE ONE OR MULTIPLE COPIES OF A FILE , IMPORT SHUTIL THEN USE : shutil.copy("file name with extension","copied file name with extension")

import shutil
os.copy("mf2.txt","copy_mf2.txt")

# USING with open()

with open("mf2.txt",'r') as f:
    print(f.read())

    




