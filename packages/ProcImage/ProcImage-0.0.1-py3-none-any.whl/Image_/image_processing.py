

'''
1- The first function get_list_sorted(main_path , answer) takes the full path of the target image folder, 
and takes the user's answer, in order to arrange the images in ascending or descending order. In the entered folder

2- The second function best_image(path_image) takes the full path of the target image folder and then returns the best image in terms
of resolution and it takes only one parameter, which is the full path of the folder containing the images

3- The third function (lowest_image) takes the full path of the target image folder and then returns the lowest image in 
terms of resolution and it takes only one parameter, which is the full path of the folder containing the images It 
works in contrast to the best_image function


4- Fifth function: (get_bytes) Returns the size of the image in the device's memory, takes the full path of the target image

5- The sixth function: (check_path) It checks the image folder if the entered path is a folder and not a file. In this case, the full path
will be returned, otherwise an error message will be returned.

6- The seventh function: (get_list) It returns a list containing all the images ending with the extension 
".png", ".jpg", ".jpeg" and at the same time it is an unordered list

7- The eighth function: (calculate_selected_photos) It counts the number of images that end with the required extension, it takes the full
path of the folder for the images in addition to the name of the extension required for the calculation

8- The ninth function: (similarity_check) Its task is to check the similarity of the images, and it takes the first parameter as the 
path of the first image, and the second parameter is the path of the second image.

9- The ninth function: get_information_image fetches the image data and takes the current path of the image
'''


from PIL import Image
from PIL.ExifTags import TAGS 
from prettytable import PrettyTable
import os
import sys
import shutil


class ImageProcessing:
    """ Arrange the images in ascending or descending order """
    def __init__(self):
        self.condition_answer = False
        self.picture_dictionary = dict()
        self.list_pixels = list()
        self.list_names = list()

    def check_path(self,path):
        """ Check the full path """
        try:
            if os.path.isfile(path):
                raise FileNotFoundError("Error Please enter the correct folder path and not the file path : {}".format(path))
            elif os.path.isdir(path):
                return path

            else:
                raise NotADirectoryError("The path is incorrect or may not exist :{}".format(path))
        except Exception as erro_path:
            return erro_path
        except AttributeError as error:
            return error

   
    def get_list(self,path_img):
        """ Returns the list of all images at random, and in unordered """
        condition = False 
        if os.path.isdir(path_img):
            condition = True
        else:
            condition = False

        if condition == True:
            images = list(filter(lambda x: x.endswith((
                                                            ".jpg" , ".png" , ".gif" , ".webr" ,
                                                            ".tiff" , ".psd" , ".raw" , ".bmp",
                                                            ".heif" , ".indd" , ".jpeg", ".svg",
                                                            ".ai" , ".ebps" , ".pdf"




                                                            )), os.listdir(path_img)))

            print("Table Images".center(50))
            self.table1 = PrettyTable()
            self.table1.field_names = ["Name Image"]

            for name in images :
                 self.table1.add_row([name])
            print(self.table1);print('\n')
            print("List Images".center(50))

            return images

    
    def get_list_sorted(self, path, answer):
        """ arrange photos take Full Path And take an answer (True) , (False)"""
        self.picture_temp , self.list_result = dict(),list()
        self.table2 = PrettyTable()
        self.table2.field_names = ["Name Image","Total dimensions Image"]

        if not isinstance(answer, (bool)):
            self.condition_answer = False
        else:
            self.condition_answer = True

        if self.condition_answer == False:
            return "Please enter a Boolean value {} or {}".format(True, False)
        self.list_image = list(filter(lambda x: x.endswith((
                                                            ".jpg" , ".png" , ".gif" , ".webr" ,
                                                            ".tiff" , ".psd" , ".raw" , ".bmp",
                                                            ".heif" , ".indd" , ".jpeg", ".svg",
                                                            ".ai" , ".ebps" , ".pdf"



                                                            )), os.listdir(path)))

        for name in self.list_image:
            with Image.open(path + '\\' + name) as image :
                width , height = image.size
                self.picture_dictionary[name] = sum([width,height])


        self.list_names = sorted(self.picture_dictionary.keys(),reverse=answer)
        self.list_pixels = sorted(self.picture_dictionary.values(),reverse=answer)

        for (name,size) in zip(self.list_names,self.list_pixels):
            self.picture_temp[name] = size

        self.picture_dictionary = self.picture_temp

        for (name) in self.picture_dictionary.keys():
           self.list_result.append(name)


        print("Table Images Sorted".center(50))


        for (self.name , self.size) in self.picture_dictionary.items() :
           self.table2.add_row([self.name , self.size])
           
        print(self.table2);print('\n')
        print("List Sorted Images".center(50))

        return False if len(self.list_result) < 1 else self.list_result



    def best_image(self,path):
        """ Get Best Image """
        self.picture_best = dict()
        self.list_best = list(filter(lambda x: x.endswith((
                                                            ".jpg" , ".png" , ".gif" , ".webr" ,
                                                            ".tiff" , ".psd" , ".raw" , ".bmp",
                                                            ".heif" , ".indd" , ".jpeg", ".svg",
                                                            ".ai" , ".ebps" , ".pdf"



                                                            )), os.listdir(path)))

        for name_best in self.list_best:
            with Image.open(path + '\\' + name_best) as image :
                width , height = image.size
                self.picture_best[name_best] = sum([width,height])

        self.best_name , self.best_size = '',0
        for (name,size) in self.picture_best.items():
            if (self.best_size < size):
                self.best_size = size
                self.best_name = name 

        if (self.best_size) > 0 and (self.best_name) in self.picture_best.keys():
            print([self.best_name , self.best_size , path])
            print("\n")
            return (f"name Image :{self.best_name}\ntotal dimensions :{self.best_size} Pixel\nLocation :{path}")


    def lowest_image(self,path):
        """ Return the lowest image """
        self.picture_lowest = dict()
        #self.list_lowest = list(filter(lambda x: x.endswith((".png", ".jpg", ".jpeg")), os.listdir(path)))
        self.list_lowest = list(filter(lambda x: x.endswith((
                                                            ".jpg" , ".png" , ".gif" , ".webr" ,
                                                            ".tiff" , ".psd" , ".raw" , ".bmp",
                                                            ".heif" , ".indd" , ".jpeg", ".svg",
                                                            ".ai" , ".ebps" , ".pdf"


                                                            )), os.listdir(path)))
        for name in self.list_lowest :
            with Image.open(path + '\\' + name) as mg : 
                width , height = mg.size 
                self.picture_lowest[name] = sum([width,height])

        self.name_lowest , self.size_lowest = '' , min(list(sorted(self.picture_lowest.values(),reverse=False)))

        for (name_lowset,size_lowset) in self.picture_lowest.items():
            if (size_lowset == self.size_lowest):
                self.name_lowest = name_lowset
                self.size_lowest = size_lowset

        print([self.name_lowest , self.size_lowest , path])
        print("\n")
        return (f"name Image :{self.name_lowest}\ntotal dimensions :{self.size_lowest} Pixel\nLocation :{path}")


       
    def get_bytes(self,path_mg):
        """ Returns the size of the image in the device's memory get full path image"""
        if not os.path.exists(path_mg):
            return "The path is wrong, please check it correctly : {}".format(path_mg)
        self.bytes_image = os.path.getsize(path_mg)

        if self.bytes_image <=1 :
            return "Error Bytes"
        return "Image size in device memory : {}".format(self.bytes_image)




    def calculate_selected_photos(self,path , stretch):
        """ Count the number of images ending in the extension (PNG, JPEG , JPG)"""

        try :
            self.table3 = PrettyTable()
            self.table3.field_names = ['Name Image','Path','Image Extension']

            if not os.path.exists(path):
                if not os.path.isdir(path):
                    raise FileNotFoundError("Please check the image path is correct :{}".format(path))
            for name_image in os.listdir(path):
                if name_image.endswith(stretch):
                    self.table3.add_row([name_image , path + '\\' + name_image , name_image.split('.')[-1]])


            print(self.table3)

            print("\n")
            print(f"The number of images that end with the extension :" 
                f"{name_image.split('.')[-1]} is {len(list(filter(lambda count :count.endswith((stretch)),os.listdir(path))))}")

            return list(filter(lambda count :count.endswith((stretch)),os.listdir(path)))



        except FileNotFoundError as error :
            return error
        raise NotADirectoryError("Invalid Path")



    def similarity_check(self,path_image_one , path_image_two):
        """ Similarity check if the two images are the same """
        try :
            self.check_condition = False 
            self.table4 = PrettyTable()
            self.table4.field_names = ['Image One','Image Two' , 'Result']

            if not os.path.exists(path_image_one) or not os.path.exists(path_image_two):
                raise FileNotFoundError("The path is wrong Please check the path is correct")

            self.img1 = Image.open(path_image_one)
            self.img2 = Image.open(path_image_two)

            #return self.table4

            if list(self.img1.getdata()) != list(self.img2.getdata()):
                self.check_condition = False 
            else:
                self.check_condition = True 


            if self.check_condition == False :
               self.table4.add_row([path_image_one , path_image_two , "No match"])
               return self.table4
            else:
                self.table4.add_row([path_image_one , path_image_two , "There is a match"])
                return self.table4


        except NotADirectoryError as er :
            return er
        except Exception as error_ex :
            return error_ex 


    def get_information_image(self,PATH_IMAGE):
        """ Get All Information Image Take Full Path Image """
        try :
            self.table5 = PrettyTable()
            self.table5.field_names = [
                                "Filename" , "Image Size" , "Image Height" , "Image Width" ,
                                "Image Format" , "Image Mode" ,"Image is Animated" ,"Frames in Image"

                                ]


            if not os.path.exists(PATH_IMAGE):
                raise FileNotFoundError("File not found : {} Please check the location is correct".format(PATH_IMAGE))

            with Image.open(PATH_IMAGE) as self.image_open:
                self.info_dict = {
                        "Filename": self.image_open.filename,
                        "Image Size": self.image_open.size,
                        "Image Height": self.image_open.height,
                        "Image Width": self.image_open.width,
                        "Image Format": self.image_open.format,
                        "Image Mode": self.image_open.mode,
                        "Image is Animated": getattr(self.image_open, "is_animated", False),
                        "Frames in Image": getattr(self.image_open, "n_frames", 1)
                        }


                for (lable,value) in self.info_dict.items():
                    self.table5.add_row([
                                    self.image_open.filename, self.image_open.size,self.image_open.height,
                                    self.image_open.width,self.image_open.format,self.image_open.mode,
                                    getattr(self.image_open, "is_animated", False),
                                    getattr(self.image_open, "n_frames", 1)

                                    ])
                    print(self.table5) ; print("\n") ; return self.info_dict

        except Exception as e :
            return e 



"""
Note: You can access the file README.md and read the examples that were placed inside the file, so that things are clear to you 
"""
