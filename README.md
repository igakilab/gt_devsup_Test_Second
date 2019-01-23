# gt_devsup_Test_Second
実験2個目のリポジトリ

プロダクト2つ目　モザイクアート

モザイクアートとは、多数の画像をモザイクのように組み合わせて作成した画像である。

今回は画像処理のライブラリのOpenCVを使用しモザイクアートを作成するプログラムを作成する。

言語はPythonを使用し、以下の3つのファイルを作成する。

・PictureHistograms.py … 画像を比較し類似度を出す。

・SplitPicture 		   … 画像の分割を行ったり、画像を結合してファイルの保存を行う

・MosaicArt			　 … 上記2つをファイルを使用し、モザイクアートを作成する（完成済み）

大雑把な処理の流れ

1. モザイクアートの元となる画像を読み込む。
2. 読み込んだ画像を細かく分割する。
3. モザイクに使用する画像が入ったフォルダを読み込み、画像をまとめて読み込む。
4. 分割した画像と、モザイクに使用する画像の解像度を同じにする。
5. モザイクに使用する画像のカラーヒストグラムを作成する。
6. 分割した画像のカラーヒストグラムを作成する。
7. 分割した画像のヒストグラムとモザイクに使用するヒストグラムを比較し、類似度が一番高い画像を選定する。
8. 選定した画像を結合し、モザイクアートを作成・保存する。

※ヒストグラム … 統計で度数分布を示すグラフで、横軸に階級、縦軸に度数をとり、各階級の度数を長方形の柱で示す。
		
    今回は、横軸に色、縦軸に頻度をとり、それぞれの色がどれだけ使われているかで類似度を算出する。

各ファイルの仕様

PictureHistograms.py

・TrimmingAndResize … 画像を16：9にトリミングした後、指定したサイズに変更する

引数 picture:画像 height,width:リサイズする解像度

返り値 トリミング、リサイズ後の画像

・CreateHistogram … 画像リストからヒストグラムを作成する

引数 picturesFile:画像リスト

返り値 作成したヒストグラムのリスト

・CompareHistograms … ターゲットになる画像のヒストグラムと、比較する画像リストのヒストグラムを比較し、最も類似度の高い画像の添字と類似度を求める

引数 target:ターゲット画像のヒストグラム pictureList:比較する画像のヒストグラムリスト

返り値 最も類似度の高い画像の添字と類似度 [添字,類似度]

・FilesPathList … 指定したディレクトリの指定した拡張子のファイルパスのリストを作成する

引数 path:ディレクトリのパス extension:拡張子

返り値 ファイルパスのリスト

SplitPicture.py

・SplitPicture … 画像ファイルを分割してリストで返す

引数 img:分割する画像 splitHeight:縦の分割数 splitWidth:横の分割数

返り値 分割した画像のリスト

・OutPutPictureList … 2次元リストの画像をそれぞれファイルとして出力する

引数 picList:画像リスト(2次元リスト) outputDirectory:出力先のディレクトリパス

・JoinPictureList … 2次元リストの画像を結合しファイルとして出力する

引数 picList:画像リスト(2次元リスト) outputDirectory:出力先のディレクトリパス


--------------------------------------------------------------------------------------------------------

想定される作成順

PictureHistograms.py

1. トリミングサイズ計算機能の追加
2. CreateHistogramの作成
3. CompareHistogramsの作成

SplitPicture.py

1. 保存する画像リストの作成
2. OutputPictureListの作成
3. JoinPictureListの作成
