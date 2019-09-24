# 开发
[![Build Status](https://travis-ci.com/ptrtonull-workshop/PianYuan.svg?branch=master)](https://travis-ci.com/ptrtonull-workshop/PianYuan)

[English](./README-EN.md)
## 准备 
执行
```git
git clone https://github.com/ptrtonull-workshop/PianYuan.git
cd ./PianYuan
pip install -r requirements.txt
```
来克隆本项目并且按照本项目需要的第三方包

注意，请确保`./vscode/settings.json`里的路径与你电脑内的`python`路径一致,本项目采用的是`python 3.7.3`
### 额外的插件
本次使用的是`mysqlclient`,一种`MySQL-Python`的一个分支，提供了python3的支持，`mysqlclient`已经加入到`requirements.txt`里，但好像有人说会出错，可以试试[Mysqlclient](https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysqlclient)，下载对应的包后在包所在的地址使用：
```python
pip install 下载的包名
```
来安装此包
### 数据库
#### 安装数据库
这个就不再赘述，按照网上的教程按照，我安装的是`mysql-8.0.17`
#### 数据库配置
按照网上的教程配置mysql数据库，主要是要自定义一个账号
#### 开启数据库
执行
```sql
net start mysql
```
来开启数据库服务
执行
```sql
mysql -u username -p
```
来登录数据库

`username`是你的用户名，一般是`root`，如果你没自定义的话

接下来系统会让你输入密码

使用
```sql
   CREATE DATABASE pianyuan; 
    USE pianyuan;
    create table film(quality char(50),
    moive_name mediumblob, 
    url mediumblob,
    size char(50),
    flash_time char(50)
   )ENGINE=MyISAM DEFAULT CHARSET=utf8;'
```
来创建一个数据，在数据库`pianyuan`，并创立一个表`film`
正常情况下，当你做好这些准备工作后，需要将：
```python
db = MySQLdb.connect("localhost", "root", "wtz", "pianyuan", charset='utf8' )
```
中的第二项和第三项改为你的账号和密码
执行
```python
python main.py
```
后，程序会自动写入数据到数据库

使用
```sql
select *from film
```
来查看数据库中的结果，当然你得确保你选择了`pianyuan`这个数据库
## 测试
在本地文件夹中执行
```
python main.py  1 2
```
来测试你的代码的功能是否正常

在本地项目文件夹中执行
```pip
flake8  --ignore E501  main.py
```
来使用flake8测试`main.py`中的语法错误和书写规范，如有不符合`flake`规范，提交的代码将无法通过`CI`的检查
### 忽略项
```
E501: E501 line too long (81 > 79 characters)
```
## 提交
本项目有四个分支：
- master：主分支：最稳定的分支，代码最成熟
- dev：开发分支，处于开发状态的分支，是两个开发者代码的混合
- bug#nubmer：修复bug临时分支，number为issue号
- feature#number：添加新功能临时分支，number为issue号

### 修改
以修复一个bug为例
在GitHub上提交一个`issue`, 记录下bug的情况，记下`issue`的号码

使用
```git
git branch bug#1
git checkout bug#1
```
创立并切换到一个bug分支来修复这个bug，#后的号码为`issue`的号码
在这个分支中进行bug的修复

修复完毕后，commit此次修改

完毕后，执行
```git
git push origin bug#1
```
来推送该分支到Github

切换到Github，我们再将`bug#1` 通过`pull request`与`dev`分支合并，在这个过程中，我们的CI会检查代码。

合并完成之后，我们在本地执行
```git
git push origin :bug#1
```
来远程删除在Github上的多余的分支










