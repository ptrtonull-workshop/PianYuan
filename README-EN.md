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
You can use the following command to adjust// your format.
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

## How to join us 
You have the following ways to join us：
- Create a temperate branch directly，and pull request the code.
- fork this project and pull request to the code.
- add a issue to help us to be better.
### Create a branch
If you are the administrator of the repository, if you have an update, please push your update's introduction in [issue](https://github.com/ptrtonull-workshop/PianYuan/issues), and you can sign that this is a `bug` or `feature`.
#### Clone or update repository's code
execute
```git
git clone https://github.com/ptrtonull-workshop/PianYuan.git
cd ./pianyuan
```
To clone `dev` branch. Usually the branch's code is newest. And if you have clone it before, please update again to make sure that the code is the newest.

If it's the first time that you download the code which means you don't have any package properly. Please execute
```
python main.py -S init
```
to init the project to get the package which you need.
#### New a bug branch
You need to push a `issue` on the Github [issue](https://github.com/ptrtonull-workshop/PianYuan/issues) and record the bug information and the bug's number.(such as #1)
Use
```git
git branch bug#1
git checkout bug#1
```
To create a bug branch to fix it from `dev` branch. The number after the # is the `issue` number, and fix the bug in this branch.
#### Check code
Execute in the local folder
```python
python main.py -G 1 1 hostname username password
```
after that, the progam will write the data in the database automaticlly to test whether your code is normal.

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


    


