#!/bin/zsh

find . -name "*.pyc" | xargs rm -rf
ENV=test python -m unittest discover . "*test.py"

# pyhton 的 unittest的discover命令只会去python的package里搜索，
# 不是package不会被检索（即目录下有__init__.py文件的文件夹）