
from osgeo import gdal
import tkinter as tk
import os
import sys
sys.dont_write_bytecode = True

import DEMPS_getParameters
import DEMPS_pathGet



#NDVIの算出
def calc_ndvi(parameters):
    filepath = DEMPS_pathGet.pathGet(parameters)
    setting_detail = DEMPS_getParameters.getParameters(parameters)

    log = setting_detail[15]
    log.insert(tk.END,"Start calculation NDVI.\n")
    log.see("end")
#--------------------------------------------- path 

    redpath = filepath[2]
    nirpath = filepath[3]

#--------------------------------------------- range

    minX      = setting_detail[4]
    minY      = setting_detail[5]
    deltaX    = setting_detail[6]
    deltaY    = setting_detail[7]

#--------------------------------------------- tif 

    band4_8bit_path =os.path.dirname(__file__) + "/tif_file/Band4_8bit.tif"
    band8_8bit_path =os.path.dirname(__file__) + "/tif_file/Band8_8bit.tif"

#---------------------------------------------- 配列変換 
    gdal.Translate(band4_8bit_path ,redpath ,srcWin=[minX,minY,deltaX,deltaY])
    gdal.Translate(band8_8bit_path ,nirpath ,srcWin=[minX,minY,deltaX,deltaY])

    b4_image =gdal.Open(band4_8bit_path)
    b8_image =gdal.Open(band8_8bit_path)

    RedBand_array       = b4_image.ReadAsArray()
    NIR_Band_array      = b8_image.ReadAsArray()

#DN→反射率に変換
    RedBand_array      = RedBand_array      / 10000
    NIR_Band_array     = NIR_Band_array     / 10000

    ndvi = (NIR_Band_array - RedBand_array)/(NIR_Band_array + RedBand_array)

    log.insert(tk.END,"Complete calculation NDVI.\n")
    log.see("end")
    
    return ndvi