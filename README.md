# Picture Spider

A picture spider for search engine like Baidu (in fact only for Baidu now)

## Features

+ Download pictures in search engine website automatically into a directory
+ All you need to do is just input your keywords and how many picture you want

## How to use

**You should download _python2.7_ before use!**

+ **Method1 :** Download the **PictureSpider** file (rename it as _PictureSpider.exe_ if you're using windows system) and run it. Picture Spider will auto run and create a directory named by your keyword and save the picture in it.
+ **Method2 :** The **PictureSpider.py** is the source code and the **requests** is the library it depends. Download them and run `python PictureSpider` command in your terminal (for Linux) or command line (for Windows).

## Bugs

+ For some how, a few pictures may failed to be downloaded. It might result from the provider of these pictures.
+ If there is no result of the searching, PictureSpider might crush.

## TODO

+ Use deeplearning method to filter the unrelated picture when you searching for someone's photograph.
+ Support for other website like Bing and Google.

