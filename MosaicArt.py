# -*- coding: UTF-8 -*-

import cv2
import PictureHistograms as his
import SplitPicture as split


if __name__ == "__main__":
    #元画像の読み込み
    print("モザイクアートにする画像の読み込み")
    print("画像ファイルの入力")
    fileName = input()
    img = cv2.imread("./" + fileName)

    if(img is None):
        print("画像ファイル読み込み失敗")

    print("最終画像サイズの指定 横 enter 縦")
    width = input()
    height = input()

    if(width == "" or height == ""):
        width = 1920
        height = 1080
    else:
        width = int(width)
        height = int(height)

    img = his.TrimmingAndResize(img,height,width)

    #元画像の分割
    print("分割数の指定\n")
    cutCount = input()
    if(cutCount == ""):
        cutCount = 32
    else:
        cutCount = int(cutCount)
    
    splitPictures = split.SplitPicture(img,cutCount,cutCount)

    #モザイク画像読み込み
    print("モザイクに使用する画像の読み込み")
    print("使用する画像があるディレクトリの入力 相対パスor絶対パス")
    directoryPath = input()
    print("使用する画像の拡張子")
    extension = input()

    if(directoryPath == ""):
        directoryPath = "./pictures"
    if(extension == ""):
        extension = ".png"

    #出力先ディレクトリの指定
    print("画像出力先ディレクトリを指定")
    outputDirectoryPath = input()
    if(outputDirectoryPath == ""):
        outputDirectoryPath = "./after/"

    #画像のパスリストの取得
    filePathList = his.FilesPathList(directoryPath,extension)

    print("読み込み中")

    #画像の読み込み,トリミング,リサイズ
    allPicture = []
    for filePath in filePathList:
        img = cv2.imread(filePath)
        if(img is None):
            print("画像ファイル読み込み失敗")
        img = his.TrimmingAndResize(img,height // cutCount,width // cutCount)
        allPicture.append(img)

    print("処理中")

    #元画像、モザイク画像ヒストグラムの作成
    splitHistogram = []
    for heightSplitPic in splitPictures:
        histogramList = his.CreateHistogram(heightSplitPic)
        splitHistogram.append(histogramList)
        print("HeightSplitPic = {}".format(len(heightSplitPic)))

    print("splitHistogram = {}".format(len(splitHistogram)))
    
    allPicHistogram = his.CreateHistogram(allPicture)


    #ヒストグラムの比較、画像の選定
    joinPictureList = [[None for i in range(cutCount)] for j in range(cutCount)]

    for i in range(cutCount):
        for j in range(cutCount):
            maxCompHist = his.CompareHistograms(splitHistogram[i][j],allPicHistogram)
            joinPictureList[i][j] = allPicture[maxCompHist[0]]

    #画像の結合
    split.JoinPictureList(joinPictureList,outputDirectoryPath)

    print("モザイクアート作成終了")
    print("Mission Complete!!")