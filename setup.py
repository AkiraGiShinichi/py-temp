from setuptools import setup, find_packages

requirements = ['numpy >= 1.11', 'matplotlib >= 1.5']

setup(
    name='NAME',
    version='1.0.0',
    description='SAMPLE',
    url='https://github.com/akiragishinichi/NAME.git',
    packages=find_packages(),
    install_requires=requirements,
    classifiers=['Programming Language :: Python :: 3.7']
)