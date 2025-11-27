<html>

<head>
<meta http-equiv=Content-Type content="text/html; charset=shift_jis">
<meta name=Generator content="Microsoft Word 15 (filtered)">

</head>

<body lang=JA style='word-wrap:break-word;text-justify-trim:punctuation'>

<div class=WordSection1 style='layout-grid:18.0pt'>

<p class=MsoNormal>「ＫＵＭＡ　ＭＩＲＵ」</p>

<p class=MsoNormal><span lang=EN-US>&nbsp;</span></p>

<p class=MsoNormal><span lang=EN-US>&nbsp;</span></p>

<p class=MsoNormal><span lang=EN-US>&nbsp;</span></p>

<p class=MsoNormal>［概要］</p>

<p class=MsoNormal>本プログラムは、<span lang=EN-US>AI</span>で「熊」を検出するプログラムです（設定ファイルで、<span
lang=EN-US>coco</span>データセットの他の番号に変えれば、他の物体も高精度に検出可能です）。</p>

<p class=MsoNormal>最近の熊による被害に対して、何か貢献出来ないかと思い、作成しました。</p>

<p class=MsoNormal>物体検出結果を保持する変数<span lang=EN-US>external_output</span>を使用し、値によって外部出力して下さい（各種通知、パトライト等の熊への威嚇装置）。</p>

<p class=MsoNormal><span lang=EN-US>&nbsp;</span></p>

<p class=MsoNormal>多方向の物体検出を安価に行う為、一台の<span lang=EN-US>PC</span>に「複数の<span
lang=EN-US>WEB</span>カメラを接続」して運用出来る様にしました。</p>

<p class=MsoNormal>十分な処理速度を保てる範囲で、複数台のカメラを接続して下さい（実際の運用ではリアルタイムで検出する必要はないので、６台程度までカメラを接続しても問題ないかと思います）。</p>

<p class=MsoNormal><span lang=EN-US>WINDOWS11PRO</span>がインストールされた<span
lang=EN-US>PC</span>を採用する事で、初期設定後はリモートで運用出来ます。</p>

<p class=MsoNormal>オープンソースのネットワークソフトウェア、<span lang=EN-US>SoftEther VPN</span>を使用する事で、柔軟なネットワークを使用した運用管理が可能になるのではないでしょうか。</p>

<p class=MsoNormal><span lang=EN-US>&nbsp;</span></p>

<p class=MsoNormal>用途に応じて、<span lang=EN-US>PC</span>を選択して下さい（後付け<span
lang=EN-US>GPU</span>は高価かなので、今回は非対応にしました）。</p>

<p class=MsoNormal><span lang=EN-US>rapberryPI5</span>等のエッジコンピューターも検討しましたが、価格と設定の手間を考えて、保留としました。</p>

<p class=MsoNormal>アマゾン社で購入出来る安価な<span lang=EN-US>PC</span>等で運用可能です（<span
lang=EN-US>INTEL</span>社の<span lang=EN-US>N97</span>や<span lang=EN-US>N95</span>で処理時間は約<span
lang=EN-US>900</span>ミリ秒<span lang=EN-US>×</span>カメラの台数となり、<span lang=EN-US>PC</span>本体とカメラ１台の費用は<span
lang=EN-US>3</span>万円前後となります）（<span lang=EN-US>AMD</span>社の<span lang=EN-US>Ryzen7PRO6850H</span>の処理時間は約<span
lang=EN-US>250</span>ミリ秒<span lang=EN-US>×</span>カメラの台数となり、<span lang=EN-US>PC</span>本体とカメラ<span
lang=EN-US>1</span>台の費用は<span lang=EN-US>6</span>万円前後となります）。</p>

<p class=MsoNormal><span lang=EN-US>&nbsp;</span></p>

<p class=MsoNormal>本プログラムのテストは、カメラを熊の画像に向けるか（精度は落ちます）、「<span lang=EN-US>settings.txt</span>」内にある、検出する物体の番号を、熊の<span
lang=EN-US>21</span>から<span lang=EN-US>0</span>にして人を検出してください。</p>

<p class=MsoNormal>パソコンの起動と同時にプログラムも自動で起動出来る様、「タスクマネージャー」の「スタートアップ アプリ」にある、「新しいタスクを実行する」でプログラムを指定して下さい。</p>

<p class=MsoNormal><span lang=EN-US>&nbsp;</span></p>

<p class=MsoNormal><span lang=EN-US>&nbsp;</span></p>

<p class=MsoNormal><span lang=EN-US>&nbsp;</span></p>

<p class=MsoNormal>［各ファイルの説明］</p>

<p class=MsoNormal><span lang=EN-US>materials</span>フォルダ<span lang=EN-US>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span>資料が入っています</p>

<p class=MsoNormal><span lang=EN-US>0.mp3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span>犬の効果音データ</p>

<p class=MsoNormal><span lang=EN-US>1.mp3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span>犬の効果音データ</p>

<p class=MsoNormal><span lang=EN-US>2.mp3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span>犬の効果音データ</p>

<p class=MsoNormal><span lang=EN-US>coco.names&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span>物体検出名のリスト</p>

<p class=MsoNormal><span lang=EN-US>excutable_files.zip&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span>圧縮された三つの実行ファイル（本フォルダに解凍すれば即時に運用可能）</p>

<p class=MsoNormal><span lang=EN-US>kuma_miru.py&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span>熊を検出するプログラム（検出後の処理は未実装）</p>

<p class=MsoNormal><span lang=EN-US>README.txt&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span>説明書</p>

<p class=MsoNormal><span lang=EN-US>sample_kuma_miru_mail.py&nbsp;&nbsp; </span>熊を検出したらメールを送信するプログラム</p>

<p class=MsoNormal><span lang=EN-US>sample_kuma_miru_sound.py&nbsp; </span>熊を検出したら犬の鳴き声を再生するプログラム</p>

<p class=MsoNormal><span lang=EN-US>sample_settings_mail.txt&nbsp;&nbsp;
sample_kuma_miru_mail</span>の設定ファイル</p>

<p class=MsoNormal><span lang=EN-US>sample_settings_sound.txt&nbsp;
sample_kuma_miru_sound</span>の設定ファイル</p>

<p class=MsoNormal><span lang=EN-US>settings.txt&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span>共通の設定ファイル</p>

<p class=MsoNormal><span lang=EN-US>yolov4.cfg&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
AI</span>の学習モデル</p>

<p class=MsoNormal><span lang=EN-US>yolov4.weights&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
AI</span>の学習済モデル</p>

<p class=MsoNormal><span lang=EN-US>&nbsp;</span></p>

<p class=MsoNormal><span lang=EN-US>&nbsp;</span></p>

<p class=MsoNormal><span lang=EN-US>&nbsp;</span></p>

<p class=MsoNormal>［ライセンス］</p>

<p class=MsoNormal>本プログラム</p>

<p class=MsoNormal><span lang=EN-US>MIT LISENCE</span></p>

<p class=MsoNormal>配布、改変、商用利用等、全て自由です。</p>

<p class=MsoNormal><span lang=EN-US>Apache License 2.0</span>のコードを使用しております（<span
lang=EN-US>OpenCV</span>）。</p>

<p class=MsoNormal><span lang=EN-US>&nbsp;</span></p>

<p class=MsoNormal><span lang=EN-US>Python</span></p>

<p class=MsoNormal><span lang=EN-US>Python Software Foundation License</span></p>

<p class=MsoNormal>成果物の配布、改変、商用利用等、全て自由です。</p>

<p class=MsoNormal><span lang=EN-US>&nbsp;</span></p>

<p class=MsoNormal><span lang=EN-US>Yolov4</span></p>

<p class=MsoNormal><span lang=EN-US>MIT LISENCE</span></p>

<p class=MsoNormal>配布、改変、商用利用等、全て自由です。</p>

<p class=MsoNormal><span lang=EN-US>&nbsp;</span></p>

<p class=MsoNormal><span lang=EN-US>OpenCV</span></p>

<p class=MsoNormal><span lang=EN-US>Apache License 2.0</span></p>

<p class=MsoNormal>配布、改変、商用利用等、全て自由です。</p>

<p class=MsoNormal><span lang=EN-US>&nbsp;</span></p>

<p class=MsoNormal><span lang=EN-US>pyinstaller</span></p>

<p class=MsoNormal><span lang=EN-US>https://github.com/pyinstaller/pyinstaller/wiki/FAQ</span></p>

<p class=MsoNormal>成果物の配布、改変、商用利用等、全て自由です。</p>

<p class=MsoNormal><span lang=EN-US>&nbsp;</span></p>

<p class=MsoNormal><span lang=EN-US>&nbsp;</span></p>

<p class=MsoNormal><span lang=EN-US>&nbsp;</span></p>

<p class=MsoNormal>［感謝］</p>

<p class=MsoNormal><span lang=EN-US>Developer of Python(programming language)</span></p>

<p class=MsoNormal><span lang=EN-US>Python Software Foundation and the
community</span></p>

<p class=MsoNormal><span lang=EN-US>https://www.python.org/</span></p>

<p class=MsoNormal><span lang=EN-US>&nbsp;</span></p>

<p class=MsoNormal><span lang=EN-US>Inventor of yolov1 to yolov3(darknet)</span></p>

<p class=MsoNormal><span lang=EN-US>Joseph Redmon and the community</span></p>

<p class=MsoNormal><span lang=EN-US>https://github.com/pjreddie</span></p>

<p class=MsoNormal><span lang=EN-US>&nbsp;</span></p>

<p class=MsoNormal><span lang=EN-US>Inventor of yolo4(darknet)</span></p>

<p class=MsoNormal><span lang=EN-US>Aleksei Bochkovskii and the community</span></p>

<p class=MsoNormal><span lang=EN-US>https://github.com/AlexeyAB</span></p>

<p class=MsoNormal><span lang=EN-US>&nbsp;</span></p>

<p class=MsoNormal><span lang=EN-US>Developer of image processing module</span></p>

<p class=MsoNormal><span lang=EN-US>OpenCV and the community</span></p>

<p class=MsoNormal><span lang=EN-US>https://github.com/opencv</span></p>

<p class=MsoNormal><span lang=EN-US>&nbsp;</span></p>

<p class=MsoNormal><span lang=EN-US>Developer of software that converts Python
programs to executable file</span></p>

<p class=MsoNormal><span lang=EN-US>pyinstaller and the community</span></p>

<p class=MsoNormal><span lang=EN-US>https://github.com/pyinstaller</span></p>

<p class=MsoNormal><span lang=EN-US>&nbsp;</span></p>

<p class=MsoNormal>フリー効果音素材の提供</p>

<p class=MsoNormal>効果音ラボ</p>

<p class=MsoNormal><span lang=EN-US>https://soundeffect-lab.info/</span></p>

<p class=MsoNormal><span lang=EN-US>&nbsp;</span></p>

<p class=MsoNormal>ロイヤリティフリーの画像の提供</p>

<p class=MsoNormal><span lang=EN-US>pixabay</span></p>

<p class=MsoNormal><span lang=EN-US>https://pixabay.com/</span></p>

</div>

</body>

</html>


