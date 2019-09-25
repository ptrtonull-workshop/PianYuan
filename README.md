[![Build Status](https://travis-ci.com/ptrtonull-workshop/PianYuan.svg?branch=master)](https://travis-ci.com/ptrtonull-workshop/PianYuan)

[English](./README-EN.md)

## 导言
<details>
<summary><mark><font color=darkred>如何使用本项目</font></mark></summary>

## 环境准备
- MySql ：8.0.17
- Python3：3.7.4
- pip：lastest
- vscode：lastest
- vscode的python插件：lastest

后面的是推荐版本，符合要求的其它版本也可，只不过没有进行测试

## 初始化
打开vscode，新建一个终端，执行
```git
git clone https://github.com/ptrtonull-workshop/PianYuan.git
cd ./PianYuan
pip install -r requirements.txt
```
来克隆本项目并且按照本项目需要的第三方包

注意，请确保`./vscode/settings.json`里的路径与你电脑内的`python`路径一致,本项目采用的是`python 3.7.4`

## 测试
执行
```python
python main.py first last -G hostname username password
```
后，程序会自动写入数据到数据库，其中
- first：爬取[电影大全](http://pianyuan.la/mv?order=score)的开始页
- last：爬取[电影大全](http://pianyuan.la/mv?order=score)的终止页
- hostname:数据库地址
- username:用户名
- password:用户名密码，为空的时候可以不填

登录数据库后使用
```sql
use pianyuan;
select *from film
```
可查看爬虫爬到的[此处](http://pianyuan.la/mv?order=score)的一部分电影

</details>

<details>
<summary><mark><font color=darkred>如何贡献本项目</font></mark></summary>

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
python main.py 1 1 -G hostname username password
```
后，程序会自动写入数据到数据库，来测试你的代码的功能是否正常

其中
- hostname:数据库地址
- username:用户名
- password:用户名密码，为空的时候可以不填

在本地项目文件夹中执行
```pip
black main.py
flake8  --ignore E501  main.py
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
</details>
