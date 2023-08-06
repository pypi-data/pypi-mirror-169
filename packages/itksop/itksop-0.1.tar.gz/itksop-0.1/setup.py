# -*- encoding: utf-8 -*-
'''
Description:  PyPI     
@created   : 2022/09/28 20:25
'''

from setuptools import setup, find_packages

setup(
    name="itksop",
    version="0.1",
    author="Xin Shi",
    author_email="Xin.Shi@outlook.com",
    description="ATLAS ITk SOP",
    packages=find_packages(),
    license='MIT',
    classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
    ]
	)
