from pip.req import parse_requirements
from setuptools import setup

setup(
   name='donatefood',
   version='1.0',
   description='A webpage dedicated to providing information about food '
   + 'donation centers',
   author='Mark Fraser',
   author_email='m_fraser3@u.pacific.edu',
   packages=['donatefood'],
   install_requires=parse_requirements('requirements.txt', session='hack'),
)
