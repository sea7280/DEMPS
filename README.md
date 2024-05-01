# DEMPS
DEtecting Marine Plastic using Satellite software

2023/8/22　作業開始
2022年　亀田研究室　佐久間　卒論にて作成したソフトウェア「DMPS」の最新版

開発環境
環境名：demps
Activate：.\demps\Scripts\activate

2023/8/28
ver1.0 作業完了

ファイルの役割（簡潔に）
DEMPS\DEMPS_crossEvaluate.py    :設定した教師データから交差検証の実行、グラフ化を行う処理
DEMPS\DEMPS_customs.py          :自身で設定した変数を用いてKNN分類を行う処理 結果はpickleファイルに保存される
DEMPS\DEMPS_exit.py             :ソフトウェアの終了処理
DEMPS\DEMPS_fdi.py              :設定した衛星データからFDIを算出する処理
DEMPS\DEMPS_getParameters.py    :各ウィジェットに入力した値を配列に格納する処理 変数の管理を簡易化するために行う
DEMPS\DEMPS_hist.py             :設定した衛星データのヒストグラムを生成する処理
DEMPS\DEMPS_image.py            :画像生成処理
DEMPS\DEMPS_knn.py              :算出したFDI、NDVIから教師データ（エクセルファイル）をもちいてKNN分類を行う処理 結果はpickleファイルに保存される
DEMPS\DEMPS_knnRGB.py           :KNN分類結果からプラスチックの検出画像を生成する
DEMPS\DEMPS_loadDataFile.py     :ファイル選択ダイアログ処理 衛星データや教師データを選択するときの処理
DEMPS\DEMPS_loadJudgeLog.py     :pickleファイルを読み込む処理
DEMPS\DEMPS_loadSetting.py      :保存していた設定ファイル（.txt）を読み込み、各ウィジェットに値を入力する処理
DEMPS\DEMPS_main.py             :メインの実行処理 ここでソフトが起動する
DEMPS\DEMPS_ndvi.py             :設定した衛星データからNDVIを算出する処理
DEMPS\DEMPS_pathGet.py          :設定した衛星データフォルダ内の各バンドを識別して変数にパスを入力するプログラム 
DEMPS\DEMPS_resulutMapping.py   :分類結果のヒートマップを生成する処理
DEMPS\DEMPS_saveSettings.py     :現在の各ウィジェットに入力されている値をテキストファイルに保存する処理
DEMPS\DEMPS_tkraise.py          :画面の切り替え処理
DEMPS\DEMPS_truecolor.py        :設定した衛星データからRGB画像を生成する処理
DEMPS\DEMPS_ui.py               :UI画面の処理
DEMPS\DEMPS_writeExcel.py       :設定した衛星の各バンドデータから設定している範囲のデータをエクセルに入力して保存する処理

