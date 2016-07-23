## Introduction:

​	This is a tiny tool used to convert a python script(e.g. demo.py -> demo.command) into a executable file(only for mac)

## Usage:

Before use it, you should ensure:

- You're using Mac OS.
- The python on your system is same version as on your scripts.

Here's' how you use `CIC`  to create a new executable file base on you original script :

- #### Simple way:

​	Double-click to open  **CIC.command** . Enter the file name of  your python script(or path).then,you can get a executable file,its name is the same as your script,but its extension is **.command** .**it will not change your original  script**.

​	Interestingly，you can also use CIC.py to convert itself into a executable file,then you can get a file ,the same as CIC.command .

- #### In terminal:

```
$ python CIC.py demo.py
```

you can also use:

```
$ python CIC.py
```

you can use it to get more info.

It worked for me ,Mac OS 10.11 ,python 2.7.11 .



## 介绍：

​	这是一个简单的工具，作用是将一个python脚本直接转换为可执行文件(只供mac系统使用)。

## 如何使用：

使用之前，你必须确保：

- 你的系统是Mac OS。
- 系统中的python版本和脚本中的python版本一致。

#### 简单的方法:

​	双击打开CIC.command文件。输入你需要转换的文件名（或者路径）。然后，你就可以得到一个与脚本名字相同，但是扩展名不同的可执行文件。程序不会改变你原来的脚本文件。

#### 使用终端:

- 请切换到CIC.py的目录，使用如下命令:

```
$ python CIC.py demo.py
```

- 你也可以使用：

```
$ python CIC.py
```

程序会进一步提示输入文件名并输出更多信息。

​	有趣的是，你可以使用CIC.py将其自身转换为可执行文件。得到的可执行文件和CIC.command相同。

​	在我的使用环境下该程序运行良好，Mac OS 10.11,python 2.7.11。

