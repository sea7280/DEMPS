# パス取得

import glob
import sys

sys.dont_write_bytecode = True


def pathGet(parameters):
    entry = parameters[2]
    data_file = entry[0].get()
    filecheck = glob.glob(data_file + "/**/*10m", recursive=True)  # L2Aチェック
    l1c_check = glob.glob(data_file + "/**/*.jp2", recursive=True)  # Lc1チェック
    if len(filecheck) > 0:  # L2Aデータ
        R10m = filecheck[0]
        R20m = glob.glob(data_file + "/**/*20m", recursive=True)[0]
        bluepath = glob.glob(R10m + "/**B02_10m.jp2", recursive=True)[0]
        greenpath = glob.glob(R10m + "/**B03_10m.jp2", recursive=True)[0]
        redpath = glob.glob(R10m + "/**B04_10m.jp2", recursive=True)[0]
        nirpath = glob.glob(R10m + "/**B08_10m.jp2", recursive=True)[0]
        R_RE2path = glob.glob(R20m + "/**B06_20m.jp2", recursive=True)[0]
        R_SWIR1path = glob.glob(R20m + "/**B11_20m.jp2", recursive=True)[0]
    elif len(filecheck) == 0 and len(l1c_check) > 4:  # L1C
        bluepath = glob.glob(data_file + "/**/*B02.jp2", recursive=True)[0]
        greenpath = glob.glob(data_file + "/**/*B03.jp2", recursive=True)[0]
        redpath = glob.glob(data_file + "/**/*B04.jp2", recursive=True)[0]
        nirpath = glob.glob(data_file + "/**/*B08.jp2", recursive=True)[0]
        R_RE2path = glob.glob(data_file + "/**/*B06.jp2", recursive=True)[0]
        R_SWIR1path = glob.glob(data_file + "/**/*B11.jp2", recursive=True)[0]
    else:
        bluepath = None  # 初期設定
        greenpath = None  # 初期設定
        redpath = None  # 初期設定
        nirpath = None  # 初期設定
        R_RE2path = None  # 初期設定
        R_SWIR1path = None  # 初期設定
        type_sentinel = 1

    data_file = entry[1].get()
    acolite_check = glob.glob(data_file + "/**/*.tif", recursive=True)  # acoliteチェック
    if len(acolite_check) > 4 and "S2A" in acolite_check[0]:  # ACOLITE S2Aデータ
        bluepath_aco = glob.glob(data_file + "/**rhos_492.tif", recursive=True)[0]
        greenpath_aco = glob.glob(data_file + "/**rhos_560.tif", recursive=True)[0]
        redpath_aco = glob.glob(data_file + "/**rhos_665.tif", recursive=True)[0]
        nirpath_aco = glob.glob(data_file + "/**rhos_833.tif", recursive=True)[0]
        R_RE2path_aco = glob.glob(data_file + "/**rhos_740.tif", recursive=True)[0]
        R_SWIR1path_aco = glob.glob(data_file + "/**rhos_1614.tif", recursive=True)[0]
        type_sentinel = 1  # S2Aデータ
    elif len(acolite_check) > 4 and "S2B" in acolite_check[0]:  # ACOLITE S2Bデータ
        bluepath_aco = glob.glob(data_file + "/**rhos_492.tif", recursive=True)[0]
        greenpath_aco = glob.glob(data_file + "/**rhos_559.tif", recursive=True)[0]
        redpath_aco = glob.glob(data_file + "/**rhos_665.tif", recursive=True)[0]
        nirpath_aco = glob.glob(data_file + "/**rhos_833.tif", recursive=True)[0]
        R_RE2path_aco = glob.glob(data_file + "/**rhos_739.tif", recursive=True)[0]
        R_SWIR1path_aco = glob.glob(data_file + "/**rhos_1610.tif", recursive=True)[0]
        type_sentinel = 2  # S2Bデータ
    else:
        bluepath_aco = None  # 初期設定
        greenpath_aco = None  # 初期設定
        redpath_aco = None  # 初期設定
        nirpath_aco = None  # 初期設定
        R_RE2path_aco = None  # 初期設定
        R_SWIR1path_aco = None  # 初期設定
        type_sentinel = 1

    satellite_data_list = [
        bluepath,  # 0
        greenpath,  # 1
        redpath,  # 2
        nirpath,  # 3
        R_RE2path,  # 4
        R_SWIR1path,  # 5
        bluepath_aco,  # 6
        greenpath_aco,  # 7
        redpath_aco,  # 8
        nirpath_aco,  # 9
        R_RE2path_aco,  # 10
        R_SWIR1path_aco,  # 11
        type_sentinel,
    ]  # 12

    return satellite_data_list
