import re
from setuptools import find_packages, setup

PACKAGE_NAME = 'aimedic_utils'
SOURCE_DIRECTORY = 'src'
SOURCE_PACKAGE_REGEX = re.compile(rf'^{SOURCE_DIRECTORY}')

source_packages = find_packages(include=[SOURCE_DIRECTORY, f'{SOURCE_DIRECTORY}.*'])
proj_packages = [SOURCE_PACKAGE_REGEX.sub(PACKAGE_NAME, name) for name in source_packages]
print(proj_packages)

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="aimedic_utils_package",
    version="0.1.0",
    author="Benyamin Ghahremani Nezhad",
    author_email="benyamin.ghahremani@gmail.com",
    description=('''
        This package offers some evaluation metrics for classification models.\n
        V0.1.0: evaluation method added.
    '''),

    packages=proj_packages,
    package_dir={'aimedic_utils':'src'},
    
    include_package_data=True,

    python_requires=">=3.6",
    install_requires=[
        'scikit-learn',
        'loguru',
        'mlflow',
        'matplotlib',
        'numpy',
        'tensorflow>=2.9',
    ],

)