from tkinter import *
import tkinter as tk

import files_main
import files_func

def load_gui(self):

    self.scrollbar1 = Scrollbar(self.master,orient=VERTICAL)
    self.lstList1 = Listbox(self.master,exportselection=0,yscrollcommand=self.scrollbar1.set)
    self.lstList1.bind('<<ListboxSelect>>')
    self.scrollbar1.config(command=self.lstList1.yview)
    self.scrollbar1.grid(row=1,column=5,rowspan=7,columnspan=1,padx=(0,0),pady=(0,0),sticky=N+E+S)
    self.lstList1.grid(row=1,column=2,rowspan=7,columnspan=3,padx=(0,0),pady=(0,0),sticky=N+E+S+W)
    
    self.btn_add.grid(row=8,column=0,padx=(25,0),pady=(45,10),sticky=W)
    self.btn_check = tk.Button(self.master,width=12,height=2,text='Check for files...',command=lambda: files_func.onBrowse(self))
    self.btn_check.grid(row=8,column=1,padx=(15,0),pady=(45,10),sticky=W)
    self.btn_close = tk.Button(self.master,width=12,height=2,text='Close program',command=lambda: files_func.ask_quit(self))
    self.btn_close.grid(row=8,column=4,columnspan=1,padx=(15,0),pady=(45,10),sticky=E)
    self.lbl_info = tk.Label(self.master)
    self.lbl_info.grid(row=0,column=2,padx=(0,0),pady=(10,0),sticky=N+W)
    self.lbl_info = tk.Label(self.master)
    self.lbl_info.grid(row=0,column=4,padx=(0,0),pady=(10,0),sticky=N+W)


if __name__ == "__main__":
    pass
