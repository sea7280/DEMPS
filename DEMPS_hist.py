#衛星データのヒストグラム生成ファイル

#ライブラリの読み込み
import matplotlib.pyplot as plt
from osgeo import gdal
import sys
sys.dont_write_bytecode = True
import tkinter as tk

import DEMPS_getParameters
import DEMPS_pathGet

#ヒストグラム生成関数
#引数（ファイルのパス配列、設定配列）
def luminance(parameters):
    filepath = DEMPS_pathGet.pathGet(parameters)
    setting_detail = DEMPS_getParameters.getParameters(parameters)

    log = setting_detail[15]
    log.insert(tk.END,"Start creating a histogram of luminance.\n")
    log.see("end")
    #パス配列から衛星データのパス取得
    bluepath  = filepath[0] #青
    greenpath = filepath[1] #緑
    redpath   = filepath[2] #赤
    nirpath   = filepath[3] #近赤外
    #最大値の設定
    range_max = setting_detail[3]
    #ヒストグラムのタイトル設定
    title     = setting_detail[13]
    #衛星データの読み込み
    band_image1=gdal.Open(bluepath)
    band_image2=gdal.Open(greenpath)
    band_image3=gdal.Open(redpath)
    band_image4=gdal.Open(nirpath)
    #読み込んだデータを配列に変換
    Band_array1 = band_image1.ReadAsArray()
    Band_array2 = band_image2.ReadAsArray()
    Band_array3 = band_image3.ReadAsArray()
    Band_array4 = band_image4.ReadAsArray()

    plt.figure(figsize=(8,4))
    #先ほど配列に変換したデータの輝度値について、500本の柱で表示することにします
    plt.hist(Band_array1.flatten(),bins=500,range=(0, range_max), label="Blue", alpha=0.3, histtype='stepfilled', color="b") 
    plt.hist(Band_array2.flatten(),bins=500,range=(0, range_max), label="Green", alpha=0.3, histtype='stepfilled', color="g") 
    plt.hist(Band_array3.flatten(),bins=500,range=(0, range_max), label="Red", alpha=0.3, histtype='stepfilled', color="r") 
    plt.hist(Band_array4.flatten(),bins=500,range=(0, range_max), label="NIR", alpha=0.3, histtype='stepfilled', color="y") 

    plt.legend()    #判例
    plt.title(title)#タイトル
    plt.show()      #出力
    plt.close()     #集力

