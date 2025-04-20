from setuptools import setup, find_packages

with open("requirements.txt") as file:
    requirements = file.read().splitlines()

setup(
    name="MLOPS-PROJECT-5",
    version="0.1",
    author="SandeepanB",
    packages=find_packages(),
    install_requires=requirements
)
