import sys
sys.dont_write_bytecode = True
import tkinter.filedialog
import os
import pickle
import tkinter as tk

import DEMPS_getParameters

def loadJudgeLog(parameters):
    setting_detail = DEMPS_getParameters.getParameters(parameters)

    log = setting_detail[15]

    dir=os.path.join(os.environ['USERPROFILE'], 'Desktop')
    data_file = tkinter.filedialog.askopenfilename(initialdir = dir)

    log.insert(tk.END,"Load file : " + str(data_file) + "\n")
    log.see("end")

    with open(data_file, mode='rb') as f:
        judegedata = pickle.load(f)
    return judegedata

