import os
import shutil
import subprocess
import xmltodict, json

def findfiles(root, source = True):
    looplist = os.listdir(root)
    for i in looplist:
        path = root+ '/' + i
        #print(path)
        if(os.path.isfile(path)):
            print(os.path.splitext(path))
            if not (os.path.splitext(path)[1] == ".xml"):
                continue

            ext_dir = "json_"+root
            ext_file = "json_"+path

            

            if not os.path.exists(ext_dir):
                os.makedirs(ext_dir)
            shutil.copy(path, ext_dir)
        
            with open(ext_file, "r", encoding="utf8") as xml:
                dic = xmltodict.parse(xml.read())
            jsonformat = json.dumps(dic)

            with open(os.path.splitext(ext_file)[0]+".json","w") as jfile:
                jfile.write(jsonformat)
            

            os.remove(ext_file)
        else:
            findfiles(path,source = False)
            





if __name__ == "__main__":
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    os.chdir("../")


    #root = str(input("Name the folder that will be looped: "))
    root = "Xml_msg"
    findfiles(root)
