# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='generate_report',
    version='1.0.0',
    description='自动生成测试报告工具',
    long_description=open('README.md', encoding='UTF-8').read(),
    author='FuXiaoXiao',
    author_email='fuxiaoxiao@pystandard.com',
    url='http://gitlab.py.in:280/fuxiaoxiao/report_origin',
    packages=find_packages(),
    include_package_data=True,   # 若包含非py文件，一定要加上这行代码
)

