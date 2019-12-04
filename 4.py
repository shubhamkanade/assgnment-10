from sys import *
import os
import shutil
import errno

def Directorycopy(path,value,ext):
	print("In fucntion")
		
	path=os.path.abspath(path)
	for folder ,subfolder,files in os.walk(path):
		for fi in files:
			newpath=folder+"/"+fi
			if not os.path.exists(value):
				try:
					os.makedirs(value, 0o700)
					print(os.path.abspath(value))
					#os.makedirs(value, 0o700)
					#print(os.path.abspath(value))
					if(newpath.endswith(ext)):
						shutil.copy(newpath,os.path.abspath(value))
				except OSError as e:
					if e.errno != errno.EEXIST:
						pass
			else:
				if(newpath.endswith(ext)):
					shutil.copy(newpath,os.path.abspath(value))
				
	#shutil.copytree(path,value)		
def main():
	
	Directorycopy(argv[1],argv[2],argv[3])
	
	
if __name__=="__main__":
	
	main()
