#====================================================================
#本プログラムは、AIで「熊」を検出するプログラムです（cocoデータセットの他の番号に変えれば、他の物体も高精度に検出可能です）。
#最近の熊による被害に対して、何か貢献出来ないかと思い、作成しました。
#物体検出結果を保持する変数external_outputを使用し、値によって外部出力して下さい（各種通知、パトライト等の熊への威嚇装置）。
#
#多方向の物体検出を安価に行う為、一台のPCに複数のWEBカメラを接続して運用出来る様にしました。
#十分な処理速度を保てる範囲で、複数台のカメラを接続して下さい（実際の運用ではリアルタイムで検出する必要はないので、６台程度までカメラを接続しても問題ないかと思います）。
#WINDOWS11PROがインストールされたPCを採用する事で、初期設定後はリモートで運用出来ます。
#オープンソースのネットワークソフトウェア、SoftEther VPNを使用する事で、柔軟なネットワークを使用した運用管理が可能になるのではないでしょうか。
#
#用途に応じて、PCを選択して下さい（後付けGPUは高価かなので、今回は非対応にしました）。
#rapberryPI5等のエッジコンピューターも検討しましたが、価格と設定の手間を考えて、保留としました。
#アマゾン社で購入出来る安価なPC等で運用可能です（INTEL社N97やN95で処理時間は約900ミリ秒×カメラの台数となり、PC本体とカメラ１台の費用は3万円前後となります）（AMD社のRyzen7PRO6850Hの処理時間は約250ミリ秒×カメラの台数となり、PC本体とカメラ1台の費用は6万円前後となります）。
#
#環境設定
#必要に応じて、設定ファイル「settings.txt」を編集して下さい（本プログラムのテストは、カメラを熊の画像に向けるか、検出する物体の番号を、熊の21から0にして人を検出してください）。
#ウィンドウズのMicrosoft StoreよりPythonを検索し、最新版をインストールして下さい。
#コマンドプロントで、pip install opencv-pythonを実行してください。
#テキストファイルを作成後、python.exe 「ファイルのパス」/kuma_miru.pyを記述し、ファイルの拡張子を.batに変更して下さい（バッチファイルの作成）。
#ファイル名の例：kuma_miru.bat
#記述の例：python.exe c:/muma_miru/kuma_miru.py
#バッチファイルをウィンドウズのスタートアップ（自動起動）に登録して下さい。
#スタートアップフォルダへの登録方法1：WindowsキーとRキーを同時に押して、「ファイル名を指定して実行」を選択します。
#スタートアップフォルダへの登録方法2：shell:startupと入力して「OK」をクリックします。
#スタートアップフォルダへの登録方法3：先程作成したkuma_miru.batをスタートアップフォルダに移動します。
#パソコン起動後に本プログラムも自動で起動します。
#
#ライセンス
#MIT LISENCE
#配布、改変、商用利用等、全て自由です。
#
#質問等の問い合わせ先
#メールアドレス daiya.seimitsu@gmail.com
#====================================================================


#モジュールの読み込み（変更不可）=======================================
import os #OSの処理に関するモジュールの読み込み
import sys #システムに関するモジュールの読み込み
import time #時間に関するモジュールの読み込み
import multiprocessing #並列処理モジュールの読み込み
import cv2 #画像処理モジュールの読み込み
#====================================================================


#変数設定1（変更不可）=================================================
cap = [] #cam_numで指定したカメラの台数分、VideoCaptureオブジェクトを格納するリスト
timer_start_time = 0 #設定した間隔で検出する為のタイマー用（開始の時間）
timer_current_time = 0 #設定した間隔で検出する為のタイマー用（現在の時間）
elapsed_time = 0 # #設定した間隔で検出する為のタイマー用（経過時間）
external_output = 0 #物体検出を外部機器に出力するか判定するフラグ（#####外部出力処理は未実装#####）
timer_process_start = 0 #検出処理時間計算用（開始時間）
timer_process_end = 0 #検出処理時間計算用（終了時間）
process_time = 0 #検出処理時間計算用（経過時間）
save_picture_num = 0 #写真を保存する際の現在の番号
save_dir_name = "picture" #写真を保存するディレクトリ名
save_picture_path = "" #検出した写真のパス
coco_names = [] #COCOデータセットの物体名を格納するクラス
file = "" #ファイルを読み込む為の変数
detected_name = "" #検出した物体の名前を格納
settings = [] #読み込んだ設定ファイルの各値を格納するリスト
detection_flag =0 #各カメラで対象物を検出したか確認するフラグ
#====================================================================


#設定ファイル内の各値を整形する関数=====================================
def value(settings): #関数を定義
    if "]" not in settings: #取得したデータに]文字があるか確認
        print("] character not found in a line of settings.") #エラーが発生した事を表示
        print("Exiting program.") #エラーが発生した事を表示
        sys.exit() #プログラムを強制終了
    settings = settings.split("]") #]文字で分割してリストに格納
    settings = settings[0].replace(" ", "") #スペース文字を削除
    settings = settings.replace("[", "") #[文字を削除
    print(settings) #整形した設定内容を表示
    return settings #整形した設定を返す
#====================================================================


#設定ファイルの読み込み================================================
print("Reading settings.") #設定ファイルを読み込んでいる事を表示
file = open("settings.txt", "r", encoding="utf-8") #設定ファイルの読み込み
settings = file.readlines() #ファイルの各行をリストに一括読み込み
file.close() #ファイルの読み込み終了
#====================================================================


#変数設定2（カメラ台数、適度な閾値、処理能力に合わせた設定に変更する）=====
cam_num = int(value(settings[0])) #PCに接続したカメラの台数を指定
det_conf = float(value(settings[1])) #検出の信頼度の閾値（小さくなる程誤検出が多くなり、大きくなる程検出しにくくなる）
cap_fps = int(value(settings[2])) #カメラのフレームレート（カメラから、毎秒何枚画像を取得するかを決める値）
timer_interval = int(value(settings[3])) #検出する間隔を秒単位で指定（0はオフ）（電気消費量を軽減します）
save_picture = int(value(settings[4])) #検出写真の保存有無
save_picture_num_MAX = int(value(settings[5])) #検出した写真の保存枚数
class_num = int(value(settings[6])) #21は熊の番号（cocoデータセット80種類内の一つ）（本プログラムのテストは、カメラを熊の画像に向けるか、値を0にして人を検出してください）
#====================================================================


#変数設定3（必要に応じて変更）==========================================
show_conf = 1 #検出した信頼度の表示有無
show_pic = 1 #画像表示有無
show_output = 1 #外部出力フラグの表示有無
show_process = 1 #検出処理時間の表示有無
#====================================================================


#変数設定4（通常は変更不要）===========================================
cap_x = 1024 #カメラ解像度（横）
cap_y = 768 #カメラ解像度（縦）
#====================================================================


#学習済みモデルの読み込み==============================================
cv2.setNumThreads(multiprocessing.cpu_count()) #CPUのコア数分、並列処理出来るように設定
net = cv2.dnn.readNet("yolov4.weights", "yolov4.cfg") #学習済モデルの読み込み
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_DEFAULT) #推論のバックエンドを設定
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU) #推論のデバイスを設定
model = cv2.dnn_DetectionModel(net) #推論モデルを作成
model.setInputParams(size=(416, 416), scale=1/255, swapRB=True) #推論モデルのパラメータを設定
#====================================================================


#カメラ指定した台数分設定==============================================
for i in range(cam_num): #cam_numで指定した回数、VideoCaptureオブジェクトを作成、設定する
    cap.append(cv2.VideoCapture(i, cv2.CAP_DSHOW)) #VideoCaptureオブジェクトを作成
    cap[i].set(3, cap_x) #カメラ解像度（横）を設定
    cap[i].set(4, cap_y) #カメラ解像度（縦）を設定
    cap[i].set(cv2.CAP_PROP_FPS, cap_fps) #カメラのフレームレートを設定
#====================================================================


#メインプログラム=====================================================
file = open("coco.names", "r") #coco.namesファイルの読み込み
coco_names = file.readlines() #ファイルの各行をリストに一括読み込み
file.close() #ファイルの読み込み終了
if os.path.exists(save_dir_name) ==False: #写真を保存するディレクトリが無いか確認
    os.mkdir(save_dir_name) #写真を保存するディレクトリを作成
while(True): #繰り返し処理
    cv2.waitKey(1) #繰り返し処理では、ウィンドウの処理等がフリーズするので、割り込み処理を可能にする
    if timer_start_time == 0: #タイマーが開始していない場合
        timer_start_time = time.time() #タイマーの開始時間を取得
    timer_current_time = time.time() #現在の時間を取得
    elapsed_time = int(timer_current_time - timer_start_time) #経過時間を取得（整数に変換）
    if elapsed_time >= timer_interval: #経過時間が、設定した時間より大きいか確認
        timer_start_time = 0 #タイマーをリセット
        detected_sum = 0 #各カメラで検出した場合に1を加算し、全てのカメラ処理終了後に1以上なら、external_outputを1にする
        for i, j in enumerate(cap): #iはインデクス（0からの番号）、jは各VideoCaptureオブジェクト
            ret, frameA = j.read() #VideoCaptureオブジェクトで、カメラから画像を取得
            if ret: #カメラ画像取得に成功した場合
                detection_flag =0 #各カメラで対象物を検出したか確認するフラグをリセット
                timer_process_start = time.time() #検出処理時間計算用（開始時間）
                classes, scores, boxes = model.detect(frameA , det_conf, 0.1)#物体検出
                for (classid, score, box) in zip(classes, scores, boxes): #検出リスト配列から各検出を取得
                    if classid == class_num: #検出が熊か確認
                        confident = str(int(score * 100)) #検出物の信頼度を格納
                        if show_conf == 1: #検出の信頼度を表示するか確認
                            print("CONFIDENT(BEAR) : " + str(confident) + "%") #検出した信頼度を表示
                        bounds = box #領域の横幅と縦幅を取得
                        xEntent = int(bounds[2]) #領域の長さ（横方向）
                        yExtent = int(bounds[3]) #領域の長さ（縦方向）
                        xCoord = int(bounds[0]) #領域左上の横方向座標を計算
                        yCoord = int(bounds[1]) #領域左上の縦方向座標を計算
                        TX = xCoord #領域左上の横方向座標を格納
                        TY = yCoord #領域左上の縦方向座標を格納
                        BX = xCoord + xEntent #領域右下の横方向座標を格納
                        BY = yCoord + yExtent #領域右下の縦方向座標を格納
                        cv2.rectangle(frameA, (TX, TY), (BX, BY), (256, 256, 256), 2) #検出領域に枠を描画
                        font_size = 1 #フォントサイズを指定
                        font = cv2.FONT_HERSHEY_PLAIN #フォントを指定
                        detected_name = coco_names[classid] #物体番号から、物体名を取得
                        detected_name = detected_name.replace("\r", "") #改行文字を削除
                        detected_name = detected_name.replace("\n", "") #改行文字を削除
                        cv2.putText(frameA, detected_name.upper(), (TX + 2, TY - 7), font, font_size, (256, 256, 256), 2) #ラベル名を描画
                        detected_sum = detected_sum + 1 #検出したとして、1を加算
                        detection_flag = 1 #本カメラで物体を一つ以上検出したとする
                if save_picture == 1 and detection_flag == 1: #写真を保存するか 確認（物体を検出後）
                    save_picture_path = save_dir_name + "/" + str(save_picture_num) + ".jpg" #写真のパスを変数に格納
                    cv2.imwrite(save_picture_path, frameA) #写真番号をファイル名にして、写真を保存
                    save_picture_num = save_picture_num + 1 #次の写真番号にする
                    if save_picture_num == save_picture_num_MAX: #写真番号が上限に達したか確認
                        save_picture_num = 0 #写真番号をリセット
                timer_process_end = time.time() #検出処理時間計算用（終了時間）
                process_time = int((timer_process_end - timer_process_start + 0.0005) * 1000) #検出処理時間計算用（終了時間）（ミリ秒で四捨五入）
                if show_process == 1: #処理時間を表示するか確認
                    print("PROCESS TIME : " + str(int(process_time)) + "ms") #検出時間を表示
                if show_pic == 1: #画像を表示するか確認
                    cv2.imshow("CAMERA NUMBER : " + str(i), frameA) #画像を表示
        if detected_sum > 0: #各カメラで検出したか確認
            external_output = 1 #外部機器に出力（オン）
        else: #検出していない場合
            external_output = 0 #外部機器に出力（オフ）
        if show_output == 1: #外部出力のフラグを表示するか確認
            if external_output == 1: #外部出力フラグが1の場合
                print("EXTERNAL OUTPUT : " + str(external_output)) #外部出力のフラグを表示
            else: #外部出力フラグが0の場合
                print("EXTERNAL OUTPUT : " + str(external_output)) #外部出力のフラグを表示
        if external_output == 1: #外部出力処理（#####外部出力処理は未実装#####）
            external_output = 0 #外部機器に出力（オフ）
            #（#####出力処理をここで実装#####）
#====================================================================
