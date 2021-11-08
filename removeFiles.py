import os
import shutil
import time

source = input("Enter the source of the file : ")
days = input("Enter the days : ")

days = time.time();
print("Time in Seconds =", days)	

ctime = os.stat(source).st_ctime
return ctime

if os.path.exists(source):
    print( os.walk(source))
    print("path is correct")

else:
    print("The file does not exist")



for f in source:
    if ctime > days :
        os.remove(os.path.join(source, f))
        print("files are deleted")
    
    else:
         print("These files are existing in the pc less than the time you want")
        
       
