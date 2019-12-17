import os
from tkinter import *
import tkinter as tk
import sqlite3


# Be sure to import our other modules 
# so we can have access to them
import files_main
import files_gui


def ask_quit(self):
    if messagebox.askokcancel("Close Program", "Okay to exit application?"):
        # This closes app
        self.master.destroy()
        os._exit(0)

def create_db(self):
    conn = sqlite3.connect('db_files.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE if not exists tbl_files( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_browse TEXT, \
            col_check TEXT, \
            );")
        # You must commit() to save changes & close the database connection
        conn.commit()
    conn.close()
    first_run(self)

def center_window(self, w, h): # pass in the tkinter frame (master) reference and the w and h
    # get user's screen width and height
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    # calculate x and y coordinates to paint the app centered on the user's screen
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeo

def first_run(self):
    conn = sqlite3.connect('db_files.db')
    with conn:
        cur = conn.cursor()
        cur,count = count_records(cur)
        if count < 1:
            cur.execute("""INSERT INTO tbl_files (col_browse,col_check) VALUES (?,?)""", ('Browse','Check for files'))
            conn.commit()
    conn.close()


def count_records(cur):
    count = ""
    cur.execute("""SELECT COUNT(*) FROM tbl_files""")
    count = cur.fetchone()[0]
    return cur,count



if __name__ == "__main__":
    pass
