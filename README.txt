「ＫＵＭＡ　ＭＩＲＵ」



［概要］
本プログラムは、AIで「熊」を検出するプログラムです（設定ファイルで、cocoデータセットの他の番号に変えれば、他の物体も高精度に検出可能です）。
最近の熊による被害に対して、何か貢献出来ないかと思い、作成しました。
物体検出結果を保持する変数external_outputを使用し、値によって外部出力して下さい（各種通知、パトライト等の熊への威嚇装置）。

多方向の物体検出を安価に行う為、一台のPCに「複数のWEBカメラを接続」して運用出来る様にしました。
十分な処理速度を保てる範囲で、複数台のカメラを接続して下さい（実際の運用ではリアルタイムで検出する必要はないので、６台程度までカメラを接続しても問題ないかと思います）。
WINDOWS11PROがインストールされたPCを採用する事で、初期設定後はリモートで運用出来ます。
オープンソースのネットワークソフトウェア、SoftEther VPNを使用する事で、柔軟なネットワークを使用した運用管理が可能になるのではないでしょうか。

用途に応じて、PCを選択して下さい（後付けGPUは高価かなので、今回は非対応にしました）。
rapberryPI5等のエッジコンピューターも検討しましたが、価格と設定の手間を考えて、保留としました。
アマゾン社で購入出来る安価なPC等で運用可能です（INTEL社のN97やN95で処理時間は約900ミリ秒×カメラの台数となり、PC本体とカメラ１台の費用は3万円前後となります）（AMD社のRyzen7PRO6850Hの処理時間は約250ミリ秒×カメラの台数となり、PC本体とカメラ1台の費用は6万円前後となります）。

本プログラムのテストは、カメラを熊の画像に向けるか（精度は落ちます）、「settings.txt」内にある、検出する物体の番号を、熊の21から0にして人を検出してください。
パソコンの起動と同時にプログラムも自動で起動出来る様、「タスクマネージャー」の「スタートアップ アプリ」にある、「新しいタスクを実行する」でプログラムを指定して下さい。



［各ファイルの説明］
materialsフォルダ          資料が入っています
0.mp3                      犬の効果音データ
1.mp3                      犬の効果音データ
2.mp3                      犬の効果音データ
coco.names                 物体検出名のリスト
excutable_files.zip        圧縮された三つの実行ファイル（本フォルダに解凍すれば即時に運用可能）
(https://github.com/DAIKICHI-PSC/KUMA-MIRU/releases/download/VERSION1.0/excutable_files.zip)
kuma_miru.py               熊を検出するプログラム（検出後の処理は未実装）
README.txt                 説明書
sample_kuma_miru_mail.py   熊を検出したらメールを送信するプログラム
sample_kuma_miru_sound.py  熊を検出したら犬の鳴き声を再生するプログラム
sample_settings_mail.txt   sample_kuma_miru_mailの設定ファイル
sample_settings_sound.txt  sample_kuma_miru_soundの設定ファイル
settings.txt               共通の設定ファイル
yolov4.cfg                 AIの学習モデル
yolov4.weights             AIの学習済モデル（ダウンロードして、同じフォルダに入れて下さい）
(https://github.com/DAIKICHI-PSC/KUMA-MIRU/releases/download/VERSION1.0/yolov4.weights)　



［ライセンス］
本プログラム
MIT LISENCE
配布、改変、商用利用等、全て自由です。
Apache License 2.0のコードを使用しております（OpenCV）。

Python
Python Software Foundation License
成果物の配布、改変、商用利用等、全て自由です。

Yolov4
MIT LISENCE
配布、改変、商用利用等、全て自由です。

OpenCV
Apache License 2.0
配布、改変、商用利用等、全て自由です。

pyinstaller
https://github.com/pyinstaller/pyinstaller/wiki/FAQ
成果物の配布、改変、商用利用等、全て自由です。



［感謝］
Developer of Python(programming language)
Python Software Foundation and the community
https://www.python.org/

Inventor of yolov1 to yolov3(darknet)
Joseph Redmon and the community
https://github.com/pjreddie

Inventor of yolo4(darknet)
Aleksei Bochkovskii and the community
https://github.com/AlexeyAB

Developer of image processing module
OpenCV and the community
https://github.com/opencv

Developer of software that converts Python programs to executable file
pyinstaller and the community
https://github.com/pyinstaller

フリー効果音素材の提供
効果音ラボ
https://soundeffect-lab.info/

ロイヤリティフリーの画像の提供
pixabay
https://pixabay.com/



［問い合わせ先］
daiya.seimitsu@gmail.com
