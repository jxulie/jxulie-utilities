# encoding: utf-8

from distutils.core import setup
import setuptools
setup(
    name='jxulie-utilities',
    description='A set of python utilities.',
    version='0.1',
    author='Xu Bo',
    author_email='bolang1988@gmail.com',
    url='http://github.com/jxulie',
    
    packages= setuptools.find_packages(exclude=["tests.*", "tests"]),
)
