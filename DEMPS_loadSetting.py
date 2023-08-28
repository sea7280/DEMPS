import sys
sys.dont_write_bytecode = True
import tkinter as tk
import tkinter.filedialog
import os


#設定の読み込み
def read_setting_file(entry): 
    def insert_entry(ent,value):
        ent.delete(0, tk.END)
        ent.insert(tk.END,value)
    
    typ = [('テキストファイル','*.txt')]
    dir = os.getcwd() + '/setting'
    data_file = tkinter.filedialog.askopenfilename(filetypes = typ, initialdir = dir) 
    with open(data_file, mode='r') as f:
        l = [s.strip() for s in f.readlines()]

        insert_entry(entry[0],l[1].replace("Satellite data path:",""))
        insert_entry(entry[1],l[2].replace("Acolite data path:",""))
        insert_entry(entry[2],int(l[3].replace("luminance:","")))
        insert_entry(entry[3],int(l[4].replace("hist luminance:","")))
        insert_entry(entry[4],int(l[5].replace("px:","")))
        insert_entry(entry[5],int(l[6].replace("py:","")))
        insert_entry(entry[6],int(l[7].replace("deltaX:","")))
        insert_entry(entry[7],int(l[8].replace("deltaY:","")))
        ndvi_value =l[9].replace("NDVI range:","").split("~")
        insert_entry(entry[8],float(ndvi_value[0]))
        insert_entry(entry[9],float(ndvi_value[1]))
        fdi_value =l[10].replace("FDI range:","").split("~")
        insert_entry(entry[10],float(fdi_value[0]))
        insert_entry(entry[11],float(fdi_value[1]))
        insert_entry(entry[12],l[11].replace("file name:",""))
        insert_entry(entry[13],l[12].replace("graph title:",""))
        