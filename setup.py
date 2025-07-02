from setuptools import setup,find_packages


with open("requirements.txt") as f:
    requirements = f.read().splitlines()


setup(
    name="hybrid-recommendation-model",
    version = "0.1",
    author = "Abhishek Jain",
    packages = find_packages(),
    install_requires = requirements,
)