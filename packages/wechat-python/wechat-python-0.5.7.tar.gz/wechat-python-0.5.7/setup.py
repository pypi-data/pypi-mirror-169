# -*- coding: utf-8 -*-


import ast
import os
import re

from setuptools import find_packages, setup

_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('weixin/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')
    ).group(1)))


def fread(fname):
    filepath = os.path.join(os.path.dirname(__file__), fname)
    if os.path.exists(filepath):
        with open(filepath, encoding='utf8') as f:
            return f.read()


setup(
    name='wechat-python',
    description='Wechat for Python',
    long_description=fread('docs/quickstart.rst'),
    long_description_content_type='text/x-rst',
    license='BSD',
    packages=find_packages(),
    version=version,
    author='zwczou',
    author_email='zwczou@gmail.com',
    url='https://github.com/wpcfan/weixin-python',
    keywords=['weixin', 'weixin pay', 'weixin login', 'weixin mp', 'weixin python',
              'wechat', 'wechat pay', 'wechat login', 'wechat mp', 'wechat python'],
    zip_safe=False,
    platforms='any',
    install_requires=[
        "requests",
        "lxml"
    ],
    classifiers=[],
)
