import os
import shutil
import subprocess

def findfiles(root, source = True):
    looplist = os.listdir(root)
    for i in looplist:
        path = root+ '/' + i
        if(os.path.isfile(path)):
            print(os.path.splitext(path))
            if not (os.path.splitext(path)[1] == ".dcx"):
                continue

            ext_dir = "ext_"+root
            ext_file = "ext_"+path

            if not os.path.exists(ext_dir):
                os.makedirs(ext_dir)
            shutil.copy(path, ext_dir)
            p = subprocess.Popen(["C:/Users/Higor/Desktop/Yabber 1.3.1/Yabber.exe",ext_file])
            returncode = p.wait()
            os.remove(ext_file)
        else:
            findfiles(path,source = False)
            





if __name__ == "__main__":
    root = str(input("Name the folder that will be looped: "))
    findfiles(root)
