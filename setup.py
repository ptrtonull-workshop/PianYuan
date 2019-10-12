import setuptools
from pianyuan  import *
with open("README.md", "r",encoding='UTF-8') as fh:
    long_description = fh.read()


setuptools.setup(
    name= "pianyuan",
    version = version,
    author = "WangTingZheng",
    author_email="wangtingzheng@outlook.com",
    description="a spider from pianyuan.la",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url ="https://github.com/ptrtonull-workshop/pianyuan",
    packages=setuptools.find_packages(),
)