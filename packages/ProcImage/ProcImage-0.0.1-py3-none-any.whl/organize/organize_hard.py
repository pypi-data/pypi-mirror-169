

"""
-1 The first function: images arranges the images and then add them in 
a new folder. This function takes the path of the images folder + the name 
of the new folder in which all images will be added.

-2 The first function: files arranges files of all kinds and then add them in 
a new folder. This function takes the path of the files 
folder + the name of the new folder in which all files will be added

-3 The first function: videos arranges video clips of all kinds and then 
add them in a new folder and this function takes the path of 
the videos folder + the name of the new folder in which all videos will be added

-4 The first function: music arranges audio clips of all kinds and then add 
them in a new folder. This function takes the path of the audio files 
folder + the name of the new folder in which all audio files will be added


-5 The first function: application arranges all applications of 
all kinds and then add them in a new folder and this function 
takes the path of the applications folder + the name of the new folder in which all files and applications will be added
"""

import os , shutil
class Organize:
	""" Hardware Regulation """
	def __init__(self):
		self.condition = False

	def images(self,currnet_path ,new_folder):
		""" The function responsible for organizing the images git full path dir"""
		try :
			if not os.path.isdir(currnet_path):
				raise FileNotFoundError("Path not found :{}".format(currnet_path))

			for filename in os.listdir(currnet_path):
				if filename.endswith((
						".png" , ".jpg" , ".jpeg" , ".gif" ,
						".webp" , ".tiff" , ".psd" , ".raw" ,
						".bmp" , ".heif" , ".indd" , ".svg",
						".ai" , ".eps" 
					)):
					
					if not os.path.exists(new_folder):
						os.mkdir(new_folder)
					shutil.copy(currnet_path + '\\' + filename , new_folder)
					os.remove(currnet_path + '\\' + filename)
		except Exception as error:
			return error


	def files(self,currnet_path ,new_folder):
		""" This function organizes files git currnet path And git new folder """
		try :
			if not os.path.isdir(currnet_path):
				raise FileNotFoundError("Path not found :{}".format(currnet_path))

			for filename in os.listdir(currnet_path):
				if filename.endswith((
						".txt" , ".pdf" , ".py" , ".css" ,
						".html" , ".js" , ".cp" , ".php" ,
						".c" , ".java" , ".xlsx" , ".accdb",
						".zip" , ".war", ".docx", ".pptx"
					)):
					
					if not os.path.exists(new_folder):
						os.mkdir(new_folder)
					shutil.copy(currnet_path + '\\' + filename , new_folder)
					os.remove(currnet_path + '\\' + filename)
		except Exception as error:
			return error



	def videos(self,currnet_path ,new_folder):
		""" This function organizes Videos git currnet path And git new folder """
		try :
			if not os.path.isdir(currnet_path):
				raise FileNotFoundError("Path not found :{}".format(currnet_path))

			for filename in os.listdir(currnet_path):
				if filename.endswith((
						".webm" , ".mpg" , ".mp2" , ".mpe" ,
						".mpv" , ".ogg" , ".mp4" , ".m4p" ,
						".m4v" , ".avi" , ".wmv" , ".mov",
						".qt" , ".flv", ".swf", ".avchd"
					)):
					
					if not os.path.exists(new_folder):
						os.mkdir(new_folder)
					shutil.copy(currnet_path + '\\' + filename , new_folder)
					os.remove(currnet_path + '\\' + filename)
		except Exception as error:
			return error


	def music(self,currnet_path ,new_folder):
		""" This function organizes Music git currnet path And git new folder """
		try :
			if not os.path.isdir(currnet_path):
				raise FileNotFoundError("Path not found :{}".format(currnet_path))

			for filename in os.listdir(currnet_path):
				if filename.endswith((
						".webm" , ".mpg" , ".mp2" , ".mpe" ,
						".mpv" , ".ogg" , ".mp4" , ".m4p" ,
						".m4v" , ".avi" , ".wmv" , ".mov",
						".qt" , ".flv", ".swf", ".avchd"
					)):
					
					if not os.path.exists(new_folder):
						os.mkdir(new_folder)
					shutil.copy(currnet_path + '\\' + filename , new_folder)
					os.remove(currnet_path + '\\' + filename)
		except Exception as error:
			return error


	def applications(self,currnet_path ,new_folder):
		""" This function organizes Applications git currnet path And git new folder """
		try :
			if not os.path.isdir(currnet_path):
				raise FileNotFoundError("Path not found :{}".format(currnet_path))

			for filename in os.listdir(currnet_path):
				if filename.endswith((".exe",".dmp")):
					
					if not os.path.exists(new_folder):
						os.mkdir(new_folder)
					shutil.copy(currnet_path + '\\' + filename , new_folder)
					os.remove(currnet_path + '\\' + filename)
		except Exception as error:
			return error

