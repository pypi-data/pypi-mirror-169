#!/usr/bin/env python
# coding=utf-8

from setuptools import setup, find_packages

setup(
    name='YolikLogging',
    version='0.0.2',
    description=(
        '自定义logging'
    ),

    author='yolik',
    author_email='252769838@qq.com',
    maintainer='yolik',
    maintainer_email='252769838@qq.com',
    license='BSD License',
    packages=find_packages(),
    platforms=["all"],
    url='http://www.baidu.com',
    install_requires=[
        'colorama',
    ],
)
