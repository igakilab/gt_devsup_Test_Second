import cv2

#画像ファイルと分割数を指定して画像を分割しリストで返す
#img:分割する画像 splitHeight:縦の分割数 splitWidth:横の分割数
#return 分割した画像のリスト
def SplitPicture(img,splitHeight,splitWidth):
    #元の画像のピクセル
    height = img.shape[0]
    width = img.shape[1]

    #分割後のピクセルを求める
    #分割した画像を入れるリストの作成
    #splitList = [[None for i in range(splitWidth)] for j in range(splitHeight)]



    #画像を分割しリストに入れる
    #追加タスク(タスク名：分割機能の追加)
    # for i in range(splitHeight):

        for j in range(splitWidth):

            clp = img[heightSplit*i:heightSplit*(i+1),widthSplit*j:widthSplit*(j+1)]

            splitList[i][j] = clp
    print("Finished")
    return splitList

#2次元リストの画像をそれぞれ出力する
#picList:画像リスト outputDirectory:出力先のディレクトリのパス
def OutputPictureList(picList,outputDirectory):
    #③


#2次元リストの画像を結合し出力する
#picList:結合する画像リスト outputDirectory:出力先のディレクトリのパス
def JoinPictureList(picList,outputDirectory):

    #横長の画像リスト
    widthJoinList = []

    for heightList in picList:
        #追加タスク(タスク名:JoinPictureListの修正)
        #横に結合する
        #④

    #縦に結合する
    #⑤

    print("JoinFinished")

if __name__ == "__main__":

    print("Input fileName")
    fName = input()

    print("Height")
    height = input()
    height = int(height)

    print("Witdh")
    width = input()
    width = int(width)

    print("SplitPictureOutput? 'y' or 'n'")
    splitFlg = input()
    if(splitFlg == "y"):
        splitFlg = True
    else:
        splitFlg = False

    print("JoinPictureOutput? 'y' or 'n'")
    joinFlg = input()
    if(joinFlg == "y"):
        joinFlg = True
    else:
        joinFlg = False

    print("./" + fName)

    img = cv2.imread("./" + fName)
    outputDirectory = "./after/"

    splitPicList = SplitPicture(img,height,width)

    if(splitFlg):
        OutputPictureList(splitPicList,outputDirectory)
    if(joinFlg):
        JoinPictureList(splitPicList,outputDirectory)
