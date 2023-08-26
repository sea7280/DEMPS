#各パラメータ取得


def getParameters(parameters):

#entryの入力値を配列に格納
    filePath       = parameters[2][0].get()
    filePathAco    = parameters[2][1].get()
    luminance      = int(parameters[2][2].get())
    luminance_hist = int(parameters[2][3].get())
    minX           = int(parameters[2][4].get())
    minY           = int(parameters[2][5].get())
    deltaX         = int(parameters[2][6].get())
    deltaY         = int(parameters[2][7].get())
    ndvi_min       = float(parameters[2][8].get())
    ndvi_max       = float(parameters[2][9].get())
    fdi_min        = float(parameters[2][10].get())
    fdi_max        = float(parameters[2][11].get())
    saveFileName   = parameters[2][12].get()
    title          = parameters[2][13].get()
    teacher        = parameters[2][14].get()
    check          = parameters[5].get()
    textbox        = parameters[3]
    calc           = parameters[4]
    overlap        = parameters[6].get()


#変数：setting_detail
    setting_detail = [filePath,         #0
                      filePathAco,      #1
                      luminance,        #2
                      luminance_hist,   #3
                      minX,             #4
                      minY,             #5
                      deltaX,           #6
                      deltaY,           #7
                      ndvi_min,         #8
                      ndvi_max,         #9
                      fdi_min,          #10
                      fdi_max,          #11
                      saveFileName,     #12
                      title,            #13
                      check,            #14
                      textbox,          #15
                      teacher,          #16
                      calc,             #17
                      overlap           #18
                      ] 
    
    return setting_detail
