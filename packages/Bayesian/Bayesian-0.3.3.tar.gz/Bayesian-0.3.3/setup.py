from distutils.core import setup

setup(
    name='Bayesian',
    version=open('CHANGES.txt').read().split()[0],
    author='BoppreH',
    author_email='boppreh@gmail.com',
    packages=['bayesian'],
    url='http://pypi.python.org/pypi/bayesian/',
    license='LICENSE.txt',
    description='Library and utility module for Bayesian reasoning',
    long_description=open('README.rst').read(),
)
