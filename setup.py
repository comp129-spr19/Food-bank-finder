from setuptools import setup

REQUIRED_PACKAGES = [
    'django==2.1.7',
    'pycodestyle==2.5.0',
    'pre-commit==1.14.4',
    'setuptools==27.2.0',
    'selenium'
]

if __name__ == "__main__":
    setup(
       name='donatefood',
       version='1.0',
       description='A webpage dedicated to providing information about food '
       + 'donation centers',
       author='Mark Fraser',
       author_email='m_fraser3@u.pacific.edu',
       packages=['donatefood'],
       install_requires=REQUIRED_PACKAGES,
    )
