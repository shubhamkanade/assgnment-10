from sys import *
import os

def Displayfile(path):
	
	flag=os.path.isabs(path)
	
	if flag==False:
		path=os.path.abspath(path)
		
	flag=os.path.isdir(path)
	
	if flag:
		for folder,subfolder,files in os.walk(path):
			print("Folder name "+folder)
			for fi in files:
				if fi.endswith(".txt"):
					print(fi)

def main():
		Displayfile(argv[1])

main()		
	
