import os
import shutil
import time

path="C:/Users/gauri/OneDrive/Desktop/Python/CheckForDeletion"
for(root,folder,files) in os.walk(path):
    print(root)
    print(folder)
    print(files)
    hour=time.time()
    newTime=os.stat(path).st_ctime
    #hour-(newTime)>hour
    print(hour)
    print(newTime)
if(newTime>hour):
    shutil.rmtree(path)
else:    
      for i in folder:
        folderPath='C:/Users/gauri/OneDrive/Desktop/Python/CheckForDeletion'+i 
        folderTime=os.stat(path).st_ctime
        if(folderTime>hour):
          shutil.rmtree(folderPath)

      for i in files():
        filePath='C:/Users/gauri/OneDrive/Desktop/Python/CheckForDeletion'+i 
        fileTime=os.stat(path).st_ctime
        if(fileTime>hour):
          os.remove(filePath)
          #os.remove for files
          #shutil.rmtree for folders
        

