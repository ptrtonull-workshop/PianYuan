-
[![Build Status](https://travis-ci.com/ptrtonull-workshop/PianYuan.svg?branch=master)](https://travis-ci.com/ptrtonull-workshop/PianYuan)

[English](./README-EN.md)

## 爬取
你可以使用以下命令，把[此处](http://pianyuan.la/mv?order=score)的电影到数据库里
```python
python main.py -G start end host username password
```
其中：
- `-G`：代表`get`，获取信息
- start：爬取的开始页，比如start等于3的时候对应的网站是[此处](http://pianyuan.la/mv?order=score&p=3)
- end：爬取的结束页，比如end等于3的时候对应的网站是[此处](http://pianyuan.la/mv?order=score&p=3)
- host：数据库的地址
- username：数据库用户的用户名
- password：数据库用户的密码

如果你的数据库账号没有密码，即密码为空，那你可以执行下面的命令来达到相同的效果
```python
python main.py -G start end host username
```
此外，你还可以使用以下命令来查看数据库中的数据条数
```
python main.py -M number localhost root root
```
> 当然，如果你要看更详细的条目，请直接登录数据库查看
## 开发
在你开发时，我们为你准备了协助性的命令脚本，格式为：

```python
python main.py -S action
```
其中：
- `-S`：代表`shell`，标记此条语句执行的是一些协助性的命令脚本
- action：代表要执行的动作，目前支持的动作有：
  - init
  - beautify
  - test

当你得到本项目的源码时，你第一步要做的就是安装项目所需要的初始化文件，你可以使用
```python
python main.py -S init
```

当你完成你的代码并且验证了要达到的功能后，你可以使用下面的命令来优化格式
```
python main.py -S beautify
```
当你要往仓库上传代码时，为了让你的CI能通过你的代码，你可以使用下面的命令查看代码中的格式错误，以确保你的代码符合规范。符合规范的情况为此命令结束后没有返回信息。
```python
python main.py -S test
```
![](./捕获.PNG)

## 其它

<details>
<summary><mark><font color=darkred>如何参与本项目</font></mark></summary>

## 问题的开端
- 直接在本仓库创建暂时分支，通过pull request 来合并代码
- fork 本项目，通过pull request来合并代码
- 提issue，由仓库管理员来改进
### 创建分支
如果你是仓库管理员，拥有直接读写仓库的权限，那么当你有一个改进时，请在[issue](https://github.com/ptrtonull-workshop/PianYuan/issues)提供一个详细的记录，你可以标记这是一个`bug`或者`feature`，并写下具体的描述。
#### 克隆或更新仓库代码
执行
```git
git clone https://github.com/ptrtonull-workshop/PianYuan.git
cd ./pianyuan
```
来克隆本仓库的`dev`分支代码，通常情况下，这个分支的代码是最新的，当然，如果你以前已经克隆过了，那就请您更新一次您的代码，使您的代码保持最新。

如果您第一次下载代码，则意味着您很可能没有本项目需要的相关包，请执行
```
python main.py -S init
```
来初始化项目来获得本项目需要的包
#### 新建bug分支
在GitHub [issue](https://github.com/ptrtonull-workshop/PianYuan/issues)上提交一个`issue`, 记录下bug的情况，记下`issue`的号码，例如您新建了一个编号为#1的`issue`:
使用
```git
git branch bug#1
git checkout bug#1
```
从`dev`分支创立并切换到一个bug分支来修复这个bug，#后的号码为`issue`的号码，在这个分支中进行bug的修复。
#### 检查代码
在本地文件夹中执行
```python
python main.py -G 1 1 hostname username password
```
后，程序会自动写入数据到数据库，来测试你的代码的功能是否正常

其中
- hostname:数据库地址
- username:用户名
- password:用户名密码，为空的时候可以不填

在本地项目文件夹中执行
```pip
python main.py -S beautify
python main.py -S test
```
来规范你的python代码，以符合flake8的规范。再使用flake8确认`main.py`中的语法错误和书写规范，如有不符合`flake`规范，提交的代码将无法通过`CI`的检查
在这条语句中，`E501`的意思是：你最多只能在一行中写79个字符，这个规定过于苛刻，故我们将它删除了
```
E501: E501 line too long (81 > 79 characters)
```
#### 提交
修复完毕后，commit此次修改
完毕后，执行
```git
git push origin bug#1
```
来推送该分支到Github。切换到Github，我们再将`bug#1` 通过`pull request`与`dev`分支合并，在这个过程中，我们的CI会检查代码。

等待合并完成之后，我们在本地执行
```git
git push origin :bug#1
```
来远程删除在Github上的多余的分支
## Q&A
> 哪些操作需要直接在Github上提交？
- README文档需要更新
- CI配置文件需要更新
>哪些情况需要直接同步到`master`分支？
- 有重大更新，可能是一天积累的；
- 涉及到CI的配置文件的；
- 紧急的BUG
</details>
