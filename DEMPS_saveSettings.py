from tkinter import messagebox
import datetime
import os
import sys
sys.dont_write_bytecode = True
import tkinter as tk
from tkinter import filedialog

import DEMPS_getParameters


#設定の保存
def saveSettings(parameters):
    setting_detail = DEMPS_getParameters.getParameters(parameters)

    log = setting_detail[15]

    satpath        = setting_detail[0]
    acopath        = setting_detail[1]
    maxluminance   = setting_detail[2]
    hist_luminance = setting_detail[3]
    px             = setting_detail[4]
    py             = setting_detail[5]
    deltaX         = setting_detail[6]
    deltaY         = setting_detail[7]
    ndvi_min       = setting_detail[8]
    ndvi_max       = setting_detail[9]
    fdi_min        = setting_detail[10]
    fdi_max        = setting_detail[11]
    fn             = setting_detail[12]
    title          = setting_detail[13]
    

    today = datetime.date.today()
    ftype=[('Textファイル', '*.txt')]
    idir=os.path.join(os.environ['USERPROFILE'], 'Desktop')

    with open(filedialog.asksaveasfilename(defaultextension='txt', filetypes=ftype, initialdir=idir), mode='w') as file:
        file.write(f"day:{today}\n")
        file.write(f"Satellite data path:{satpath}\n")
        file.write(f"Acolite data path:{acopath}\n")
        file.write(f"luminance:{maxluminance}\n")
        file.write(f"hist luminance:{hist_luminance}\n")
        file.write(f"px:{px}\n")
        file.write(f"py:{py}\n")
        file.write(f"deltaX:{deltaX}\n")
        file.write(f"deltaY:{deltaY}\n")
        file.write(f"NDVI range:{ndvi_min}~{ndvi_max}\n")
        file.write(f"FDI range:{fdi_min}~{fdi_max}\n")
        file.write(f"file name:{fn}\n")
        file.write(f"graph title:{title}\n")
        log.insert(tk.END,"Save Completed.\n")
        log.see("end")