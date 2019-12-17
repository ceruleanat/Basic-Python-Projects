from tkinter import filedialog
from tkinter import *


def browse_button():
    # Allow user to select a directory and store it in global var
    # called folder_path
    global folder_path
    filename = filedialog.askdirectory()
    folder_path.set(filename)
    print(filename)


root = Tk()
folder_path = StringVar()
lbl1 = Label(master=root,textvariable=folder_path)
lbl1.grid(row=0, column=1)
button2 = Button(text="Browse...", command=browse_button)
button2.grid(row=0,column=0,padx=(27,0),pady=(30,0),sticky=N+W),
text1 = Text(root, height=2, width=40)
text1.grid(row=0,column=2,padx=(27,0),pady=(30,0),sticky=N+W)
button3 = Button(text="Browse...", command=browse_button)
button3.grid(row=2,column=0,padx=(27,0),pady=(10,0),sticky=N+W)
text1 = Text(root, height=2, width=40)
text1.grid(row=2,column=2,padx=(27,0),pady=(10,0),sticky=N+W)
button3 = Button(text="Check for files...", command=browse_button)
button3.grid(row=5,column=0,padx=(27,10),pady=(15,15),sticky=N+W)
button3 = Button(text="Close Program", command=root.destroy)
button3.grid(row=5,column=16,padx=(87,27),pady=(15,15),sticky=N+W)

mainloop()



