# Challenge Name: Misplaced

***
file.whatが渡される
~~~
$ binwalk file.what 

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
1048576       0x100000        Zip archive data, encrypted at least v2.0 to extract, compressed size: 282364, uncompressed size: 287052, name: Article1.jpg
1331114       0x144FAA        End of Zip archive, comment: "Password: 3a24869a641d60c09ceb71af4f99cffc"
~~~
binwalkを使うとzipとパスワードがわかる

ZIPにしてPassword: 3a24869a641d60c09ceb71af4f99cffcで解凍するとArticle1.jpgが見つかる
~~~
$ strings Article1.jpg 
[Content_Types].xml 
1+'RE
@;5VwK
wx6Gms*
_rels/.rels 
jH[{
l0/%
word/document.xml
~~~
stringsコマンドでワードだとわかる

wordとして開くとフラグがある

![aa](https://github.com/xn16h7/CTF/blob/master/SecureBug%20CTF/securebugctfimg/writeup3.png)

### BCTF{n1c3_c4rv1n6_w3ll_d0n3}
