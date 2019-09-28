# Exploit

## Crawling
You can use those command to get the movies which from [there](http://pianyuan.la/mv?order=score) in the database 
```python
python main.py -G start end host username password
```
Details：
- `-G`：represents `get`，to get information
- start:The start page of crawling，such as the url is [此处](http://pianyuan.la/mv?order=score&p=3)when start equals to 3.
- end:The end page of crawling，such as the url is [此处](http://pianyuan.la/mv?order=score&p=3)
when start equals to 3.
- host：database's address
- username：database's username
- password：datebase's password

if your database have not password-meaning password is empty-Then you can execute the following command to realize the same function
```python   
python main.py -G start end host username
```
Otherwise, you can use the following code to check the database's the amount of data.
```
python main.py -M number localhost root root
```
> If course, if you want to see more details,please login in the database directly.当
## Development
When you develop, we prepare the assist script to help you. The format is:
```python
python main.py -S action
```
details:
- `-S`：represents `shell` . To sign the code is a assist script.
- action：repressent the action which is ready to execute. Up to now the support actions are:
  - init
  - beautify
  - test

When you get the code, The first things is setting the initation. You can use:
```python
python main.py -S init
```
When you finish your code and 
当你完成你的代码并且验证了要达到的功能后，你可以使用下面的命令来优化格式
```
python main.py -S beautify
```
When you want to update your code to the repository, you can use the following order to check the format error in your code to insure the code is compliance with requirements for access the CI's check.

```python
python main.py -S test
```
## Other
<details>
<summary><mark><font color=darkred>How to work with us </font></mark></summary>

## 问题的开端
你有以下几种方式参与本项目：
- 直接在本仓库创建暂时分支，通过pull request 来合并代码
- fork 本项目，通过pull request来合并代码
- 提issue，由仓库管理员来改进
### 创建分支
如果你是仓库管理员，拥有直接读写仓库的权限，那么当你有一个改进时，请在[issue](https://github.com/ptrtonull-workshop/PianYuan/issues)提供一个详细的记录，你可以标记这是一个`bug`或者`feature`，并写下具体的描述。
接下来，我将为您示范在此情况下如何修正一个bug：
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


    


