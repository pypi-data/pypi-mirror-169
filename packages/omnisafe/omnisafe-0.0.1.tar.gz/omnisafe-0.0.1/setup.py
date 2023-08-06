from distutils.core import setup
from setuptools import find_packages

# with open("README.rst", "r") as f:
#   long_description = f.read()

setup(name='omnisafe',
      version='0.0.1',
      description='A small example package',
      long_description="placeholder",
      author='Jiaming Ji',
      author_email='jiamg.ji@gmail.com',
    #   url='www.xxxxx.com',
      install_requires=[],
      license='Apache License',
      packages=find_packages(),
      platforms=["all"],
      classifiers=[
          'Intended Audience :: Developers',
          'Operating System :: OS Independent',
          'Natural Language :: English',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Topic :: Software Development :: Libraries'
      ],
      )