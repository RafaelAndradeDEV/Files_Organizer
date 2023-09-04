import os
import shutil

class Os:
   """ Class that have many functions using 'os' library, such: list_folder, list_files, list_extensions_files_and_move """
   
   def __init__(self):
     #self variables
      self.types_set = set()
      self.types_list = list()
   
   #Change directory given path indicated as parameters returning cwd changed
   def selecting_directory(self, dir:str):
      return os.chdir(str(dir))

   #Return list with all directories in folder selected
   def list_folder(self) -> list:
      return list(filter(os.path.isdir, os.listdir()))

   #Return list with all files in folder selected
   def list_files(self) -> list:
      return list(filter(os.path.isfile, os.listdir()))
   
   #Get the files and return a list with types
   def types_files(self) -> list:
      files = self.list_files()
      self.types_set = set()
      for file in files:
         self.types_set.add(file.split(".")[-1].lower())
      self.types_list =  list(self.types_set)
      return self.types_list
      
   #Get types selected and create a folder with extension selected
   def create_folder_extension(self, selected:list) -> str("End process"):
      self.current_directory = os.getcwd()
      directory = str(self.current_directory)
      for i in range(len(selected)): 
         parent_folder = str(selected[i][1:])
         path = os.path.join(directory, parent_folder)
         os.mkdir(path)

   #Compare if extension selected matches with actually file(in a loop), if yes, move to her
   def list_extension_files_and_move(self, selected:list):
      self.list_extension_chdir = []
      type_selected = []
      for j in selected:
         type_selected.append((j.split(".")[-1]))
      list_files = self.list_files()
      for i in list_files:
         type_in_chdir = ((i.split(".")[-1]).lower())
         for j in type_selected:
            if type_in_chdir == j:
               self.move_files(j, i)

   #Move files given path and given path_file
   def move_files(self, type_in_chdir, file_in_list_files):
      #cwd = os.getcwd()
      path = os.path.join(self.current_directory, type_in_chdir) #f"{cwd}\{type_in_chdir}"
      path_file = os.path.join(self.current_directory, file_in_list_files)
      shutil.move(path_file, path)
