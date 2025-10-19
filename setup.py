from setuptools import setup, find_packages

setup(
    name = 'mypackage',
    version = '0.4',
    packages = find_packages(exclude = ['tests*']),
    license = 'MIT',
    description = 'EDSA example python package',
    long_description = open('README.md').read(),
    install_requires = ['numpy'],
    url = 'https://github.com/divineanekwe/mypackage',
    author = 'Divine Anekwe',
    author_email = 'divine.anekwe.chukwubuikem@gmail.com'
)