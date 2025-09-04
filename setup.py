from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)->List[str]:
     '''
       this function will return the list of requirements
     '''
setup(
    name='mlproject',
    version='0.0.1',
    author='Abhijeet',
    email='b222001@iiit-bh.ac.in',
    packages=find_packages(),
    install_requires=get_requirements('requiremnets.txt')


)