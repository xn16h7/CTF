#Challenge Name: Flag Script

アクセス時に下記通信が飛ぶ
***
GET /flagscript/flagscript.js HTTP/1.1
Host: 18.194.166.81
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0
Accept: */*
Accept-Language: ja,en-US;q=0.7,en;q=0.3
Accept-Encoding: gzip, deflate
Connection: close
Referer: http://18.194.166.81/flagscript/
If-Modified-Since: Mon, 01 Feb 2021 05:09:06 GMT
If-None-Match: "8f7-5ba3f5a67a080-gzip"
Cache-Control: max-age=0

HTTP/1.1 200 OK
Server: nginx/1.10.3 (Ubuntu)
Date: Mon, 15 Feb 2021 16:26:57 GMT
Content-Type: application/javascript
Content-Length: 2295
Connection: close
Last-Modified: Mon, 01 Feb 2021 05:09:06 GMT
ETag: "8f7-5ba3f5a67a080-gzip"
Accept-Ranges: bytes
Vary: Accept-Encoding

var _0x2edb=['split','height','concat','462146ImhqlY','floor','width','getElementById','571444xYNRvZ','888334BBTblW','length','rgba(0,\x200,\x200,\x200.04)','clear','#0F0','log','fillText','1VNTbrE','random','px\x20arial','2771251YYnHzb','1ehyRvF','getContext','256435bQmXAe','fillStyle','canvasObject','598270VFUica','1163546aJJHzJ','innerWidth'];var _0x44a7=function(_0x239d1d,_0x2f7f45){_0x239d1d=_0x239d1d-0x169;var _0x2edb04=_0x2edb[_0x239d1d];return _0x2edb04;};var _0x26ff06=_0x44a7;(function(_0x330f9e,_0x1bb3f1){var _0x50d8d0=_0x44a7;while(!![]){try{var _0x597e7a=-parseInt(_0x50d8d0(0x16b))+parseInt(_0x50d8d0(0x170))*-parseInt(_0x50d8d0(0x180))+-parseInt(_0x50d8d0(0x174))+-parseInt(_0x50d8d0(0x182))+parseInt(_0x50d8d0(0x17c))*parseInt(_0x50d8d0(0x175))+-parseInt(_0x50d8d0(0x16a))+parseInt(_0x50d8d0(0x17f));if(_0x597e7a===_0x1bb3f1)break;else _0x330f9e['push'](_0x330f9e['shift']());}catch(_0x2e09ef){_0x330f9e['push'](_0x330f9e['shift']());}}}(_0x2edb,0x94600));var canvasObj=document[_0x26ff06(0x173)](_0x26ff06(0x169)),ctx=canvasObj[_0x26ff06(0x181)]('2d');canvasObj[_0x26ff06(0x16e)]=window['innerHeight'],canvasObj[_0x26ff06(0x172)]=window[_0x26ff06(0x16c)];var matrix='ABCDEFGHIJKLMNOPQRSTUWXYZ0123456789@#$%&^*()';matrix=matrix[_0x26ff06(0x16d)]('');var fontSize=0xa,columns=canvasObject[_0x26ff06(0x172)]/fontSize,drops=[],a='S',xx='_',ab='}',c='C',d='T',e='F',f='{',g='n',r='c',bg='0',fv='B',i='t',j='_',k='a',m='n',n='i',o='c',u='e',jj='e',q='_',s='o',kk='d',flag=a[_0x26ff06(0x16f)](fv,c,d,e,f,g,bg,i,j,k,xx,m,n,o,jj,q,r,s,kk,u,ab);console[_0x26ff06(0x17a)](flag);for(var x=0x0;x<columns;x++){drops[x]=0x1;}function draw(){var _0x531c57=_0x26ff06;ctx[_0x531c57(0x183)]=_0x531c57(0x177),ctx['fillRect'](0x0,0x0,canvasObject[_0x531c57(0x172)],canvasObject[_0x531c57(0x16e)]),ctx[_0x531c57(0x183)]=_0x531c57(0x179),ctx['font']=fontSize+_0x531c57(0x17e);for(var _0x2e7d69=0x0;_0x2e7d69<drops['length'];_0x2e7d69++){var _0x41a070=matrix[Math[_0x531c57(0x171)](Math[_0x531c57(0x17d)]()*matrix[_0x531c57(0x176)])];ctx[_0x531c57(0x17b)](_0x41a070,_0x2e7d69*fontSize,drops[_0x2e7d69]*fontSize),drops[_0x2e7d69]*fontSize>canvasObject[_0x531c57(0x16e)]&&Math[_0x531c57(0x17d)]()>0.975&&(drops[_0x2e7d69]=0x0),drops[_0x2e7d69]++;}}console[_0x26ff06(0x178)](),setInterval(draw,0x23);
***
---

>a='S',xx='_',ab='}',c='C',d='T',e='F',f='{',g='n',r='c',bg='0',fv='B',i='t',j='_',k='a',m='n',n='i',o='c',u='e',jj='e',q='_',s='o',kk='d',

下記値を上記に置き換えればフラグ
>flag=a[_0x26ff06(0x16f)](fv,c,d,e,f,g,bg,i,j,k,xx,m,n,o,jj,q,r,s,kk,u,ab)

---

`SBCTF{n0t_a_nice_code}`
