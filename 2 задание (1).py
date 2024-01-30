import tkinter as tk
from tkinter import messagebox
import time

def start_timer():
    minutes = int(minutes_entry.get())
    seconds = int(seconds_entry.get())

    total_seconds = minutes * 60 + seconds

    while total_seconds > 0:
        minutes, seconds = divmod(total_seconds, 60)
        timer_label.config(text='Time left: {:02d}:{:02d}'.format(minutes, seconds))
        root.update()
        time.sleep(1)
        total_seconds -= 1

messagebox.showinfo('Timer', 'Timer has finished!')

root = tk.Tk()
root.title('Timer')

minutes_label = tk.Label(root, text='Mins:')
minutes_label.grid(row=0, column=0, padx=5, pady=5)

minutes_entry = tk.Entry(root, width=5)
minutes_entry.grid(row=0, column=1, padx=5, pady=5)

seconds_label = tk.Label(root, text='Secs:')
seconds_label.grid(row=0, column=2, padx=5, pady=5)

seconds_entry = tk.Entry(root, width=5)
seconds_entry.grid(row=0, column=3, padx=5, pady=5)

start_button = tk.Button(root, text='Старт', command=start_timer)
start_button.grid(row=1, column=0, columnspan=4, padx=5, pady=5)

timer_label = tk.Label(root, text='Time left: 00:00')
timer_label.grid(row=2, column=0, columnspan=4, padx=5, pady=5)

root.mainloop()