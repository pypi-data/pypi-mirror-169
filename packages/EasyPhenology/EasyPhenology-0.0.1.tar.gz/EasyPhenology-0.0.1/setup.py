
from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]

setup(
    name='EasyPhenology',
    version='0.0.1',
    description='Calculates vegetation phenological transition dates',
    long_description = open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
    long_description_content_type='text/markdown',
    url='',
    author='Annu Panwar',
    author_email='apanwar@bgc-jena.mpg.de',
    license='MIT',
    classifiers=classifiers,
    keywords='Phenology',
    packages=find_packages(),
    install_requires=['']
)