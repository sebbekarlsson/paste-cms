import os
from setuptools import setup


setup(
    name='Foliumer',
    version='1.0',
    description='Foliumer',
    author='Sebastian Robert Karlsson',
    author_email='ianertson@gmail.com',
    url='http://ianertson.me/',
    install_requires=[
        'flask',
        'pymongo',
        'flask_assets',
        'jsmin'
    ],
    entry_points={
        "console_scripts": [
            "foliumer-develop = develop:run"
        ]
    }
)
