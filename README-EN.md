# Exploit

## Crawling
You can use those command to get the movies which from [there](http://pianyuan.la/mv?order=score) in the database 
```python
python main.py -G start end host username password
```
Details：
- `-G`：represents `get`，to get information
- start:The start page of crawling，such as the url is [here](http://pianyuan.la/mv?order=score&p=3)when start equals to 3.
- end:The end page of crawling，such as the url is [here](http://pianyuan.la/mv?order=score&p=3)
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
> If course, if you want to see more details,please login in the database directly.
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

Details:
- hostname:database address
- username:database username
- password:database password(if it's empty,miss it)

Execute in the local folder
```pip
python main.py -S beautify
python main.py -S test
```
Standarding your python code to accord with the standard the flake8. Please use flake8 to ensure `main.py` grammer error and writing norms.if your code has some problems, `CI` will intercept you to push the code.
`E501` means: You can write 79 characters at one line.This rule is too rigor to do, so we delete it.
```
E501: E501 line too long (81 > 79 characters)
```
#### Push
after fixing the bug, commit your adjusting.
Then execute
```git
git push origin bug#1
```
to push the branch to Github. Switch to Github, we combine `bug#1` and `dev` through `pull request`. CI will check the code automaticlly.
After that,execute
```git
git push origin :bug#1
```
To delete the useless branch on Github.
## Q&A
> Which opration can push on Github directly
- Update the README
- Update the CI configuration.
>Which condition need to sychronize to the `master`directly?
- Significant update
- Come down to CI configuration
- Enmergency Bug
</details>


    


