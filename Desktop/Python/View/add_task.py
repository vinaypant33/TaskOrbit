import tkinter as tk
from tkinter import ttk

import ttkbootstrap as btk


from pubsub import pub


class add_task():


    def increase_timer(self):
        if self.running == True:
            self.actual_task_frame.after(1000 , self.increase_timer)
        
        self.seconds+=1
        if self.seconds >= 60:
            self.minutes +=1
            # print(f"Minutes {self.minutes}")
            self.seconds = 0
        if self.minutes >= 60:
            self.hours +=1
            self.minutes = 0
            # print(f"Hours {self.hours}")
        
        self.time_string  = f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"
        self.time_text.configure(text=self.time_string)

        # pub.sendMessage("timedata" , f"{self.seconds,self.minutes,self.hours}")
        
        
        



    def add_button_clicked(self):
        if self.running:
            self.running = False
            self.start_stop_button.configure(text="\u25B6")
            task_name  = self.task_entry.get()
            timer_data = str(f"{self.hours}:{self.minutes}:{self.seconds}")
            message_string  = str(task_name  + timer_data)
            pub.sendMessage("timer_data" , message_string)
           

        else:
            self.running = True
            self.start_stop_button.configure(text="\u25A0")
            self.increase_timer()


    def __init__(self , master , app_width  = 400):
        self.upper_task_frame  = master
        self.width = app_width
        
        self.running  = False

        self.seconds = 0
        self.minutes = 0
        self.hours   = 0


        self.actual_task_frame  = btk.Frame(self.upper_task_frame , width=self.width , bootstyle  = "dark")
        
        # Frames for each control one for entry box and one for  the timer and one for the stop or pause butotn 
        self.text_frame  = btk.Frame(self.actual_task_frame , width=10 , bootstyle  = "dark")
        self.time_text  = btk.Label(self.actual_task_frame  , text="00:00:00" , font=("Arial" , 14 , "bold") ,  bootstyle  = "dark" , foreground="white" , background="#2F2F2F")
        self.start_stop_button  = btk.Button(self.actual_task_frame , text = "\u25B6" ,  bootstyle  = "danger" , command=self.add_button_clicked) # For the stop button this unicde  : "\u25A0"

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