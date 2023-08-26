#FDIの算出処理

#ライブラリの読み込み
import sys
sys.dont_write_bytecode = True
import numpy as np
from osgeo import gdal
import tkinter as tk

import DEMPS_getParameters
import DEMPS_pathGet

#fdi算出関数
#引数（ファイルのパス配列、設定配列）
def calc_fdi(parameters):
    filepath = DEMPS_pathGet.pathGet(parameters)
    setting_detail = DEMPS_getParameters.getParameters(parameters)

    #ログの出力
    log = setting_detail[15]
    log.insert(tk.END,"Start calculation FDI.\n")
    log.see("end")
    #衛星データファイルパスの取得
    nirpath     = filepath[9]
    R_RE2path   = filepath[10]
    R_SWIR1path = filepath[11]
    senti_num   = filepath[12]
    #切り抜き範囲設定
    minX      = setting_detail[4]
    minY      = setting_detail[5]
    deltaX    = setting_detail[6]
    deltaY    = setting_detail[7]
    #gdal.Openで画像を読み込みます
    cut_NIR_img  =gdal.Open(nirpath    )
    cut_RE2_img  =gdal.Open(R_RE2path  )
    cut_SWIR1_img=gdal.Open(R_SWIR1path)
    #画像情報を配列に変換します
    NIR_Band_array      = cut_NIR_img.ReadAsArray()
    R_RE2_Band_array    = cut_RE2_img.ReadAsArray()
    R_SWIR1_Band_array  = cut_SWIR1_img.ReadAsArray()
    #範囲指定がなければ切り抜きは行わない
    if deltaX == 0 and deltaY == 0:
        pass
    #切り抜き範囲に合わせて配列の抜き出し
    else:
        NIR_Band_array   = NIR_Band_array[minY:minY+deltaY, minX:minX+deltaX]
        R_RE2_Band_array = R_RE2_Band_array[minY:minY+deltaY, minX:minX+deltaX]
        R_SWIR1_Band_array = R_SWIR1_Band_array[minY:minY+deltaY, minX:minX+deltaX]

    #sentinelの号機に合わせて中心周波数値を切り替え
    if senti_num == 1:  #S2A
        hNIR = 832.8
        hRed = 664.6
        hSWIR1 = 1613.7
    elif senti_num == 2: #S2B
        hNIR = 833.0
        hRed = 665.0
        hSWIR1 = 1610.4

    #FDI算出
    R_NIR = R_RE2_Band_array + ((R_SWIR1_Band_array - R_RE2_Band_array) * ((hNIR - hRed) / (hSWIR1 - hRed)) * 10)
    FDI = NIR_Band_array - R_NIR
    #ログの出力
    log.insert(tk.END,"Complete calculation FDI.\n")
    log.see("end")
    return FDI



