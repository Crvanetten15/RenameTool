import os
import sys

inputs = sys.argv
filesInDir = []
def fileChange(var1, var2):
  os.rename(var1, var2)

def typeChange(var1, var2):
  file_name = var1.split('.')
  file_name = file_name[0]
  file_name = file_name + var2
  fileChange(var1, file_name)

def retrieveFiles():  
  for filename in os.listdir():
    if not filename.startswith('.'):
      filesInDir.append(filename)

def sortByName():
  filesInDir.sort(key=os.path.splitext)

def sortByType():
  filesInDir.sort(key=os.path.splitext)
  filesInDir.sort(key=lambda f: os.path.splitext(f)[1])

def mutliByType(var1, var2):
  uni_name = var1
  type_check = var2

  

retrieveFiles()
sortByName()
print(filesInDir)

