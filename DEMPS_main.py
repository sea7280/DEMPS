#ソフトウェアの起動ファイル

#ライブラリの読み込み
import tkinter as tk
import sys
sys.dont_write_bytecode = True


#Applicationクラスの定義
class Application(tk.Frame):
    def __init__(self,master=None):
        super().__init__(master)

        #メインウィンドウの生成
        self.master.geometry("900x600")
        self.master.title("DMPS")
        self.master.configure(bg="black")
        self.master.resizable(width=False, height=False)

#Applicationの実行関数
def main():
    win = tk.Tk()
    app = Application(master=win)
    app.mainloop()


if __name__ == "__main__":
    main()
