import setuptools
from pianyuan.package import *


with open("README.md", "r", encoding="UTF-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pianyuan",
    version="1.4.0",
    author="WangTingZheng",
    author_email="wangtingzheng@outlook.com",
    description="a spider from pianyuan.la",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ptrtonull-workshop/pianyuan",
    packages=setuptools.find_packages(),
    install_requires=[
        "bs4>=0.0.1",
        "beautifulsoup4>=4.8.0",
        "requests>=2.21.0",
        "flake8>=3.7.8",
        "mysqlclient>=1.4.4",
        "black>=19.3b0",
        "twine>=2.0.0",
        "requests>=2.21.0",
        "pick",
    ],
    entry_points={"console_scripts": ["pianyuan = pianyuan.main:main"]},
)
