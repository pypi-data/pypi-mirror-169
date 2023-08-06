#!/usr/bin/env python3
# encoding: utf-8
"""
Flask-Telebot
-------------
This is the description for that library
"""
from setuptools import setup

setup(
    name='Flask-Telebot',
    version='1.0.0',
    url='https://github.com/GatLab/Flask-Telebot.git',
    license='BSD',
    author='Gatlab',
    author_email='dev@gatlab.co',
    description='Telebot on flask',
    long_description=__doc__,
    py_modules=['flask_telebot'],
    # if you would be using a package instead use packages instead
    # of py_modules:
    # packages=['flask_telebot'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask',
        'pyngrok',
        'pyTelegramBotAPI',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
