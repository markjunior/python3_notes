```
sed 's/dude/Colt/g' report.txt > report_new.txt

echo "Welcome To The Geek Stuff" | sed 's/\(\b[A-Z]\)/\(\1\)/g'
```



# Chmod

chgrp: 改变文件所属用户组
chown: 改变文件所有者
chmod: 改变文件的权限

Read is equivalent to ‘4’.
Write is equivalent to ‘2’.
Execute is equivalent to ‘1’

```
chomd 777 path/to/file
```

[d]  --> 表示是一个目录
[-] --> 表示是一个文件
[|] --> 表示为连接文件（linkfile）
[b] --> 表示设备文件里面的可供存储的接口设备
[c] --> 表示设备文件里面的串行端口设备，例如键盘，鼠标（一次性读取设备）

r (read): 可读取此文件的实际内容，如读取文本文件的文字内容等
w(write): 可以编辑，新增或者修改该文件的内容（但能不能删除这个文件与这个用户有没有这个文件的write权限无关）
x(execute): 该文件具有可以被系统执行的权限，在windows中一个文件是否具有执行的能力，是根据 “拓展名” 来判断的，例如.exe, .bat, .com等，但是在linux下面，我们的文件是否能被执行则是由是否具有 “x” 这个权限来决定的，而与文件名没有绝对关系。
权限对目录的重要性
r(read contents in directory) : 表示具有读取目录结构列表的权限，也就是可以利用ls命令查询该目录下的文件名数据
w(modify contents of directory): 表示具有更改该目录结构列表的权限，就是：
新建新的文件与目录
删除已经存在的文件与目录（跟该文件有什么权限无关）
将已存在的文件或目录重命名
转移该目录内的文件，目录位置
x(access directory): 代表用户能否进入该目录
