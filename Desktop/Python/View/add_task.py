import tkinter as tk
from tkinter import ttk

import ttkbootstrap as btk

from pubsub import pub
from time import sleep


class add_task:
    def increase_timer(self):
        if not self.running:
            self.seconds = 0
            self.minutes = 0
            self.hours = 0
            self.time_string = f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"
            self.time_text.configure(text=self.time_string)
            return

        self.seconds += 1
        if self.seconds >= 60:
            self.minutes += 1
            self.seconds = 0
        if self.minutes >= 60:
            self.hours += 1
            self.minutes = 0

        self.time_string = f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"
        self.time_text.configure(text=self.time_string)

        if self.running:
            self.actual_task_frame.after(1000, self.increase_timer)

    def add_button_clicked(self):
        if self.running:
            self.running = False
            self.start_stop_button.configure(text="\u25B6")

            task_name = self.task_entry.get()

            if task_name.strip() == "":
                return
                

            timer_data = f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"
            message_string = f"{task_name},{timer_data}"

            pub.sendMessage("timer_data", message_string=message_string)

            self.task_entry.delete(0, "end")

            self.seconds = 0
            self.minutes = 0
            self.hours = 0
            self.time_string = f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"
            self.time_text.configure(text=self.time_string)
        else:
            if self.task_entry.get() == "":
                return
            self.running = True
            self.start_stop_button.configure(text="\u25A0")
            self.increase_timer()


    def focus_on_text(self, ent):
        self.task_entry.icursor(0)
        self.task_entry.xview_moveto(0)

    def __init__(self, master, app_width=400):
        self.upper_task_frame = master
        self.width = app_width

        self.running = False

        self.seconds = 0
        self.minutes = 0
        self.hours = 0

        self.time_string = f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"

        self.actual_task_frame = btk.Frame(self.upper_task_frame, width=self.width, bootstyle="dark")

        self.text_frame = btk.Frame(self.actual_task_frame, width=10, bootstyle="dark")
        self.time_text = btk.Label(
            self.actual_task_frame,
            text=self.time_string,
            font=("Arial", 14, "bold"),
            bootstyle="dark",
            foreground="white",
            background="#2F2F2F",
        )
        self.start_stop_button = btk.Button(
            self.actual_task_frame,
            text="\u25B6",
            bootstyle="danger",
            command=self.add_button_clicked,
        )

        self.task_entry = btk.Entry(self.text_frame, width=37, bootstyle="dark")

        self.task_entry.bind("<FocusIn>", self.focus_on_text)

        self.actual_task_frame.pack(side=btk.LEFT, padx=(0, 0))
        self.text_frame.pack(side=btk.LEFT, padx=(4, 4))
        self.task_entry.pack(side=btk.LEFT, padx=(4, 0))
        self.time_text.pack(side=btk.LEFT, padx=(4, 4))
        self.start_stop_button.pack(side=btk.LEFT, padx=(0, 0))


class add_completed_task:
    def __init__(self, master, curernt_text, current_time):
        self.master = master
        self.current_text = curernt_text
        self.current_time = current_time

        max_chars = 37
        text = self.current_text

        lines = [text[i:i + max_chars] for i in range(0, len(text), max_chars)]
        display_text = "\n".join(lines)

        number_of_lines = len(lines)
        line_height = 18
        frame_height = number_of_lines * line_height + 10

        self.master_frame = btk.Frame(self.master, width=360, height=frame_height, border=1)
        self.master_frame.pack_propagate(0)

        self.work_text = btk.Label(
            master=self.master_frame,
            text=display_text,
            font=("Arial", 10, "bold"),
            anchor="w",
            justify="left",
            width=max_chars
        )

        self.time_taken = btk.Label(
            master=self.master_frame,
            text=self.current_time,
            font=("Arial", 10, "bold"),
            anchor="e",
            justify="right"
        )

        self.master_frame.pack(pady=2)
        self.work_text.pack(side=btk.LEFT, padx=(0 , 2), pady=5)
        self.time_taken.pack(side=btk.LEFT, padx=(0 , 2), pady=5)




if __name__ == "__main__":
    main = btk.Window()
    add_task(master=main)
    main.mainloop()
