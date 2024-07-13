import os
import shutil
import subprocess
import json

def findfiles(root, source = True):
    looplist = os.listdir(root)
    for i in looplist:
        path = root+ '/' + i
        #print(path)
        if(os.path.isfile(path)):
            if not (os.path.splitext(path)[1] == ".json"):
                continue

            ext_dir = "comp_"+("/".join(i for i in root.split("/")[:-6]))

            ext_file = ext_dir+"/"+root.split("/")[-6]+".json"
            print(path)


            if not os.path.exists(ext_dir):
                os.makedirs(ext_dir)
        


            with open(path, "r", encoding="utf8") as jpiece:
                jp = json.load(jpiece)
            
            try:
                result = {element['@id']: element['#text'] for element in jp['fmg']['entries']['text']}
            except TypeError:
                try:
                    result = {jp['fmg']['entries']['text']['@id']:jp['fmg']['entries']['text']['#text']}
                except KeyError:
                    continue   
            except KeyError:
                continue            


            origin = os.path.splitext("N://"+("/".join(i for i in path.split("/")[-6:])))[0]
            jc = {origin:result}
            
            if not os.path.exists(ext_file):
                with open(ext_file, "w", encoding="utf8") as jfull:
                    json.dump(jc, jfull)
                continue


            with open(ext_file, "r", encoding="utf8") as jfull:
                jf = json.load(jfull)
            jf.update(jc)

            with open(ext_file, "w", encoding="utf8") as jfull:
                json.dump(jf, jfull)


        else:
            findfiles(path,source = False)
            





if __name__ == "__main__":

    jp = {"fmg": {"compression": "None", "version": "DarkSouls3", "bigendian": "False", 
                  "entries": {
                      "text": {"@id": "9", "#text": "asd"}
                      
                      }}}
    root = "json_ext_ext_msg"
    findfiles(root)

