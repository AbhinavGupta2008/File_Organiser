import os
import shutil
from_dir="C:/Users/HP/Downloads"
to_dir="C:/Users/HP/Downloads/docs"
listoffiles=os.listdir(from_dir)
print(listoffiles)
for file_name in listoffiles:
    name,extention=os.path.splitext(file_name)
    print(name)
    print(extention)
    if(extention==""):
        continue
    if(extention in [".pdf",".doc",".csv",".txt", ".doc", ".docx", ".pdf"]):
        path1=from_dir+"/"+file_name
        path2=to_dir+"/"+"documents"
        path3=to_dir+"/"+"documents"+file_name
        print("path",path1)
        print("path3",path3)
        if(os.path.exists(path2)):
            print("moving"+file_name)
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("moving"+file_name)
            shutil.move(path1,path3)
    
    

