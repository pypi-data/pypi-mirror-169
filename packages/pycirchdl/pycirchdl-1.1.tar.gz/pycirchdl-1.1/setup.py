from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='pycirchdl',
    version='1.1',
    description='Python logic circuit hardware description language',
    keywords='digital circuit logic hardware description modeling simulation',
    author='Samy Zafrany',
    url='https://www.samyzaf.com/pycirc/pycirchdl.html',
    author_email='sz@samyzaf.com',
    license='MIT',
    packages=['pycirchdl'],
    install_requires=['networkx'],
    zip_safe=False,
)

