# -*- encoding: utf-8 -*-
'''
@Time    :   2021/03/07
@Author  :   mafei 
'''
import setuptools


version = '1.0.0'

with open('requirements') as f:
    requires = f.read().splitlines()

setuptools.setup(
    name="wyltools",
    version=version,
    description='常用方法工具箱',
    long_description=open('README.md').read(),
    author='yanlei.wang',
    author_email="wangyalei310@163.com",
    url='http://www.tophant.com',
    packages=setuptools.find_packages(),
    install_requires=requires,
)

