from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()


setup(name='sight_machine',
      version='0.1',
      description='Simple binary logger',
      url='http://github.com/dbajet/sight_machine/',
      author='Denis Bajet',
      license='MIT',
      packages=['sight_machine'],
      zip_safe=False)
