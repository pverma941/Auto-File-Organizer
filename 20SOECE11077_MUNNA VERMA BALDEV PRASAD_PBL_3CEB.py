#Name = Munna Verma Baldev prasad   Enrollment no.= 20SOECE11077
#Simple Python Script To arrange your files in one click
import os                                        
import glob
files_list = glob.glob("*")                         #glob function of glob module to detect all files inside current directory
extension_set = set()                               #Creating a set of extension types inside the folder to avoid duplicate entries
for file in files_list:
    extension = file.split(sep=".")
    try:
        extension_set.add(extension[1])
    except IndexError:
        continue
def createDirs():                                   #Function to create directory for each type of extension
    for dir in extension_set:
        try:
            os.makedirs(dir+"_files")
        except FileExistsError:
            continue
def arrange():                                      #Function to move files to respective folders
    for file in files_list:
        fextension = file.split(sep=".")
        try:
            os.rename(file, fextension[1]+"_files/"+file)
        except (OSError, IndexError):
            continue
#Calling the functions in order
createDirs()
arrange()