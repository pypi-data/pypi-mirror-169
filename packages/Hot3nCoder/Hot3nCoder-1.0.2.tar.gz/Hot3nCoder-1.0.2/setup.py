import setuptools
from setuptools import setup, find_packages

with open("README.md", 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name='Hot3nCoder',
    version='1.0.2',
    description='Encode your cpp file with whatever you want',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Jas0ff/Hot3nCoder',
    author='Jas0ff',
    author_email='jason20021019@gmail.com',
    packages=setuptools.find_packages(),
    keywords=['cpp', 'encode', 'emoji', 'funny'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ],
    entry_points={
        'console_scripts': [
            'Hot3nCoder = Hot3nCoder.main:main'
        ]
    }


)
