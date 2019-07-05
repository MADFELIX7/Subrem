#coding=utf-8
import sys,os,shutil

def printhelp():
    print('''
    使用方法：subrem [path*] [video suffix] [subtitle suffix]
    依次输入路径 视频后缀 字幕后缀即可将字幕重命名为对应字母顺序的视频文件名
    也可以直接输入视频和字幕后缀，这将在脚本所在的路径下搜索文件
    后缀数目不限，如中文字幕常以.cht.ass为后缀，可以直接输入
    路径中一般都有非常规字符，如空格等，所以如果手动输入路径的话请加上双引号
    ''')
    exit(0)

try:
    if(sys.argv[1][0]=='-' or sys.argv[1][0]=='h'):
        printhelp()

except IndexError:
    printhelp()

else:
    if(sys.argv[1][0]=='.'):
        path = os.getcwd()
        vd_suffix = sys.argv[1]
        sub_suffix = sys.argv[2]
    else:
        path = sys.argv[1]
        vd_suffix = sys.argv[2]
        sub_suffix = sys.argv[3]

    vd_name = []
    sub_name = []
    for file in os.listdir(path):
        if file.endswith(vd_suffix):
            vd_name.append(file)
    for file in os.listdir(path):
        if file.endswith(sub_suffix):
            sub_name.append(file)
    #print(vd_name)
    #print('\n')
    #print(sub_name)
    i=0
    for file in os.listdir(path):
        if file.endswith(sub_suffix):
            newname = vd_name[i].replace(vd_suffix,sub_suffix)
            #print(newname)
            shutil.copyfile(os.path.join(path,sub_name[i]),os.path.join(path,newname))
            i+=1
            #os.rename()