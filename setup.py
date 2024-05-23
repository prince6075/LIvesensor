from setuptools import find_packages,setup
from typing import List

def get_requiremnets()->list[str]:

    requiremnets_list= list[str] = []

    return requiremnets_list





setup(

    name='Sensor',
    version="0.0.1",
    author="Prince kumar",
    author_email="prince6075@gmail.com",
    packages= find_packages(),
    install_requires = get_requiremnets() #["pymongo"]
) 