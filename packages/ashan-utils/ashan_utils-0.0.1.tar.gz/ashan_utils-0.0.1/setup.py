from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='ashan_utils',
  version='0.0.1',
  description='A very basic cumulative value calculator',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='Ashan Jaysundara',
  author_email='developer.ashan@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='utils', 
  packages=find_packages(),
  install_requires=[''] 
)