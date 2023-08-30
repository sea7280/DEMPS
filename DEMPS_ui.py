#UI画面

import tkinter as tk
import sys
sys.dont_write_bytecode = True
from tkinter.scrolledtext import ScrolledText

import DEMPS_truecolor as true
import DEMPS_loadDataFile as loaddata
import DEMPS_exit as exit
import DEMPS_tkraise as tkraise
import DEMPS_ndvi
import DEMPS_fdi
import DEMPS_image as dataImage
import DEMPS_getParameters
import DEMPS_hist as hist
import DEMPS_saveSettings as saveSetting
import DEMPS_loadSetting as readSetting
import DEMPS_writeExcel as excel
import DEMPS_knnRGB as knnRGB
import DEMPS_knn as knn
import DEMPS_loadJudgeLog as JudgeLog
import DEMPS_resulutMapping as heatmap
import DEMPS_customs as custom

#フレームの生成関数
def create_frame(master):
    mainFrame      = tk.Frame(master   , height=480, width=860, bg="gray88")
    customFrame    = tk.Frame(mainFrame, height=480, width=420, bg="gray88", relief=tk.GROOVE, bd=3)
    runFrame       = tk.Frame(mainFrame, height=480, width=420, bg="gray88", relief=tk.GROOVE, bd=3)
    setteingFrame  = tk.Frame(mainFrame, height=480, width=420, bg="gray88", relief=tk.GROOVE, bd=3)

    
    mainFrame.place(     x=0, y=25)
    customFrame.place(   x=5, y=0)
    runFrame.place(      x=435, y=0)
    setteingFrame.place( x=5, y=0)

    frame_list = [setteingFrame,    #0
                    runFrame,       #1
                    customFrame,    #2
                    mainFrame,      #3
                    ]
    return frame_list
#ラベル生成
def create_label(area):
    setteingFrame   = area[0]
    runFrame = area[1]
    customFrame  = area[2]
    

    background = "gray88"
    fontcolor = "black"

################################################# main #################################################
    setpositionY = 30
    label = tk.Label(setteingFrame, text=u'Settings'        , bg=background, fg=fontcolor, font=("",14)).place(x=10, y=0)
    label = tk.Label(setteingFrame, text=u'Load Settings→'   ,
                    bg=background, fg=fontcolor, font=("",13)).place(x=5, y=setpositionY)
    label = tk.Label(setteingFrame, text=u'Data:'           , bg=background, fg=fontcolor, font=("",13)).place(x=5, y=setpositionY + 30)
    label = tk.Label(setteingFrame, text=u'ACOLITE:'        , bg=background, fg=fontcolor, font=("",13)).place(x=5, y=setpositionY + 60)
    label = tk.Label(setteingFrame, text=u'Luminance'       , bg=background, fg=fontcolor, font=("",13)).place(x=50, y=setpositionY + 90)
    label = tk.Label(setteingFrame, text=u'Luminance hist'  , bg=background, fg=fontcolor, font=("",13)).place(x=50, y=setpositionY + 120)
    label = tk.Label(setteingFrame, text=u'Top left point'  , bg=background, fg=fontcolor, font=("",13)).place(x=50, y=setpositionY + 150)
    label = tk.Label(setteingFrame, text=u':'               , bg=background, fg=fontcolor, font=("",13)).place(x=263,y=setpositionY + 151)
    label = tk.Label(setteingFrame, text=u'Sampling range'  , bg=background, fg=fontcolor, font=("",13)).place(x=50, y=setpositionY + 180)
    label = tk.Label(setteingFrame, text=u'×'               , bg=background, fg=fontcolor, font=("",13)).place(x=257,y=setpositionY + 181)
    label = tk.Label(setteingFrame, text=u'NDVI Range'      , bg=background, fg=fontcolor, font=("",13)).place(x=50, y=setpositionY + 210)
    label = tk.Label(setteingFrame, text=u'〜'              , bg=background, fg=fontcolor, font=("",13)).place(x=257,y=setpositionY + 210)
    label = tk.Label(setteingFrame, text=u'FDI Range'       , bg=background, fg=fontcolor, font=("",13)).place(x=50, y=setpositionY + 240)
    label = tk.Label(setteingFrame, text=u'〜'              , bg=background, fg=fontcolor, font=("",13)).place(x=257,y=setpositionY + 240)
    label = tk.Label(setteingFrame, text=u'K-NN Value'      , bg=background, fg=fontcolor, font=("",13)).place(x=50, y=setpositionY + 270)
    label = tk.Label(setteingFrame, text=u'plot title'      , bg=background, fg=fontcolor, font=("",13)).place(x=10, y=setpositionY + 300)
    label = tk.Label(setteingFrame, text=u'Teacher data'    , bg=background, fg=fontcolor, font=("",13)).place(x=5,  y=setpositionY + 360)
    label = tk.Label(setteingFrame, text=u'Overlap ?'       , bg=background, fg=fontcolor, font=("",13)).place(x=50,  y=setpositionY + 390)

################################################# button #################################################
    label = tk.Label(runFrame,      text=u'Run'             , bg=background, fg=fontcolor, font=("",14)).place(x=10, y=0)

################################################# custom #################################################

    label = tk.Label(customFrame, text=u'a : blueband'         , bg=background, fg=fontcolor, font=("",14)).place(x=20,  y=setpositionY)
    label = tk.Label(customFrame, text=u'b : greenband'        , bg=background, fg=fontcolor, font=("",14)).place(x=20,  y=setpositionY+30)
    label = tk.Label(customFrame, text=u'c : redband'          , bg=background, fg=fontcolor, font=("",14)).place(x=20,  y=setpositionY+60)
    label = tk.Label(customFrame, text=u'd : nirband'          , bg=background, fg=fontcolor, font=("",14)).place(x=20,  y=setpositionY+90)
    label = tk.Label(customFrame, text=u'e : acolite blueband' , bg=background, fg=fontcolor, font=("",14)).place(x=200,  y=setpositionY)
    label = tk.Label(customFrame, text=u'f : acolite greenband', bg=background, fg=fontcolor, font=("",14)).place(x=200,  y=setpositionY+30)
    label = tk.Label(customFrame, text=u'g : acolite redband'  , bg=background, fg=fontcolor, font=("",14)).place(x=200,  y=setpositionY+60)
    label = tk.Label(customFrame, text=u'h : acolite nirband'  , bg=background, fg=fontcolor, font=("",14)).place(x=200,  y=setpositionY+90)
    label = tk.Label(customFrame, text=u'i : acolite RE2band'  , bg=background, fg=fontcolor, font=("",14)).place(x=200,  y=setpositionY+120)
    label = tk.Label(customFrame, text=u'j : acolite SWIRband' , bg=background, fg=fontcolor, font=("",14)).place(x=200,  y=setpositionY+150)
    label = tk.Label(customFrame, text=u'ndvi : ndvi'          , bg=background, fg=fontcolor, font=("",14)).place(x=20,  y=setpositionY+120)
    label = tk.Label(customFrame, text=u'fdi  : fdi'            , bg=background, fg=fontcolor, font=("",14)).place(x=20,  y=setpositionY+150)

    label = tk.Label(customFrame, text=u'A', bg=background, fg=fontcolor, font=("",14)).place(x=10,  y=215)
    label = tk.Label(customFrame, text=u'B', bg=background, fg=fontcolor, font=("",14)).place(x=10,  y=305)
    label = tk.Label(customFrame, text=u'Name A', bg=background, fg=fontcolor, font=("",13)).place(x=210,  y=278)
    label = tk.Label(customFrame, text=u'Name B', bg=background, fg=fontcolor, font=("",13)).place(x=210,  y=368)
#entry作成関数
def create_entry(area):
    #出力先を指定
    settingsArea   = area[0]
    #背景色、フォントカラーの指定
    background = "white"
    fontcolor = "black"
    
    #出力座標の基準位置
    setpositionY = 60

    #entryの生成
    entry_file         = tk.Entry(settingsArea, width=50, bg=background, fg=fontcolor, font=("", 8 ))
    entry_acolite_file = tk.Entry(settingsArea, width=50, bg=background, fg=fontcolor, font=("", 8 ))
    entry_lumi         = tk.Entry(settingsArea, width=7 , bg=background, fg=fontcolor, font=("", 14),justify=tk.RIGHT)
    entry_lumi_hist    = tk.Entry(settingsArea, width=7 , bg=background, fg=fontcolor, font=("", 14),justify=tk.RIGHT)
    entry_px           = tk.Entry(settingsArea, width=7 , bg=background, fg=fontcolor, font=("", 14),justify=tk.RIGHT)
    entry_py           = tk.Entry(settingsArea, width=7 , bg=background, fg=fontcolor, font=("", 14),justify=tk.RIGHT)
    entry_deltaX       = tk.Entry(settingsArea, width=7 , bg=background, fg=fontcolor, font=("", 14),justify=tk.RIGHT)
    entry_deltaY       = tk.Entry(settingsArea, width=7 , bg=background, fg=fontcolor, font=("", 14),justify=tk.RIGHT)
    entry_ndvi_min     = tk.Entry(settingsArea, width=4 , bg=background, fg=fontcolor, font=("", 14),justify=tk.RIGHT)
    entry_ndvi_max     = tk.Entry(settingsArea, width=4 , bg=background, fg=fontcolor, font=("", 14),justify=tk.RIGHT)
    entry_fdi_min      = tk.Entry(settingsArea, width=4 , bg=background, fg=fontcolor, font=("", 14),justify=tk.RIGHT)
    entry_fdi_max      = tk.Entry(settingsArea, width=4 , bg=background, fg=fontcolor, font=("", 14),justify=tk.RIGHT)
    entry_k_value      = tk.Entry(settingsArea, width=3 , bg=background, fg=fontcolor, font=("", 14))
    entry_plt_title    = tk.Entry(settingsArea, width=25, bg=background, fg=fontcolor, font=("", 14))
    entry_teacherdata  = tk.Entry(settingsArea, width=45, bg=background, fg=fontcolor, font=("", 8))
    #entry設置

    entry_file.place(        x=80,y=setpositionY  + 5)
    entry_acolite_file.place(x=80,y=setpositionY  + 35)
    entry_lumi.place(        x=200,y=setpositionY + 62)
    entry_lumi_hist.place(   x=200,y=setpositionY + 92)
    entry_px.place(          x=180,y=setpositionY + 122)
    entry_py.place(          x=280,y=setpositionY + 122)
    entry_deltaX.place(      x=180,y=setpositionY + 152)
    entry_deltaY.place(      x=280,y=setpositionY + 152)
    entry_ndvi_min.place(    x=210,y=setpositionY + 182)
    entry_ndvi_max.place(    x=280,y=setpositionY + 182)
    entry_fdi_min.place(     x=210,y=setpositionY + 212)
    entry_fdi_max.place(     x=280,y=setpositionY + 212)
    entry_k_value.place(     x=250,y=setpositionY + 242)
    entry_plt_title.place(   x=130,y=setpositionY + 272)
    entry_teacherdata.place( x=110 ,y=setpositionY + 337)
    
    #enrtyに初期値を設定
    entry_lumi.insert(0,10000)
    entry_lumi_hist.insert(0,10000)
    entry_px.insert(0,0)
    entry_py.insert(0,0)
    entry_deltaX.insert(0,0)
    entry_deltaY.insert(0,0)
    entry_ndvi_min.insert(0,-1)
    entry_ndvi_max.insert(0,1)
    entry_fdi_min.insert(0,0)
    entry_fdi_max.insert(0,0.1)
    entry_k_value.insert(0,7)
    entry_plt_title.insert(0,'data')

    #生成したentryを配列で保持
    entry_list = [entry_file        #0
                ,entry_acolite_file #1
                ,entry_lumi         #2
                ,entry_lumi_hist    #3
                ,entry_px           #4
                ,entry_py           #5
                ,entry_deltaX       #6
                ,entry_deltaY       #7
                ,entry_ndvi_min     #8
                ,entry_ndvi_max     #9
                ,entry_fdi_min      #10
                ,entry_fdi_max      #11
                ,entry_k_value      #12
                ,entry_plt_title    #13
                ,entry_teacherdata] #14
    #entry_listを返す
    return entry_list
#計算ボックス生成
def create_calcbox(area):
    frame = area[2]
    background = "white"
    fontcolor = "black"
    entry_calcboxA = tk.Entry(frame, width=42, bg=background, fg=fontcolor, font=("", 13 ))
    entry_calcboxB = tk.Entry(frame, width=42, bg=background, fg=fontcolor, font=("", 13 ))

    entry_calcboxA.place(x=10, y=240)
    entry_calcboxB.place(x=10, y=330)

    entry_A_name = tk.Entry(frame, width=10, bg=background, fg=fontcolor, font=("", 13 ))
    entry_B_name = tk.Entry(frame, width=10, bg=background, fg=fontcolor, font=("", 13 ))

    entry_A_name.place(x=280, y=280)
    entry_B_name.place(x=280, y=370)

    calcbox = [entry_calcboxA, entry_calcboxB, entry_A_name, entry_B_name]
    return calcbox
#テキストボックスの作成
def create_textbox(area):
    frame = area[1]
    background = "white"
    fontcolor = "black"
    textbox = ScrolledText(frame, font=("",12), height=18, width=48,
                            bg=background, fg=fontcolor)
    textbox.place(x=5, y=180)
    return textbox
#チェックの端生成関数
def create_checkbutton(area, px, py):
    #色の指定
    background = "gray88"
    fontcolor = "black"
    #出力先フレームの設定
    settingsArea = area[0]
# チェックONにする
    bln = tk.BooleanVar()
    bln.set(True)

    # チェックボタン作成
    chk = tk.Checkbutton(settingsArea, variable=bln, bg=background, fg=fontcolor)
    chk.place(x=px, y=py)
    #ウィジェットを返り値として渡す
    return bln
#ボタン生成
def create_button(parameters):
        #引数から各ウィジェットを保持
        master         = parameters[0]
        settingsArea   = parameters[1][0]
        runArea        = parameters[1][1]
        customArea     = parameters[1][2]
        background = "gray88"
        fontcolor = "black"

################################################# change frame #################################################
        Button = tk.Button(master,text=u'setting' , width=8, bg=background, fg=fontcolor,
                        command=lambda:tkraise.change_frame(settingsArea))
        Button.place(x=5,y=3, height=20)
        
#拡張用エリア
        Button = tk.Button(master,text=u'custom', width=8, bg=background, fg=fontcolor,
                        command=lambda:tkraise.change_frame(customArea))
        Button.place(x=73,y=3, height=20)

#終了
        Button = tk.Button(master,text=u'Exit', width=8, bg=background, fg=fontcolor,command=lambda:exit.exit_window(master))
        Button.place(x=141,y=3, height=20)


################################################# function #################################################

#ヒストグラムの生成ボタン
        Button = tk.Button(settingsArea,text=u'hist', width=5, bg=background, fg=fontcolor, font=("",12),
                        command=lambda:hist.luminance(parameters))
        Button.place(x=300,y=148, height=30, width=90)
#衛星データファイルの読み込みボタン
        Button = tk.Button(settingsArea,text=u'...', bg=background, fg=fontcolor, 
                           command=lambda:loaddata.load_dataFile(parameters[2][0]))
        Button.place(x=390, y=63, height=20 , width=20)
        Button = tk.Button(settingsArea,text=u'...', bg=background, fg=fontcolor,
                           command=lambda:loaddata.load_dataFile(parameters[2][1])     )
        Button.place(x=390, y=93, height=20 , width=20)
#設定ファイルの読み込みボタン
        Button = tk.Button(settingsArea,text=u'Load', width=5, bg=background, fg=fontcolor, font=("",12),
                                command=lambda:readSetting.read_setting_file(parameters[2]))
        Button.place(x=150,y=30, height=30, width=90)
#設定のボタン保存
        Button = tk.Button(settingsArea,text=u'Save Settings', bg=background, fg=fontcolor, command=lambda:saveSetting.saveSettings(parameters))
        Button.place(x=300, y=430, height=30 , width=100)
#教師データ選択
        Button = tk.Button(settingsArea,text=u'...', bg=background, fg=fontcolor,
                           command=lambda:loaddata.load_teacherdata(parameters[2][14]))
        Button.place(x=390,y=395, height=20 , width=20)

        #ボタンの生成座標の設定
        setpositionX   = 35
        deltapositionX = 120
        setpositionY   = 50
        deltapositionY = 40

#RGB画像生成
        Button = tk.Button(runArea,text=u'RGB', bg=background, fg=fontcolor, command=lambda:true.truecolor(parameters))
        Button.place(x=setpositionX + deltapositionX*0, y=setpositionY + deltapositionY*0, height=30 , width=110)
#NDVI算出
        def ndvi_image():
                setting_detail = DEMPS_getParameters.getParameters(parameters)
                ndvi_min = setting_detail[8]
                ndvi_max = setting_detail[9]
                title    = setting_detail[13]
                ndvi = DEMPS_ndvi.calc_ndvi(parameters)
                dataImage.image_create(ndvi, ndvi_min, ndvi_max, title)
        Button = tk.Button(runArea,text=u'NDVI', bg=background, fg=fontcolor, command=lambda:ndvi_image())
        Button.place(x=setpositionX + deltapositionX*1, y=setpositionY + deltapositionY*0, height=30 , width=110)
#FDI算出
        def fdi_image():
                setting_detail = DEMPS_getParameters.getParameters(parameters)
                fdi_min = setting_detail[10]
                fdi_max = setting_detail[11]
                title   = setting_detail[13]
                fdi     = DEMPS_fdi.calc_fdi(parameters)
                dataImage.image_create(fdi, fdi_min, fdi_max, title)
        Button = tk.Button(runArea,text=u'FDI', bg=background, fg=fontcolor, command=lambda:fdi_image())
        Button.place(x=setpositionX + deltapositionX*2, y=setpositionY + deltapositionY*0, height=30 , width=110)
#NDVI＆FDI算出
        def ndvi_fdi_image():
                setting_detail = DEMPS_getParameters.getParameters(parameters)
                ndvi_min = setting_detail[8]
                ndvi_max = setting_detail[9]
                fdi_min  = setting_detail[10]
                fdi_max  = setting_detail[11]
                ndvi     = DEMPS_ndvi.calc_ndvi(parameters)
                fdi      = DEMPS_fdi.calc_fdi(parameters)
                dataImage.image_create_double(ndvi, fdi, ndvi_min, ndvi_max, fdi_min, fdi_max)
        Button = tk.Button(runArea,text=u'NDVI&FDI', bg=background, fg=fontcolor, command=lambda:ndvi_fdi_image())
        Button.place(x=setpositionX + deltapositionX*0, y=setpositionY + deltapositionY*1, height=30 , width=110)
#エクセルに保存
        def write_excel():
                ndvi     = DEMPS_ndvi.calc_ndvi(parameters)
                fdi      = DEMPS_fdi.calc_fdi(parameters)
                excel.saveExcel(parameters, ndvi, fdi)
        Button = tk.Button(runArea,text=u'Save Excel', bg=background, fg=fontcolor, command=lambda:write_excel())
        Button.place(x=setpositionX + deltapositionX*1, y=setpositionY + deltapositionY*1, height=30 , width=110)
#分類
        def knn_createImage():
                ndvi     = DEMPS_ndvi.calc_ndvi(parameters)
                fdi      = DEMPS_fdi.calc_fdi(parameters)
                knn_result = knn.knn_judge(ndvi, fdi, parameters)
                knnRGB.knnRGB(parameters, knn_result)
        Button = tk.Button(runArea,text=u'Judge', bg=background, fg=fontcolor, command=lambda:knn_createImage())
        Button.place(x=setpositionX + deltapositionX*2, y=setpositionY + deltapositionY*1, height=30 , width=110)


#解析結果読み込み
        def load_judge():
                log_data = JudgeLog.loadJudgeLog(parameters)
                knnRGB.knnRGB(parameters, log_data)
        Button = tk.Button(runArea,text=u'Load Judge', bg=background, fg=fontcolor, command=lambda:load_judge())
        Button.place(x=setpositionX + deltapositionX*0, y=setpositionY + deltapositionY*2, height=30 , width=110)


#ヒートマップ作成
        
        def create_heatmap():
                log_data = JudgeLog.loadJudgeLog(parameters)
                heatmap.resultMapping(parameters, log_data, False)
        Button = tk.Button(runArea,text=u'heat map', bg=background, fg=fontcolor, command=lambda:create_heatmap())
        Button.place(x=setpositionX + deltapositionX*1, y=setpositionY + deltapositionY*2, height=30 , width=110)

#ヒートマップ作成(数字付き)
        def create_figuremap():
                log_data = JudgeLog.loadJudgeLog(parameters)
                heatmap.resultMapping(parameters, log_data, True)
        Button = tk.Button(runArea,text=u'heat figure', bg=background, fg=fontcolor, command=lambda:create_figuremap())
        Button.place(x=setpositionX + deltapositionX*2, y=setpositionY + deltapositionY*2, height=30 , width=110)

################################################# cal #################################################

#機械学習実行
        def custom_knn():
              custom_data = custom.custom_knn(parameters)
              knnRGB.knnRGB(parameters, custom_data)
        Button = tk.Button(customArea,text=u'knn start', bg=background, fg=fontcolor, command=lambda:custom_knn())
        Button.place(x=250, y=430, height=30 , width=110)



def ui(master):
    framelist = create_frame(master)
    create_label(framelist)

    entry = create_entry(framelist)
    calcbox = create_calcbox(framelist)
    textbox = create_textbox(framelist)
    overlap_chk         = create_checkbutton(framelist, px=125, py=420)

    parameters_list = [master,                   #0
                    framelist,              #1
                    entry,                  #2
                    textbox,                #3
                    calcbox,                #4
                    overlap_chk]            #5

    create_button(parameters_list)