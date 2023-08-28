
#ライブラリの読み込み
import pandas as pd
import os
from osgeo import gdal
import datetime
import numpy as np
import tkinter as tk
# k-近傍法（k-NN）
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
import pickle
import sys
sys.dont_write_bytecode = True
import warnings
warnings.simplefilter('ignore', UserWarning)
#オーバーサンプリング
from imblearn.over_sampling import SMOTE
from tkinter import filedialog

import DEMPS_fdi as fdi_calc
import DEMPS_ndvi as ndvi_calc
import DEMPS_getParameters
import DEMPS_pathGet

def custom_knn(parameters):
    filepath = DEMPS_pathGet.pathGet(parameters)
    setting_detail = DEMPS_getParameters.getParameters(parameters)
#ログの出力先
    log = setting_detail[15]
    start_time = datetime.datetime.now()
    log.insert(tk.END,"Start time : " + str(start_time)+"\n")
    log.see("end")


#式の取得
    equationA = setting_detail[14][0].get()
    equationB = setting_detail[14][1].get()

    #切り出しの詳細
    minX          = setting_detail[4]
    minY          = setting_detail[5]
    deltaX        = setting_detail[6]
    deltaY        = setting_detail[7]
    #空変数の用意
    BlueBand_array       = None
    GreenBand_array      = None
    RedBand_array        = None
    NIR_Band_array       = None
    aco_BlueBand_array   = None
    aco_GreenBand_array  = None
    aco_RedBand_array    = None
    aco_NIR_Band_array   = None
    aco_RE2_Band_array   = None
    aco_SWIR1_Band_array = None
    ndvi_result          = None
    fdi_result           = None

    """文字列に衛星データ変数が含まれるか判定
       必要な変数のみデータを保持することでメモリへの負担を軽減"""
    #判定、保持の処理を関数化
    #データを保持する変数を引数としている

    def haveData(pathNum):
        path = filepath[pathNum]
        band_8bit_path =os.path.dirname(__file__) + "/Band_8bit.tif"
        gdal.Translate(band_8bit_path,path  ,srcWin=[minX,minY,deltaX,deltaY])
        b8_image=gdal.Open(band_8bit_path)
        band_array  = b8_image.ReadAsArray()
        band_array  = band_array  / 10000
        return band_array

    #acoliteデータ用
    def haveAcoData(pathNum):
        path = filepath[pathNum]
        cut_img = gdal.Open(path)
        band_array  = cut_img.ReadAsArray()
        if deltaX == 0 and deltaY == 0:
            pass
        #切り抜き範囲に合わせて配列の抜き出し
        else:
            band_array = band_array[minY:minY+deltaY, minX:minX+deltaX]
        return band_array

    if 'a' in equationA or 'a' in equationB:
        BlueBand_array = haveData(0)
    if 'b' in equationA or 'b' in equationB:
        GreenBand_array = haveData(1)
    if 'c' in equationA or 'c' in equationB:
        RedBand_array = haveData(2)
    if 'd' in equationA or 'd' in equationB:
        NIR_Band_array = haveData(3)
    if 'e' in equationA or 'e' in equationB:
        aco_BlueBand_array = haveAcoData(6)
    if 'f' in equationA or 'f' in equationB:
        aco_GreenBand_array = haveAcoData(7)
    if 'g' in equationA or 'g' in equationB:
        aco_RedBand_array = haveAcoData(8)
    if 'h' in equationA or 'h' in equationB:
        aco_NIR_Band_array = haveAcoData(9)
    if 'i' in equationA or 'i' in equationB:
        aco_RE2_Band_array = haveAcoData(10)
    if 'j' in equationA or 'j' in equationB:
        aco_SWIR1_Band_array = haveAcoData(11)
    if 'ndvi' in equationA or 'ndvi' in equationB:
        ndvi_result = ndvi_calc.calc_ndvi(parameters)
    if 'fdi' in equationA or 'fdi' in equationB:
        fdi_result = fdi_calc.calc_fdi(parameters)

##################################################################################################
    #変数へ割り当て
    a = BlueBand_array       
    b = GreenBand_array      
    c = RedBand_array        
    d = NIR_Band_array       
    e = aco_BlueBand_array   
    f = aco_GreenBand_array  
    g = aco_RedBand_array    
    h = aco_NIR_Band_array   
    i = aco_RE2_Band_array   
    j = aco_SWIR1_Band_array 
    ndvi = ndvi_result
    fdi  = fdi_result

#入力した計算式の実行

    calc_equationA = eval(equationA)
    calc_equationB = eval(equationB)

#################################### 機械学習実行 #####################################

    #変数名取得
    nameA = setting_detail[14][2].get()
    nameB = setting_detail[14][3].get()

    #ログ出力
    log.insert(tk.END,"calc " + nameA + "  " + str(calc_equationA[0][0]) + "～" +"\n")
    log.insert(tk.END,"calc " + nameB + "  " + str(calc_equationB[0][0]) + "～" +"\n")
    log.see("end")

    #教師データの読み込み
    excel_path = setting_detail[16]
    if excel_path == "":
        log.insert(tk.END,"Please Select a teacher data" + "\n")
        log.see("end")
    else:
        excel_file = pd.read_excel(excel_path)
        #データのコピー
        df_X = excel_file.copy()
        df_Y = excel_file.copy()

        df_X = df_X.drop('検出物質',axis=1)         #Excelデータから属性データのみを取り出す
        drop_idx = [nameA,nameB]#取得したExcelデータから目的変数のみを取り出す
        df_Y = df_Y.drop(drop_idx,axis=1)
        #オーバーサンプリング処理で教師データの増量
        sm = SMOTE(k_neighbors=5) 
        df_X, df_Y = sm.fit_resample(df_X, df_Y)
        #ログ出力
        log.insert(tk.END,"Complete over sampling.\n")
        log.see("end")
        
        result_data = []

        #標準化
        sc = StandardScaler()
        sc.fit(df_X)
        df_X = sc.transform(df_X)
        raw = len(calc_equationA)
        row = len(calc_equationA[0])
            
        calc_equationA = calc_equationA.flatten()
        calc_equationB  = calc_equationB.flatten()
        data = np.array([calc_equationA, calc_equationB])
        data = sc.transform(data.T)
        calc_equationA = data.T[0].reshape(raw, row)
        calc_equationB  = data.T[1].reshape(raw, row)
        data = None
        log.insert(tk.END,"Complete standardization.\n")
        log.see("end")

        log.insert(tk.END,"Start Knn\n")
        log.see("end")
        kValue = setting_detail[12]
        model = KNeighborsClassifier(n_neighbors=kValue) #k-NNインスタンス
        model.fit(df_X, df_Y.values.ravel())
        for count_all in range(len(calc_equationA)):
            result_data_row = []
            for count in range(len(calc_equationA[count_all])):
                target = [[calc_equationA[count_all][count],calc_equationA[count_all][count]]]
                target = pd.DataFrame(target,columns = [nameA,nameB])
                target = target.fillna(0)
                # 構築したモデルから検出物を判定
                judge_data = model.predict(target)
                result_data_row.append(judge_data[0])
            result_data.append(result_data_row)

    #log用
        ftype=[('pickleファイル', '*.pickle')]
        idir=os.path.join(os.environ['USERPROFILE'], 'Desktop')
        with open(filedialog.asksaveasfilename(defaultextension='pickle', filetypes=ftype, initialdir=idir), mode='wb') as f:
            pickle.dump(result_data, f)

        end_time = datetime.datetime.now()
        log.insert(tk.END,"End time : " + str(end_time)+"\n")
        log.see("end")
        return result_data


