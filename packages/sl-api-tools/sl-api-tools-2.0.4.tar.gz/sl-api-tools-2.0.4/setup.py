#!/usr/bin/env python
# -*- coding: utf-8 -*-

# __title__ = ''
# __author__ = 'xuepl'
# __mtime__ = '2019/9/14'

from distutils.core import setup

setup(
    name="sl-api-tools",  # 这里是pip项目发布的名称 pip install 包名
    version="2.0.4",  # 版本号，数值大的会优先被pip
    keywords=["api", "auto"],
    description="to simplify auto test",
    long_description="A init package,to simplify develope auto test",
    license="MIT Licence",
    url="https://git.code.tencent.com/2207B/auto_api_xuepl.git",  # 项目相关文件地址，一般是github
    author="xuepl",
    author_email="xuepl@songlinxy.com",
    packages=['tools', "common"],  # 发布的包列表 ,from import的包名
    platforms="python3",
    install_requires=[
        'allure-pytest==2.9.45',
        'configparser==5.2.0',
        'Faker==14.2.0',
        'jsonpath==0.82',
        'PyMySQL==1.0.2',
        'pytest==7.0.1',
        'requests==2.27.1',
        'xlrd==2.0.1',
        'xlwt==1.3.0'
    ]
)
