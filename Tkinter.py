from customtkinter import filedialog 
import customtkinter as ctk
from Os import Os
from time import sleep
   
class Interface(Os):
   """ Class Interface that implements Class "Os", window with 600px width and 400px height, have 3 frames(2 place and 1 pack(organized in grid)).  """
   def __init__(self):
      super().__init__()  #or Os().__init__()
      
      #appearance
      ctk.set_appearance_mode("dark")  #Default is the theme in computer. Can set, "dark", "light"
      ctk.set_default_color_theme("dark-blue")

      #window
      self.window = ctk.CTk()
      self.window.title("Files Organizer")
      self.window.geometry("600x400")
      self.window.resizable(width=False, height=False)

      #frames
      self.frame_1 = ctk.CTkFrame(master = self.window, width=400, height=400)
      self.frame_2 = ctk.CTkFrame(master = self.frame_1, width=300, height=200, fg_color="transparent")
      self.frame_3 = ctk.CTkFrame(master = self.frame_1, width=140, height=150, fg_color="transparent")
      self.frame_1.pack(padx = 10, pady= 10,fill="both", expand=True)
      self.frame_1.columnconfigure((0,1,2,3), weight=1)
      self.frame_1.rowconfigure((0,1,2,3), weight=1)
      self.frame_2.place(x=250, y=100)
      self.frame_3.place(x=25, y=180)
      
      #self Variables
      self.os = Os()
      self.selected = []
      self.checkBox_list = []
      self.checkBoxObjects = []
      self.checkBox = ctk.CTkCheckBox(master = self.frame_2)
      self.textLabel = ctk.StringVar(self.frame_3)
      self.textLabel.set("Click on Button above and\nChoose the folder you want\nto organize the files")

      
   #Changing directory by filedialog
   def choose(self):
      dir = filedialog.askdirectory()
      self.os.selecting_directory(dir)
           
   #forget checkbox's in frame and del objects(checkBoxObjects)
   def forget(self):
      for i in self.checkBoxObjects:
         i.grid_forget()
      size = len(self.checkBoxObjects)
      for i in range(size):
         #print(self.checkBoxObjects)
         del(self.checkBoxObjects[0])

   #Create checkBox according to quantity extensions selected by user
   def create_check_box(self):
      try:
         quantity_check_box = len(self.types_set)
         self.types_list = self.types_files()
         column = 1
         row = 1
         c = []
         a = sorted(self.checkBox_list)
         b = sorted(self.types_list)
        
         if a==b and len(self.checkBox_list) == 0:
            return
         else:
            if c == a:
               for i in range(quantity_check_box):
                  #f = ctk.CTkFrame(self.window).pack()
                  checkBox = ctk.CTkCheckBox(master = self.frame_2, text="."+self.types_list[i])
                  if i%4 == 0 and not i==0:
                     column += 1
                     row = 1
                     checkBox.grid(column=column,row=row)
                  else:   
                     checkBox.grid(column=column,row=row)
                  self.checkBox_list.append(self.types_list[i])
                  self.checkBoxObjects.append(checkBox)
                  row += 1
            else:
               if len(b)>len(a):
                  self.forget()
                  for i in self.checkBox_list:
                     if i in b:
                        b.remove(i)
                  for i in range(len(b)):
                     #f = ctk.CTkFrame(self.window).pack()
                     checkBox = ctk.CTkCheckBox(master = self.frame_2, text="."+b[i])
                     if i%4 == 0 and not i==0:
                        column += 1
                        row = 1
                        checkBox.grid(column=column,row=row)
                     else:   
                        checkBox.grid(column=column,row=row)
                     self.checkBox_list.append(b[i])
                     self.checkBoxObjects.append(checkBox)
                     row += 1
               else:
                  self.forget()
                  #for i in b:
                  #   a.remove(i)
                  for i in range(len(b)):
                     #f = ctk.CTkFrame(self.window).pack()
                     checkBox = ctk.CTkCheckBox(master = self.frame_2, text="."+b[i])
                     if i%4 == 0 and not i==0:
                        column += 1
                        row = 1
                        checkBox.grid(column=column,row=row)
                     else:   
                        checkBox.grid(column=column,row=row)
                     self.checkBox_list.append(b[i])
                     self.checkBoxObjects.append(checkBox)
                     row += 1
      except Exception as e:
         print("O erro foi:", e)

   #Get what user selected in checkbox and store in self.selected
   def getValues(self):
      self.selected = []
      for i in self.checkBoxObjects:
         text = i.cget("text")
         value = i.get()
         if value == 1:
            self.selected.append(text)

   #before everything analyze if is possible create a folder and organize. Call other functions to organize files given extensions selected and changes label
   def final_button(self):
      if self.verify():
         self.textLabel.set("Organizing...")
         self.window.update_idletasks()
         sleep(1)
         self.getValues()
         self.os.create_folder_extension(self.selected)
         self.os.list_extension_files_and_move(self.selected)
         self.textLabel.set("Folders created and Organized!\nThank you for using our program!\nUse 'Back' to restart interface")
         self.types_files()
         self.create_check_box()

   #Changes Label Value to initially text
   def setInitially(self):
      self.textLabel.set("Click on Button above and\nChoose the folder you want\nto organize the files")

   #Changes Label Value text to after selected folder 
   def setMedium(self):
      self.textLabel.set("Folder selected!\nSelect which extensions\nWould you like to organize\nThen Click on 'OK'")

   #Reset values from CheckBox to 0
   def reset(self):
      #self.setInitially()
      for i in self.checkBoxObjects:
         i.deselect(0)

   #Verify if have any CheckBox selected to execute other functions
   def verify(self):
      for i in self.checkBoxObjects:
         value = i.get()
         if value == 1:
            return True
      return False

   #Back everything to initial state
   def back(self):
      self.forget()
      self.setInitially()

   #Create widgets in frames
   def interface(self):

      #Labels:    
      labelTitle = ctk.CTkLabel(master=self.frame_1, text="Files Organizer", font=("Arial", 25)) #Load indirectly in root, by frame
      labelTexto = ctk.CTkLabel(master=self.frame_3, textvariable=self.textLabel, justify="left")
      labelTitle.grid(column=0, columnspan=4, row=0, pady=20, padx=15)
      labelTexto.pack(padx=5, pady=5)

      #Buttons:
      buttonChoose = ctk.CTkButton(master = self.frame_1, text="Choose folder",command = lambda:[self.choose(), self.types_files(), self.create_check_box(), self.setMedium()])
      buttomReset = ctk.CTkButton(master = self.frame_1, text="Reset", command=self.reset)
      buttomBack = ctk.CTkButton(master = self.frame_1, text="Back", command=self.back)
      buttonFinal = ctk.CTkButton(master = self.frame_1, text="OK", command=self.final_button)
      buttonChoose.grid(column=0, columnspan=2, row=1, sticky="n")
      buttomReset.grid(column=2, row=5,pady=10,padx=10, sticky="se")
      buttomBack.grid(column=1, row=5,pady=10,padx=10, sticky="se")
      buttonFinal.grid(column=3, row=5,pady=10,padx=10, sticky="se")

      self.window.mainloop()
