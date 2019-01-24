# -*- coding: UTF-8 -*-

import cv2
import glob

#画像を16:9にトリミング、指定サイズにリサイズする
#picture:画像 height:縦 width:横
#return トリミング、リサイズ後の画像
def TrimmingAndResize(picture,height,width):
    #画像の縦横を取得
    picHeight = picture.shape[0]
    picWidth  = picture.shape[1]

    #画像を16:9にトリミングするサイズを計算する
    #①
    cutHeight = 0
    cutWidth  = (16 * picHeight) //9
 
    if(picHeight &lt; picWidth and picWidth &gt;= cutWidth):
        cutHeight = picHeight
    else:
        cutHeight = (9 * picWidth) // 16
        cutWidth  = picWidth
 
revHeight = (picHeight - cutHeight) // 2
revWidth  = (picWidth  - cutWidth ) // 2

    #画像を中央寄せでトリミングする
    #追加タスク
    #②
    picture = picture[revHeight:revHeight + cutHeight, revWidth:revWidth + cutWidth]
    #画像をリサイズする
    #追加タスク
    #③

    return picture

#画像リストを取得しヒストグラムを作成
#picturesFile:画像を入れたリスト
#return ヒストグラムのリスト
def CreateHistogram(picturesFile):
    histograms = []

    for picture in picturesFile:
        #ヒストグラムの作成、追加
        #④

    return histograms

#一つの画像と画像リストのヒストグラムを比較し、最も類似した添字と数値を返す
#target:比較画像のヒストグラム pictureList:比較対象のヒストグラムリスト
#return 最も類似した画像 :リスト[対象の添字,比較した値]
def CompareHistograms(target,pictureList):
    maxCompareHist = [0,0.0]

    #targetとリストを比較し、最大値を保存する
    for i in range(len(pictureList)):
        #⑤

    return maxCompareHist

#ディレクトリ内の指定された拡張子のファイルパスのリストを作成する
#path:ディレクトリのパス extension:拡張子
#return ファイルパスのリスト
def FilesPathList(path,extension):
    fileNameList = glob.glob(path + "/*" + extension)
    return fileNameList

if __name__ == '__main__':
    height =  90
    width  = 160

    path = "./pictures"
    extension = ".png"

    #画像パス入力
    pictureFileNameList = FilesPathList(path,extension)

    picturesList = []
    i = 0
    #画像の取得、トリミング、リサイズ
    for fileName in pictureFileNameList:
        img = cv2.imread(fileName)
        img = TrimmingAndResize(img,height,width)
        picturesList.append(img)
        cv2.imwrite("./after/hoge{}.png".format(i),img)
        i += 1
    #ヒストグラム作成
    histogram = CreateHistogram(picturesList)

    print("画像を比較しますか？(y or n)")
    flg = input()
    if(flg == "y"):
        print("比較する画像のパスを入力")
        compFileName = input()
        target = TrimmingAndResize(cv2.imread(compFileName),height,width)
        targetHist = cv2.calcHist([target],[0],None,[256],[0,256])

        maxCompareHist = CompareHistograms(targetHist,histogram)

        print("targetに一番類似した画像は以下の通りです。")
        print("path = {}".format(pictureFileNameList[maxCompareHist[0]]))
        print("類似値 = {}".format(maxCompareHist[1]))

    print("終了します")
