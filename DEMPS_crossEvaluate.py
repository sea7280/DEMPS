#4.2 DMPSでの検出精度の把握　に使用

#https://nakano-tomofumi.hatenablog.com/entry/2017/11/09/142828

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
# k-近傍法（k-NN）
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import (cross_val_predict, KFold)
import warnings
warnings.filterwarnings('ignore')
#オーバーサンプリング
from imblearn.over_sampling import SMOTE
import itertools
import tkinter as tk

import DEMPS_getParameters

def evaluate(parameters):

    setting_detail = DEMPS_getParameters.getParameters(parameters)

    log = setting_detail[15]

    kValue = setting_detail[12]
    excel_path = setting_detail[16]

    excel_file = pd.read_excel(excel_path)

    df_X = excel_file.copy()                    # データをコピーする。
    df_Y = excel_file.copy()

    df_X = df_X.drop('検出物質',axis=1)         #取得したExcelデータから属性データのみを取り出す
    drop_idx = ['NDVI','FDI']#取得したExcelデータから目的変数のみを取り出す
    df_Y = df_Y.drop(drop_idx,axis=1)

    #オーバーサンプリング
    sm = SMOTE(k_neighbors=5) 

    df_X, df_Y = sm.fit_resample(df_X, df_Y)

    '''
    #標準化
    sc = StandardScaler()
    sc.fit(df_X)
    df_X = sc.transform(df_X)
    '''

    model = KNeighborsClassifier(n_neighbors=kValue) 
    model.fit(df_X , df_Y.values.ravel()) #学習モデル構築。引数に訓練データの特徴量と、それに対応したラベル

    y_pred = cross_val_predict(model,df_X , df_Y,cv=KFold(n_splits=10, shuffle=True))
    conf_mat = confusion_matrix(df_Y,y_pred)


    def plot_confusion_matrix(cm, classes, normalize=False, title='Confusion matrix', cmap=plt.cm.Blues):
        """
        This function prints and plots the confusion matrix.
        Normalization can be applied by setting `normalize=True`.
        """
        if normalize:
            cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
            log.insert(tk.END,"Normalized confusion matrix" + "\n")
            log.see("end")
        else:
            log.insert(tk.END,"Confusion matrix, without normalization" + "\n")
            log.see("end")
        #print(cm)
        plt.imshow(cm, interpolation='nearest', cmap=cmap)
        plt.title(title)
        plt.colorbar()
        tick_marks = np.arange(len(classes))
        plt.xticks(tick_marks, classes, rotation=45)
        plt.yticks(tick_marks, classes)
        fmt = '.2f' if normalize else 'd'
        thresh = cm.max() / 2.
        for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
            plt.text(j, i, format(cm[i, j], fmt),
                    horizontalalignment="center",
                    color="white" if cm[i, j] > thresh else "black")
        plt.tight_layout()
        plt.ylabel('True label')
        plt.xlabel('Predicted label')

    classnames = ['water', 'plant', 'plastic', 'pumice', 'sand', 'cloud', 'ship', 'rock', 'wood']
    plot_confusion_matrix(conf_mat, list(classnames))
    log.insert(tk.END,"Cross Evaluate Complete" + "\n")
    log.see("end")
    plt.show()
    plt.close()