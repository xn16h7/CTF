# Protected Directory

Find the flag in the protected directory.
http://167.71.246.232/
---

下記にアクセスするとBasic認証を求められる
> http://167.71.246.232:8080/admin/

下記にアクセスするとadminのパスワードがある
> http://167.71.246.232/admin/.htpasswd  
> admin:$apr1$1U8G15kK$tr9xPqBn68moYoH4atbg20

ハッシュ化してあるので復号化をする必要がある
パスワードクラッカーのJohn the Ripperというツールを使う

~~~
$ john htpasswd.txt 
Loaded 1 password hash (md5crypt [MD5 32/64 X2])
Press 'q' or Ctrl-C to abort, almost any other key for status
0g 0:00:00:13 3/3 0g/s 20353p/s 20353c/s 20353C/s 021684..021683
0g 0:00:00:15 3/3 0g/s 20364p/s 20364c/s 20364C/s barcide..barcidy
0g 0:00:00:17 3/3 0g/s 20396p/s 20396c/s 20396C/s abric..abrat
0g 0:00:00:22 3/3 0g/s 20439p/s 20439c/s 20439C/s bermero..bermena
0g 0:00:00:28 3/3 0g/s 20480p/s 20480c/s 20480C/s jasmot..jasmet
0g 0:00:00:29 3/3 0g/s 20444p/s 20444c/s 20444C/s kusto..kust1
0g 0:00:00:30 3/3 0g/s 20448p/s 20448c/s 20448C/s 057747..057745
0g 0:00:00:31 3/3 0g/s 20450p/s 20450c/s 20450C/s 181123..181121
0g 0:00:00:32 3/3 0g/s 20455p/s 20455c/s 20455C/s 064322..064326
0g 0:00:00:33 3/3 0g/s 20460p/s 20460c/s 20460C/s ciahoe..ciahor
0g 0:00:00:34 3/3 0g/s 20459p/s 20459c/s 20459C/s boremma..boremmm
0g 0:00:00:35 3/3 0g/s 20468p/s 20468c/s 20468C/s 214515..214512
0g 0:00:00:37 3/3 0g/s 20483p/s 20483c/s 20483C/s lamyl..lamyn
0g 0:00:00:38 3/3 0g/s 20485p/s 20485c/s 20485C/s stumn1..stumns
0g 0:00:00:39 3/3 0g/s 20489p/s 20489c/s 20489C/s bront1..bronti
0g 0:00:00:40 3/3 0g/s 20496p/s 20496c/s 20496C/s amtpi..amtpq
0g 0:00:00:41 3/3 0g/s 20501p/s 20501c/s 20501C/s anggota..anggote
0g 0:00:00:42 3/3 0g/s 20505p/s 20505c/s 20505C/s magsy6..mags99
0g 0:00:00:43 3/3 0g/s 20509p/s 20509c/s 20509C/s bol103..bol102
0g 0:00:00:44 3/3 0g/s 20517p/s 20517c/s 20517C/s 216763..216764
0g 0:00:00:45 3/3 0g/s 20516p/s 20516c/s 20516C/s 147129..147146
0g 0:00:00:46 3/3 0g/s 20523p/s 20523c/s 20523C/s 040338..040361
0g 0:00:00:47 3/3 0g/s 20530p/s 20530c/s 20530C/s jm0752..jm0748
alesh16          (admin)
1g 0:00:00:50 3/3 0.01979g/s 20542p/s 20542c/s 20542C/s alesh16..alesh09
Use the "--show" option to display all of the cracked passwords reliably
Session completed

alesh16          (admin)
~~~

ログイン
> admin/alesh16
![aa](https://github.com/xn16h7/CTF/blob/master/Tenable%20CTF%202021/img/%E2%91%A7.png)

## flag{cracked_the_password} 
