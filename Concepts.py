"""
- Current Working Directory(CWD): Where the python is operating.
- Current Directory(CD): The folder where the Python Script is running.


Ex: # Getting the locate:
import os 
cwd = os.getcwd()
print("Current working directory:", cwd)

# Changing locate of CWD:
os.chdir("c:\GitHub\Projetos_Praticos") or ("../")

# Creating new Directory:
- os.mkdir() ; os.makedirs()

- os.mkdir(): is used to create a directory named path with the specified numeric mode. This method raises FileExistsError if the directory to be created already exists.

directory = "GeeksforGeeks"
parent_dir = "C:/GitHub/Projetos_Praticos"
path = os.path.join(parent_dir, directory)
os.mkdir(path)  # If have some cod mode, puts like another parameter.

- os.makedirs(): is used to create a directory recursively, that means while making leaf directory if any intermediate-level directory is missing, the method will create them all.
- Can be used to create a directory tree

directory = "Nikhil" #Leaf directory
parent_dir = "C:/Github/Projetos_Praticos/Felizes"
path = os.path.join(parent_dir, directory)
os.makedirs(path)

# Listing out files and Directories with python:
- os.listdir(): used to get the list of all files and directories in the specified directory. if we don't specify any directory, then the list of files and directories in the current working directory will be returned; Files with extension and directories.

# Deleting Directory or Files using Python:
- os.remove(): is used to remove or delete a file path. This method can not remove or delete a directory. If the specified path is a directory then OSError will be raised by method. Two ways:
1: Changing Current working directory and then execute the remove
Ex: os.chdir("c:\GitHub\Projetos_praticos\Organizador_files_folders")
os.remove("Feliz.txt")
2: give the path and file: file = "Feliz.txt"
location = "c:\GitHub\Projetos_praticos\Organizador_files_folders"
path = os.path.join(location, file)
os.remove(path)

- os.rmdir(): Is used to remove or delete an empty directory. OSError will be raised if the specified path is not an empty directory.
Ex: directory = "Geeks"
parent = "C:/Github"
path = os.path.join(parent, directory)
os.rmdir(path)

# Commonly Used Functions:
1° os.name: This function gives the name of the operating system dependent module imported(Commons names: "posix, nt, os2, ce, java, riscos")
2° os.error: All functions in this module raise OSError in the case of invalid or inaccessible file names and paths, or other arguments that have the correct type, but are not accepted by the operating system. os.error is an alias for built-in OSError exception.

Ex: 
try: 
   # if the file does not exist, then it would throw an IOError
   filename = "GFG.txt"
   f = open(filename, 'rU')
   text = f.read()
   f.close()
except IOError:
   print("problem reading: " + filename)

3° os.popen(): opens a pipe to or from command. The return value can be read or written depending on whether the mode is 'r' or 'w'. ex: os.popen(command[, mode[, bufsize]])  # mode & bufsize are not necessary parameters, if not provided, default 'r' is taken for mode.

Ex: 
fd = "GFG.txt"
file = os.popen(fd, 'w')  #Provides a pipe/gateway and access the file directly
file.write("Hello") #File not closed, shown in next fuction

#similar to:
file = open(fd, 'w')
file.write("Hello")
file.close()
file = open(fd, 'r')
text = file.read()
print(text)

4° os.close(): Close file descriptor fd. A file opened using open(), can be closed by close() only. But file opened through os.popen(), can be closed with close() or os.close(). If we try closing a file opened with open(), using os.close(), python would throw TypeError.

5° os.rename(): The name of the file changes only if, the file exists and the user has sufficient privilege permission to change the file.

Ex: fd = "GFG.txt"
os.rename(fd, 'New.txt')
os.rename(fd, 'New.txt')

6° os.remove(): To remove a file we need to pass the name of hte file as a parameter.
Ex: os.remove("file_name.txt")  #If file not exist, python throw a "FileNotFoundError"

7° os.path.exist(): will check whether a file exists or not by passing the name of the file as a parameter. OS module has a submodule named PATH by using which we can perform many more functions.
Ex: result = os.path.exists('file_name')
print(result) #Given back True or False

8° os.path.getsize(): will give us the size of the file in bytes. To use this method we need to pass the name of the file as a parameter.
Ex: size = os.path.getsize('filename')
print("Size of the file is", size, 'bytes.')

# Ways to get only files in a directory:
1° filenames = next(os.walk(path))[2]
2° from os import listdir
from os.path import isfile, join

mypath = '/home/'

onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
print(onlyfiles)

3° import glob
print glob.glob("/home/user/*.txt") or "*." to get any extension

4° Only directories: 
list(filter(os.path.isdir, os.listdir())) or list(filter(os.path.isfile, os.listdir()))






"""
"""# Importante rodar no terminal, se torna diferente rodando pelo console.
import os 
cwd = os.getcwd()
print("Current working directory:", cwd)

os.chdir("c:\GitHub\Projetos_praticos\Organizador_files_folders")
print("Current working directory:", os.getcwd())

print(os.listdir())
#os.remove("Feliz.txt")
#print(os.listdir())
"""
""" files = ["hello.txt", "feliz.pdf"]
sete = set()
for file in files:
   sete.add(file.split(".")[1].lower())
set_list = list(sete)
quantity_check_box = len(sete)
for i in range(quantity_check_box):
   print(f"checkBox_{i} = ctk.CTkCheckBox(master = self.frame_1, text={set_list[i]}).pack()")
 """
""" 
from tkinter import *

root = Tk()

name = StringVar()
check_box_list = []
ent=Entry(root,textvariable=name).pack()

def clear():
    for i in check_box_list:
        i.pack_forget()    # forget checkbutton
        # i.destroy()        # use destroy if you dont need those checkbuttons in future

def generate():
    k=name.get()
    c=Checkbutton(root,text=k)
    c.pack()
    check_box_list.append(c)  # add checkbutton

btn1=Button(root,text="Submit",command=generate)
btn1.pack()

btn2=Button(root,text="Clear",command=clear)
btn2.pack()

mainloop()
 """
import customtkinter as ctk
window = ctk.CTk()
window.geometry("600x400")
window.resizable(width=False, height=False)
frame_1 = ctk.CTkFrame(master = window, width=400, height=400)
frame_2 = ctk.CTkFrame(master = frame_1, width=200, height=50)
frame_2.place(x=100, y=100)
frame_1.pack(padx = 10, pady= 10,fill="both", expand=True)
frame_1.columnconfigure((0,1,2,3), weight=1)
frame_1.rowconfigure((0,1,2,3), weight=1)

window.mainloop()
