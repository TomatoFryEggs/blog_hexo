
---

title: 记在Windows上一个小需求的折腾过程

urlname: ob82dg

date: 2018-07-03 11:09:13 +0800

tags: []

---

最近将Axure文件从AxureShare迁移到公司内网服务器上，在本地设置了一个网络驱动器，将服务器位置映射到本地，这样就可以使用Auxre自带的一键发送，完美分享。

事情总是不会那么顺利，第二天，发送文件时提示网络驱动器不存在，一看，原来windows开机时居然不会自动连接网络驱动器，需要手动连接一次才能使用。

于是找到net use 命令，制作[开机自动执行脚本bat文件](https://blog.csdn.net/csdnliuxin123524/article/details/78949803)

```powershell
@echo off
start  "wumin" "C:\Windows\System32\cmd.exe" 
net use Z: \\10.110.1.99\shares
taskkill /f /im cmd.exe
exit
```

放到启动目录，开机测试，居然给我弹出黑窗，实在不能忍，难道windows就没有什么类似rc.local的文件可以在后台执行脚本？还真没找到，但找到了可以满足我需求的办法：[制作vbs文件](https://serverfault.com/questions/9038/run-a-bat-file-in-a-scheduled-task-without-a-window/9042)。

```vbscript
Dim WinScriptHost
Set WinScriptHost = CreateObject("WScript.Shell")
WinScriptHost.Run Chr(34) & "C:\Users\Jobin\Documents\autoz.bat" & Chr(34), 0
Set WinScriptHost = Nothing
```

制作成vbs脚本放到启动目录，然后将原来的bat脚本多余的命令注释掉，移动到其他文件夹，搞定。

```powershell
rem @echo off
rem start  "wumin" "C:\Windows\System32\cmd.exe" 
net use Z: \\10.110.1.99\shares
rem taskkill /f /im cmd.exe
rem exit
```

吐槽下自己，没事瞎折腾什么呀！

