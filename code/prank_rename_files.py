#imports
import os


"""
removes numbers from file names in a specified folder path
"""


def rename_files():

    #list of the fields inside a particular directory
    file_list = os.listdir("/home/mark/Dropbox/Courses/udacity_ProgramingFoundationswithPython/prank")
    print(file_list)
    

    # change the working directory to the path where the files are
    os.chdir("/home/mark/Dropbox/Courses/udacity_ProgramingFoundationswithPython/prank")
    
    # set the saved path to be what the current working directory is
    saved_path = os.getcwd()
    print("Saving Directory is " + saved_path)
    

    # for each file in the directory, rename file_name by remove
    for file_name in file_list:
        os.rename(file_name, file_name.translate(None, "0123456789"))
    os.chdir(saved_path)


# run the program
rename_files()
