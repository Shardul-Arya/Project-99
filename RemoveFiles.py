import time
import os
import shutil

def main() :
    days = 30
    deletedFiles = 0
    deletedFolders = 0
    path = "/Users/shardularya/Desktop/WhiteHatJr./Python-Files/Project-99/text.txt"
    seconds = time.time() - (days * 86400)
    if os.path.exists(path) :
        for rootFolder,folders,files in os.walk(path) :
            if (seconds >= getFileAge(rootFolder)) :
                RemoveFolder(rootFolder)
                deletedFolders = deletedFolders+1
                break
            else :
                for folder in folders :
                    folder_path = os.path.join(rootFolder,folder)
                    if seconds >= getFileAge(folder_path) :
                        RemoveFolder(folder_path)
                        deletedFolders = deletedFolders+1
                for file in files :
                    file_path = os.path.join(rootFolder,file)
                    if seconds >= getFileAge(file_path) :
                        RemoveFile(file_path)
                        deletedFiles = deletedFiles+1
                    else :
                        if seconds >= getFileAge("/Users/shardularya/Desktop/WhiteHatJr./Python-Files/Project-99/text.txt") :
                            RemoveFile("/Users/shardularya/Desktop/WhiteHatJr./Python-Files/Project-99/text.txt")
                            deletedFiles = deletedFiles + 1
    else :
        print("File Doesn't Exist")
        print(deletedFiles)
        print(deletedFolders)

#                    else :
#                        if seconds >= getFileAge(path) :
#                            RemoveFile(path)

def RemoveFolder(path) :
    if not shutil.rmtree(path) :
        print(f"{path} has been removed successfully")
    else :
        print(f"Unable to delete"+path)

def RemoveFile(path) :
    if not os.remove(path) :
        print(f"{path} has been removed successfully")
    else :
        print(f"Unable to delete"+path)

def getFileAge(path) :
    ctime = os.stat(path).st_ctime
    return ctime