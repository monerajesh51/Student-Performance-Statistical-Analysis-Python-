import calendar
import tkinter as tk
from tkinter import *

def showCal():
    year = int(year_field.get())
    month = int(month_field.get())

    cal = calendar.month(year, month)

    new_window = tk.Tk()
    new_window.title("Calendar")

    cal_content = Label(new_window, text=cal, font=("Consolas", 12))
    cal_content.grid(row=5, column=1)

    new_window.mainloop()


root = tk.Tk()
root.title("GUI Calendar")

root.geometry("300x250")

cal = Label(root, text="Calendar", bg="lightblue",
            font=("Arial", 20, "bold"))
year_label = Label(root, text="Enter Year")
month_label = Label(root, text="Enter Month")

year_field = Entry(root)
month_field = Entry(root)

show_button = Button(root, text="Show Calendar",
                     fg="black", bg="lightgreen",
                     command=showCal)

exit_button = Button(root, text="Exit",
                     fg="black", bg="red",
                     command=root.destroy)

cal.grid(row=1, column=1)
year_label.grid(row=2, column=0)
year_field.grid(row=2, column=1)
month_label.grid(row=3, column=0)
month_field.grid(row=3, column=1)
show_button.grid(row=4, column=1)
exit_button.grid(row=6, column=1)

root.mainloop()