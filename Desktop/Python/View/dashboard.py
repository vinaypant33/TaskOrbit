import tkinter as tk
from tkinter import ttk
import ttkbootstrap as btk
import os
import sys
from datetime import time
from PIL import Image , ImageTk
from ttkbootstrap.scrolled  import ScrolledFrame
from pubsub import pub  


# Importing the classes for the controls : 
from View import add_task




main_application  = btk.Window(themename="darkly")


# Check the main application Height and Width and the center location for y and x 
window_height = 600
window_width  = 400
main_x = 0 
main_y = 0

# Important Functions to be done in this part: 

# Close Application  : 
def close_application():
    main_application.destroy()
    sys.exit()


# Function to make the value of x and y for the main application : 
def mouse_click(event):
    global main_x
    global main_y
    main_x  = event.x
    main_y = event.y

def mouse_move(event):
    global main_x
    global main_y
    main_x = main_x
    main_y = main_y
    delta_x = event.x - main_x
    delta_y = event.y - main_y
    x_location  = main_application.winfo_x() + delta_x
    y_location  = main_application.winfo_y() +delta_y
    main_application.geometry(f"{window_width}x{window_height}+{x_location}+{y_location}")


def show_task_menu(event):
    add_task_menu.tk_popup(event.x_root - 8, event.y_root + 17)

def show_selection_menu(event):
    selection_menu.tk_popup(event.x_root - 7 , event.y_root + 17)


def help_window(event):
    main_help_window = btk.Toplevel(main_application )
    main_help_window.configure(background="#303030")
    master_x = main_application.winfo_x()
    master_y = main_application.winfo_y()
    main_help_window.geometry(f"300x300+{master_x  + 50}+{master_y + 100}")
    main_help_window.overrideredirect(True)
    title_bar  = btk.Frame(main_help_window , height=29  , width = main_help_window.winfo_width(), bootstyle  = "info")
    title_bar.pack_propagate(0)
    close_button = btk.Button(master = title_bar  ,text='\u2716'  , bootstyle  = "dark" , command=main_help_window.destroy)
    help_text = btk.Label(master=main_help_window , text="This is the another helper function \n and this to be done for the main application")
    close_button.bind("<Enter>" , lambda x : close_button.configure(bootstyle  = "danger"))
    close_button.bind("<Leave>" , lambda x : close_button.configure(bootstyle  = "dark"))
    title_bar.pack(side=btk.TOP , fill=btk.X)
    close_button.pack(side=tk.RIGHT , padx=0)

    help_text.pack()
    main_help_window.mainloop()




# Functions for the Pubsub : 
def message(message_string):
    message_string = str(message_string)
    task_name  = message_string.split(",")[0]
    current_time  = message_string.split(",")[1]
    add_task.add_completed_task(below_added_tasks_frame , task_name , current_time)




screen_height  = main_application.winfo_screenheight()
screen_width  = main_application.winfo_screenwidth()

screen_x =  ( screen_width // 2 ) - (window_width // 2)
screen_y = (screen_height // 2 ) - (window_height // 2)

# make the main applicaiotn with the relevenat title heihgt and the width 
main_application.title("Tickture")
main_application.geometry(f"{window_width}x{window_height}+{screen_x}+{screen_y}")
main_application.overrideredirect(True)

# Getting the images and the other assets : All making the right size and other tkintering to be done in the same code block  : 
clock_image  = r"assets\clock_image.png"
clock_image  =Image.open(clock_image)
clock_image = clock_image.resize((26, 26), Image.LANCZOS)
clock_image  = ImageTk.PhotoImage(clock_image)



# Title bar, icon , close button and the menu items :
title_frame = btk.Frame(master=main_application , height=30  , bootstyle  = "dark")
close_button  = btk.Button(master=title_frame , text='\u2716' , bootstyle  = "dark" , command=close_application ,  width=5  , padding=(0 , 6))
application_icon_label  = btk.Label(master=title_frame , image=clock_image , bootstyle  = "dark")

# Menu for the main titlebar  :  This is only one menu section that we can see for each option we have to code the seperate menu bar each time : 
# menubar_01  = btk.Menubutton(master=title_frame , text="Task" ,  bootstyle  = "dark")
menubar_01  = btk.Label(master=title_frame , text="Task" , bootstyle ="light"  ,foreground="gray" ,background="#303030")


add_task_menu = tk.Menu(menubar_01 , tearoff=0)
add_task_menu.add_command(label="Add Task")
add_task_menu.add_command(label="Clear Tasks")
add_task_menu.add_command(label="Archive Tasks")
add_task_menu.add_separator()
add_task_menu.add_command(label="Settings")
add_task_menu.add_checkbutton(label="Black Theme")
add_task_menu.add_separator()
add_task_menu.add_command(label="Exit" , command=close_application)


# menubar_01["menu"] = add_task_menu This wont work as it is not the menu button anymore but we can open the menu on the place as : 



menubar_02  = btk.Label(master=title_frame , text="Selection" ,  bootstyle  = "light" , foreground="gray" , background="#303030")

selection_menu  = tk.Menu(menubar_02)
selection_menu.add_command(label="Select All")
selection_menu.add_command(label="View Archived")

# menubar_02["menu"] = selection_menu


menubar_03 = btk.Label(master=title_frame , text = "Help" , bootstyle = "light"  , foreground="gray" , background="#303030")
# help_menu  = tk.Menu(menubar_03)ddir
# help_menu.add_command(label="Help")

# menubar_03.bind("<Button-1>", on_help_click)



# Frames for the two applications  : one would be the simple frame and another frame would be scrolled frame : 
upper_task_frame  = btk.Frame(master=main_application , width=window_width - 20  , height=window_height * .10  , bootstyle  = "dark")
below_added_tasks_frame  = ScrolledFrame(master=main_application ,width=window_width - 20 , height=window_height * .80 , bootstyle  = "dark")

# Configuring the Controls : 
title_frame.pack_propagate(0)

close_button.bind("<Enter>" , lambda x: close_button.configure(bootstyle = "danger"))
close_button.bind("<Leave>" , lambda x : close_button.configure(bootstyle = "dark"))
title_frame.bind("<ButtonPress-1>" , mouse_click)
title_frame.bind("<B1-Motion>" , mouse_move)
application_icon_label.bind("ButtonPress-1"  ,mouse_click)
application_icon_label.bind("<B1-Motion>" , mouse_move)

menubar_01.bind("<Button-1>" , show_task_menu)
menubar_02.bind("<Button-1>" , show_selection_menu)
menubar_03.bind("<Button-1>" , help_window)


# Enter and Leave and make the menubar for the color in red or another color : 
menubar_03.bind("<Enter>" , lambda x: menubar_03.configure(background="#424040"))
menubar_03.bind("<Leave>" , lambda  x : menubar_03.configure(background="#303030"))
menubar_01.bind("<Enter>" , lambda x: menubar_01.configure(background="#424040"))
menubar_01.bind("<Leave>" , lambda  x: menubar_01.configure(background="#303030"))
menubar_02.bind("<Enter>" , lambda x : menubar_02.configure(background="#424040"))
menubar_02.bind("<Leave>" , lambda x: menubar_02.configure(background="#303030"))



# Adding the controls from other classes and add them in the main application : 
add_task.add_task(upper_task_frame)



# Packing or Placing the controls  : 
title_frame.pack(fill=btk.X)
close_button.pack(side=tk.RIGHT , padx=0 , pady=0)
application_icon_label.pack(side=btk.LEFT)
menubar_01.pack(side=btk.LEFT , padx=(10 , 0))
menubar_02.pack(side=btk.LEFT , padx=(10 , 0))
menubar_03.pack(side=btk.LEFT , padx=(10 , 0))





upper_task_frame.pack(side=btk.TOP , padx=10 , pady=10)
below_added_tasks_frame.pack(side=btk.TOP , padx=10 , pady=10)



# Receive the messages from the other PubSub 
pub.subscribe(listener = message , topicName="timer_data")


main_application.mainloop()