# Exploit

## Ready 
execute
```git
git clone https://github.com/ptrtonull-workshop/PianYuan.git
cd ./PianYuan
pip install -r requirements.txt
```
to clone this project and install the third-party package

**ATTENTION!**
Make sure `./vscode/settings.json`'s path is same as the`python` in your computer.
This Project use the `python 3.7.3`

## Test
To execute 
```
python main.py
```

```pip
flake8  --ignore E501  main.py
```
in your local folder to test whether your code's funcion is OK.

Use **flake8** to test  `main.py` grammatical mistake and writing norms.
If the code is not conform to the norms,it will not accept the check of the `CI`

### Ignoring item
```
E501: E501 line too long (81 > 79 characters)
```

## Submit
This project have four branches:
- master: the main branch
Most stablized version
- dev: the development branch
The mix of two developer's code
- bug#number:
A branch to help to fix the bug. number is the issue.
- feature#number:
Add a new feature's temporary branch. number is the issue.

### Repair

Here we have an example that how to fix a bug.

Submit an `issue` on GitHub, recode the bug's status and write down the `issue`

Use
```git
git branch bug#1
git checkout bug#1
```
To create and switch to a bug branch to fix this bug.
The # number is the `issue`

If you fix up, commit this action.

Finish and execute
```git
git push origin bug#1
```
To push this branch to Github

And now let's get back to the Github,We will combine `bug#1` with `dev` by `pull request`.
The CI will check the code automaticlly.

After the combanition, we need to execute
```git
git push origin :bug#1
```
on local to remote-deleting the Github's useless branch on Github.
    


