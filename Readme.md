## Introduction:

​	This is a tiny tool used to convert a python script(e.g. demo.py -> demo.command) to a executable file(only for mac),so that you are able to use it anywhere.

## Usage:

Before use it, you should ensure:

- You're using Mac OS.
- The python on your system is same version as on your scripts.

Here's' how you use `CIC`  to create a new executable file base on you original script :

- #### Simple way:

  ​	Firstly,open a terminal to elevate the permission of **CIC.command** .Concrete methods are:

  ```
  $ cd [where the CIC.command is located]
  $ chmod +x CIC.command
  ```

  ​	then,Double-click to open  **CIC.command** . Enter the file name of  your python script(or path).then,you can get a executable file,its name is the same as your script,but its extension is **.command**. and what's more,**it will not change your original  script**.

  Interestingly，you can also use CIC.py to convert itself into a executable file,then you can get a file ,the same as CIC.command .

- #### In terminal:

Please change your current working directory to the directory where the CIC.py  is located.replace demo.py with your script name.don't forget to add extension.

```
$ python CIC.py demo.py
```

you can also use:

```
$ python CIC.py
```

you can use it to get more info.

Operating environment : Mac OS 10.11 ,python 2.7.11 .



## 介绍：

​	这是一个简单的工具，作用是将一个python脚本直接转换为可执行文件(只供mac系统使用)。如此，你可以在系统的任何地方运行这个脚本。

## 如何使用：

使用之前，你必须确保：

- 你的系统是Mac OS。
- 系统中的python版本和脚本中的python版本一致。

#### 简单的方法:

​	首先，你需要提升CIC.command的权限来打开它。

```
$ cd [将方框和方框内的内容替换为CIC.command的目录]
$ chmod +x CIC.command
```

​	然后，双击打开CIC.command文件。输入你需要转换的文件名（或者路径）。之后，你就可以得到一个与脚本名字相同，但是扩展名不同的可执行文件。程序不会改变你原来的脚本文件。

#### 使用终端:

​	或者你也可以使用CIC.py来实现文件转换。

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

​	运行环境:Mac OS 10.11,python 2.7.11。

