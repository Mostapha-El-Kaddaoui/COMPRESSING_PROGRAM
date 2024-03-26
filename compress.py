# Importing required module
import os
name_compress=input("entrer le nom du file a compresser : ")
file_path=input("entrer le file path : ")
cmd ="tar -zcvf "+name_compress+" "+file_path
os.system(cmd)