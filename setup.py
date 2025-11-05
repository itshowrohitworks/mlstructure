from setuptools import find_packages, setup
from typing import List

# Use an uppercase constant for clarity
HYPHEN_E_DOT = "-e ."

def get_requirements(file_path:str) -> List[str]:
    """
    Reads all requirements from the file path, stripping whitespace,
    and removing the special '-e .' marker.
    """
    requirements = []
    with open(file_path) as f:
        # Read all lines and strip leading/trailing whitespace
        requirements = [line.strip() for line in f.readlines()]
        
        # Explicitly remove the '-e .' entry
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
            
    return requirements

setup(
    name="mlstructure",
    version="0.0.1",
    author='itshowrohitworks',
    author_email='therohitshrivastava@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt'),
)
