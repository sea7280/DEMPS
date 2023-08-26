#ソフトウェアの終了処理

#ライブラリの読み込み
import sys
sys.dont_write_bytecode = True

#ソフトウェアの終了関数
def exit_window(master):          #終了
    master.destroy()