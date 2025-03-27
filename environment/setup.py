'''
author: Karan Chauhan
github: @Karan-Chauhan19
organization: L.J University
'''

from setuptools import  setup, find_packages

setup(
    name='Project',  # project name
    version='1.0',  # version number
    description='A Synthetic Weather Classification Project',  # description of the project
    packages = find_packages(),  # find all packages
    author='Karan-Chauhan' ,# author of the package
    author_email='kc879022@gmail.com', # email of the author
    url='https://github.com/karan190806/Project.git', # url of the project
    install_requires=['pandas', 'numpy', 'sklearn', 'matplotlib'],
    # list of the dependencies required by the package
    classifiers=['Programining Language :: python :: 3.12.3']
)