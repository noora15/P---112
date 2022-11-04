import os
import shutil 
source = r'C:\Users\Noona\Downloads'
destination = r'C:\Users\Noona\Desktop\PYTHON\P - 111\Document_files'


list_of_files = os.listdir(source)
print(list_of_files)

for file_name in list_of_files:
    name, extension = os.path.splitext(file_name)
    print(name)
    print(extension)
    if extension == '':
        continue
    if extension in ['.txt','.pdf','.doc','docx']:

        path1 = source + '/' + file_name                            
        path2 = destination + '/'                            
        path3 = destination + '/' +  file_name  
        print("path1 " , path1)
        print("path2 " , path2)
        print("path3 ", path3)


        if os.path.exists(path2):
          print("Moving " + file_name + ".....")
          shutil.move(path1, path3)

        else:
          os.mkdir(path2)
          print("Moving " + file_name + ".....")
          shutil.move(path1, path3)