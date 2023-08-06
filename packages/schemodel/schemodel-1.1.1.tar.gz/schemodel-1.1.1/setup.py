# -*- coding:utf-8 -*-
# @Author cc
# @TIME 2019/5/25 23:26

from setuptools import setup, find_packages

setup(
    name='schemodel',
    version='1.1.1',
    description=(
        'scheme validate and save to database(support mysql , mongodb)'
    ),
    keywords=("scheme validate, database, mongodb, mysql"),
    author='abo123456789',
    author_email='abcdef123456chen@sohu.com',
    maintainer='abo123456789',
    maintainer_email='abcdef123456chen@sohu.com',
    license='MIT License',
    install_requires=[
        'curd>=0.0.11',
        'pymongo>=3.5.1',
        'schemv>=2.1.1.1'
    ],
    packages=find_packages(),
    platforms=["all"],
    entry_points={
        'console_scripts': ['mcc=mysql_conn_check.mcc:mysql_connection'],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Software Development :: Libraries'
    ])
