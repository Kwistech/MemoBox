# Memo Box - Johnathon Kwisses (Kwistech)
from datetime import datetime
from os import makedirs
from subprocess import Popen
from tkinter import *


class App:
    """Contains the interface and the initializing variables for the program.

    The user enters their "memo" into the program's entry box and presses
    the button labeled "Write". The class calls the "write_memo" function
    after the user has pressed the button.

    The user can open the project's root directory by pressing the button
    labeled "Open". When the button is pressed, the class calls the
    "open_root" function.

    Note: Change the "path_open" to your project's root directory path.
    """

    def __init__(self):
        """Defines the interface function calls for the program."""
        self.frame = Frame()
        self.frame.pack()

        date = datetime.now()
        month = convert_month(date.month)
        path_open = "."
        path_memos = "./memos/{}/{}/".format(date.year, month)

        label_text = "Enter memo in box and press Write"
        label = Label(self.frame, text=label_text)
        entry = Entry(self.frame, width=30)
        button_open = Button(self.frame, text="Open", width=4, height=1,
                             command=lambda: open_root(path_open))
        button_write = Button(self.frame, text="Write", width=4, height=2,
                              command=lambda: write_memo(entry, date,
                                                         month, path_memos))

        label.grid(row=0, column=0)
        entry.grid(row=1, column=0)
        button_open.grid(row=0, column=1)
        button_write.grid(row=1, column=1, padx=5, sticky=N)


def create_dir(path):
    """Helper function that attempts to create directory path."""
    try:
        makedirs(path)
    except FileExistsError:
        pass


def convert_month(m):
    """Converts datetime month number to month string.

    Args:
        m (int): Month number [eg. 4].

    Returns:
        str: Month string [eg. "april"].

    """
    months = {1: "january", 2: "february", 3: "march", 4: "april", 5: "may",
              6: "june", 7: "july", 8: "august", 9: "september", 10: "october",
              11: "november", 12: "december"}
    m = months[m]
    return m


def open_root(path):
    """Opens root directory in explorer."""
    Popen(r'explorer "{}"'.format(path))


def write_memo(entry, date, month, path):
    """Writes user text to appropriate file.

    Args:
        entry (tkinter.Entry): Entry box tkinter class.
        date (datetime.datetime): datetime class.
        month (str): Month as a string.
        path (str): Path to appropriate file.

    """
    text = entry.get()
    date_str = "{}-{}-{}.txt".format(month, date.day, date.year)
    write_template = "- "            # Creates a 'list' in file.
    create_dir(path)

    with open(path + date_str, "a") as f:
        f.write(write_template + text + "\n")

    entry.delete(first=0, last=139)  # Deletes text in Entry widget.

root = Tk()
root.title("Memo Box")
app = App()
root.mainloop()
