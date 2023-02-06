from tkinter import *   
  
master = Tk()   
  
master.geometry('600x300')   
    
button = Button(master,  
                text = 'Submit',  
                bg='blue', activebackground='red').pack()   
  
master.mainloop()