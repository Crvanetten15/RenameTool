import os
import sys

filesInDir = []

# Symplistically it will chane the (file, new file)
def fileChange(var1, var2):
  os.rename(var1, var2)

# given (file name, .type) it will change the extension
def typeChange(var1, var2):
  file_name = var1.split('.')
  file_name = file_name[0]
  file_name = file_name + var2
  fileChange(var1, file_name)

# Give a list of the files in dir
def retrieveFiles():
  for filename in os.listdir():
    if filename in filesInDir:
      continue
    if not filename.startswith('.'):
      filesInDir.append(filename)

# Returns sorted by extension then name
def sortByType():
  filesInDir.sort(key=os.path.splitext)
  filesInDir.sort(key=lambda f: os.path.splitext(f)[1])

# Needed function to clean after manipulation
def cleanReDir(var):
  if var in filesInDir:
    filesInDir.remove(var)

# Change multiple files with the same extension to a desired name with desired extension
def mutliByTypeD(var1, var2, var3):
  uni_name = str(var1)
  type_check = str(var2)
  count = 0
  tempList = []
  for file in filesInDir:
    if "."+file.split('.')[1] == var2:
      fileChange(file, uni_name+str(count)+str(var3))
      count += 1
      tempList.append(file)
  for _ in tempList:
    if _ in filesInDir:
      filesInDir.remove(_)
  retrieveFiles()

# Change multiple files with the same extension to a desired name with Same Extension
def mutliByTypeS(var1, var2):
  uni_name = str(var1)
  type_check = str(var2)
  count = 0
  tempList = []
  for file in filesInDir:
    if "."+file.split('.')[1] == var2:

      fileChange(file, uni_name+str(count)+str(var2))
      count += 1
      tempList.append(file)
  for _ in tempList:
    if _ in filesInDir:
      filesInDir.remove(_)
  retrieveFiles()


retrieveFiles()
sortByType()

print(filesInDir)

