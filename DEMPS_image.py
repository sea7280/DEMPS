#画像出力ファイル

#ライブラリの読み込み
import matplotlib.pyplot as plt
import sys
sys.dont_write_bytecode = True
from PIL import Image
Image.MAX_IMAGE_PIXELS = None

#画像生成（1枚）関数
#引数（出力データ、出力最小値、出力最大値、出力タイトル）
def image_create(data,min,max,title):

        plt.figure(figsize=(7,5))
        #画像と合わせてヒストグラムを出力　出力範囲はmin〜max
        plt.hist(data.flatten(),bins=300,range=(min, max))

        plt.figure(figsize=(7,5))
        #データの画像化　カラーマップは白〜オレンジ
        plt.imshow(data,vmin=min,vmax=max,cmap='Oranges')
        plt.title(title)
        plt.colorbar()  #カラースケール
        plt.show()      #出力
        plt.close()     #終了

#画像生成（2枚）関数
#引数（データ1（NDVI）、データ2（FDI）、1の最小値、1の最大値、2の最小値、2の最大値）
def image_create_double(dataA,dataB,minA,maxA,minB,maxB):

        plt.figure(figsize=(10,6))
        plt.subplot(1,2,1)
        #NDVIの画像化　カラーマップは白〜オレンジ
        plt.imshow(dataA,vmin=minA,vmax=maxA,cmap='Oranges')
        plt.title("NDVI")
        plt.colorbar()

        plt.subplot(1,2,2)
        #NFDIの画像化　カラーマップは白〜オレンジ
        plt.imshow(dataB,vmin=minB,vmax=maxB,cmap='Oranges')
        plt.title("FDI")
        plt.colorbar()  #カラースケール
        plt.show()      #出力
        plt.close()     #終了

