#解析結果のRGB画像出力

import matplotlib.pyplot as plt
from osgeo import gdal
import matplotlib.image as mpimg
import os
import tkinter as tk
import sys
sys.dont_write_bytecode = True
from PIL import Image
Image.MAX_IMAGE_PIXELS = None

import DEMPS_getParameters
import DEMPS_pathGet

def knnRGB(parameters, judegedata):
    setting_detail = DEMPS_getParameters.getParameters(parameters)
    filepath = DEMPS_pathGet.pathGet(parameters)

    log = setting_detail[15]
    log.insert(tk.END,"Generate RGB images from analysis results.\n")
    log.see("end")

    bluepath  = filepath[0]
    greenpath = filepath[1]
    redpath   = filepath[2]

    #-------------------------------- カラー合成 -------------------------------
    band2_8bit_path=os.path.dirname(__file__) + "/Band2_8bit.tif"
    band3_8bit_path=os.path.dirname(__file__) + "/Band3_8bit.tif"
    band4_8bit_path=os.path.dirname(__file__) + "/Band4_8bit.tif"

    #切り出しの詳細
    minX          = setting_detail[4]
    minY          = setting_detail[5]
    deltaX        = setting_detail[6]
    deltaY        = setting_detail[7]
    max_luminance = setting_detail[2]

    #各バンドのファイルを、それぞれ、関心領域のみ切り出す。出力は8bitのgeotifとする
    #gdal.Translate({出力画像名}, {入力画像名}, outputType={データ形式設定} , scaleParams=[[min,max]], srcWin=[minX,minY,deltaX,deltaY])
    gdal.Translate(band2_8bit_path,bluepath,  scaleParams=[[0,max_luminance]],outputType=gdal.GDT_Byte, srcWin=[minX,minY,deltaX,deltaY])
    gdal.Translate(band3_8bit_path,greenpath, scaleParams=[[0,max_luminance]],outputType=gdal.GDT_Byte, srcWin=[minX,minY,deltaX,deltaY])
    gdal.Translate(band4_8bit_path,redpath,   scaleParams=[[0,max_luminance]],outputType=gdal.GDT_Byte, srcWin=[minX,minY,deltaX,deltaY])

    #作成した8bitの切り出し画像を読み込む
    b2_image=gdal.Open(band2_8bit_path)
    b3_image=gdal.Open(band3_8bit_path)
    b4_image=gdal.Open(band4_8bit_path)

    #読み込んだ画像を配列に変換する
    BlueBand_array  = b2_image.ReadAsArray()
    GreenBand_array = b3_image.ReadAsArray()
    RedBand_array   = b4_image.ReadAsArray()

#解析結果ごとに色付け
    size_y = len(judegedata)
    size_x = len(judegedata[0])
    count = 0
    for y in range(size_y):
        for x in range(size_x):
            if judegedata[y][x] == "plastic":
                RedBand_array[y][x] = 255
                GreenBand_array[y][x] = 0
                BlueBand_array[y][x] = 0
                count = count + 1
            elif judegedata[y][x] == "ship":
                RedBand_array[y][x] = 0
                GreenBand_array[y][x] = 0
                BlueBand_array[y][x] = 255
            elif judegedata[y][x] == "water":
                pass
            elif judegedata[y][x] == "wood":
                pass
            elif judegedata[y][x] == "pumice":
                pass

    log.insert(tk.END,"plastic pixel : " + str(count) + ".\n")
    log.see("end")

    #出力ファイルの設定のために、入力ファイルのX方向のピクセル数、Y方向のピクセル数を読み出す
    Xsize=b2_image.RasterXSize #band2の画像のX方向ピクセル数
    Ysize=b2_image.RasterYSize #band2の画像のY方向ピクセル数
    dtype=gdal.GDT_Byte
    band=3

    #出力ファイルの設定を行う(True Color)
    out_True_path =os.path.dirname(__file__) + "/truecolor.tif"    #出力ファイル名
    out1= gdal.GetDriverByName('GTiff').Create(out_True_path, Xsize, Ysize, band, dtype)#({出力ファイル名}, {X方向のピクセル数},{Y方向のピクセル数},{バンド数},{データ形式})

    #出力ファイルの座標系を設定する
    out1.SetProjection(b2_image.GetProjection())      #{出力変数}.SetProjection(座標系情報)
    out1.SetGeoTransform(b2_image.GetGeoTransform())  #{出力変数}.SetGeoTransform(座標に関する６つの数字)

    #Red、Green、Blueバンドの配列を、WriteArrayを用いて出力ファイルの3バンドに書き込む
    out1.GetRasterBand(1).WriteArray(RedBand_array)   #赤の配列を赤バンドに書き込む
    out1.GetRasterBand(2).WriteArray(GreenBand_array) #緑の配列を緑バンドに書き込む
    out1.GetRasterBand(3).WriteArray(BlueBand_array)  #青の配列を青バンドに書き込む
    out1.FlushCache()

    #---------------------------------------- 出力 -----------------------------------------

    plt.figure(figsize=(7,5))

    image1 = mpimg.imread(out_True_path)
    plt.imshow(image1)
    plt.title(setting_detail[13])

    #不要なので削除
    b2_image = None
    b3_image = None
    b4_image = None
    out1     = None
    os.remove(band2_8bit_path)
    os.remove(band3_8bit_path)
    os.remove(band4_8bit_path)
    os.remove(out_True_path)

    plt.show()
    plt.close()


