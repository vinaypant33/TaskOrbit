import tkinter as tk
from tkinter import ttk

import ttkbootstrap as btk





class add_task():

    def __init__(self , master , app_width  = 400):
        self.upper_task_frame  = master
        self.width = app_width
        

        self.actual_task_frame  = btk.Frame(self.upper_task_frame , width=self.width , bootstyle  = "dark")
        
        # Frames for each control one for entry box and one for  the timer and one for the stop or pause butotn 
        self.text_frame  = btk.Frame(self.actual_task_frame , width=10 , bootstyle  = "dark")
        self.time_text  = btk.Label(self.actual_task_frame  , text="00:00:00" , font=("Arial" , 14 , "bold") ,  bootstyle  = "dark" , foreground="white" , background="#2F2F2F")
        self.start_stop_button  = btk.Button(self.actual_task_frame , text = "\u25B6" ,  bootstyle  = "danger") # For the stop button this unicde  : "\u25A0"

        # Make the entry for the text :
        self.task_entry  = btk.Entry(self.text_frame , width=37 ,  bootstyle  = "dark")


        # Configure the controls : 


        # Pack the controls  : 
        self.actual_task_frame.pack(side=btk.LEFT  , padx=(0,0))
        self.text_frame.pack(side=btk.LEFT , padx =(4 , 4))
        self.task_entry.pack(side=btk.LEFT , padx = (4 , 0))
        self.time_text.pack(side=btk.LEFT , padx=(4 , 4))
        self.start_stop_button.pack(side=btk.LEFT , padx=( 0  , 0))






if __name__ =='__main__':
    main = btk.Window()
    add_task(master = main)
    main.mainloop()