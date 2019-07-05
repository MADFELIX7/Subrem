# Subrem：字幕文件批量重命名

**Please scroll down for the English version.**

一个用于将字幕文件批量改为对应视频文件名的python脚本（字幕文件的后缀仍将保留）

**使用方法：**

`subrem.py [path*] [video suffix] [subtitle suffix]`

依次输入路径 视频后缀 字幕后缀即可将字幕重命名为对应的视频文件名。

（要求视频文件与字幕文件原来的顺序都是正确的。即指定字幕后缀的按字幕排序第一的字幕文件将会被命名为指定视频后缀字幕排序第一的视频文件名。字幕文件可能有很多，只要指定后缀的顺序与视频顺序对应即可。这样说有点绕，可以参考下面的例子。）

* **可以直接输入视频和字幕后缀**，这默认在脚本所在的路径下搜索文件。

* **支持组合后缀**，你可以通过这一点指定被修改的语言，如简体中文字幕常以.chs.ass为后缀，可以直接输入，中间不能有空格。

* 路径中一般都有非常规字符，如空格等，所以如果手动输入路径的话请加上双引号。

* 脚本只是重命名字幕文件副本，对原字幕文件没有影响。

处理前：


| 视频文件名 | 原字幕文件名|
|:-:|:-:|
|show1.mkv|sub_show1.en.ass|
|show2.mkv|sub_show2.en.ass|
|   ...   |   ...   |



`python3 subrem.py [path] .mkv .en.ass` 或者 `python3 subrem.py .mkv .en.ass`


| 视频文件名 | 新字幕文件名|
|:-:|:-:|
|show1.mkv|show1.en.ass|
|show2.mkv|show2.en.ass|
|   ...   |   ...   |

# Subrem: subtitle batch renaming

A python script makes subtitle files to have the same name as video files (the suffix of subtitle files will remain unchanged). 

**Usage:**

`python3 subrem.py [path*] [video suffix] [subtitle suffix]`

Input paragram in the order of: the path of video and sub files, video suffix and subtitle suffix, the script will rename all sub files according to the order of video files.

* You can also just input the suffixes, which will use current directory as working directory.

* Like the example below, strings like `.en.ass` will also be seen as suffixes, so you can decide which language of sub files you want to rename.

* It is recommended to add double quotation marks arround your manually input directory path.

* The script will rename a copy of your sub files, so there is no worry about your original sub files, just feel free to try :)

For example:


| Video filename | Original Sub filename|
|:-:|:-:|
|show1.mkv|sub_show1.en.ass|
|show2.mkv|sub_show2.en.ass|
|   ...   |   ...   |


`python3 subrem.py [path] .mkv .en.ass` OR `python3 subrem.py .mkv .en.ass`


| Video filename | New Sub filename|
|:-:|:-:|
|show1.mkv|show1.en.ass|
|show2.mkv|show2.en.ass|
|   ...   |   ...   |
