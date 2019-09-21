# 开发
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
## 测试
在本地文件夹中执行
```
python main.py
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










