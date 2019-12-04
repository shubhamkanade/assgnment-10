from sys import *
import os
from pathlib import Path

def Displayfile(path,old,new):
	
	flag=os.path.isabs(path)
	
	if flag==False:
		path=os.path.abspath(path)
		
	flag=os.path.isdir(path)
	
	if flag:
		for folder,subfolder,files in os.walk(path):
			print("Folder name "+folder)
			for fi in files:
				newpath=folder+"/"+fi
				root_path=os.path.splitext(newpath)
				if(newpath.endswith(old)):
					h1=newpath
					h2=root_path[0]+new
				#print(h1) 
					print(os.rename(h1,h2))	
def main():
		Displayfile(argv[1],argv[2],argv[3])

main()		
	
