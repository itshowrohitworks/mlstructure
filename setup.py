from setuptools import find_packages,setup
from typing import List

hypen_e_dot = "-e ."

def get_requirements(path:str)->List[str]:
    """
    This function will return the list of requirements.
    """
    requirements = []
    with open(path) as f:
        requirements = f.readline()
        requirements = [req.replace("\n"," ") for req in requirements]
        if hypen_e_dot in requirements:
            requirements.remove(hypen_e_dot)
    return requirements
    pass

setup(
    name="mlstructure",
    version="0.0.1",
    author='itshowrohitworks',
    author_email='therohitshrivastava@gmail.com',
    packages=find_packages(),
    install_requires = ['numpy','pandas'],
)