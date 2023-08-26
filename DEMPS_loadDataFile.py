import tkinter.filedialog
import tkinter as tk
import sys
import os
sys.dont_write_bytecode = True

def load_dataFile(ent):
        ent.delete(0, tk.END)
        data_file = tkinter.filedialog.askdirectory()
        ent.insert(tk.END,data_file)

def load_teacherdata(ent):
        ent.delete(0, tk.END)
        #data_file = tkinter.filedialog.askdirectory()
        fTyp = [("", "*")]
        iFile = os.path.abspath(os.path.dirname(__file__))
        data_file = tkinter.filedialog.askopenfilename(filetype = fTyp, initialdir = iFile)
        ent.insert(tk.END,data_file)