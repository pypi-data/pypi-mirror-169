#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools
import BaolingxinTaluoDailingniKaiqiZhijuede78tangTaluoke
import os
from os import path

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

for subdir, _, _ in os.walk('BaolingxinTaluoDailingniKaiqiZhijuede78tangTaluoke'):
    fname = path.join(subdir, '__init__.py')
    open(fname, 'a').close()
    
setuptools.setup(
    name="baolingxin-taluo-dailingni-kaiqi-zhijuede-78tang-taluoke",
    version=BaolingxinTaluoDailingniKaiqiZhijuede78tangTaluoke.__version__,
    url="https://github.com/apachecn/baolingxin-taluo-dailingni-kaiqi-zhijuede-78tang-taluoke",
    author=BaolingxinTaluoDailingniKaiqiZhijuede78tangTaluoke.__author__,
    author_email=BaolingxinTaluoDailingniKaiqiZhijuede78tangTaluoke.__email__,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "License :: Other/Proprietary License",
        "Natural Language :: Chinese (Simplified)",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Text Processing :: Markup :: Markdown",
        "Topic :: Text Processing :: Markup :: HTML",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Documentation",
        "Topic :: Documentation",
    ],
    description="宝灵心塔罗：带领你开启直觉的78堂塔罗课",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=[],
    install_requires=[],
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            "baolingxin-taluo-dailingni-kaiqi-zhijuede-78tang-taluoke=BaolingxinTaluoDailingniKaiqiZhijuede78tangTaluoke.__main__:main",
            "BaolingxinTaluoDailingniKaiqiZhijuede78tangTaluoke=BaolingxinTaluoDailingniKaiqiZhijuede78tangTaluoke.__main__:main",
        ],
    },
    packages=setuptools.find_packages(),
    package_data={'': ['*']},
)
