import setuptools
from setuptools import find_packages

setuptools.setup(
    name="altinference",
    version="0.0.1",
    author="Altscore-analytics",
    author_email="kishan.parshotam@altscore.ai",
    description="A library to put altscore models into production",
    url="https://github.com/AltScore/altinference.git",
    packages=find_packages(),
    install_requires=[
        "pandas==1.4.2",
        "dill==0.3.5.1",
        "numpy==1.21.6",
        "xgboost",
        "pdpipe",
    ],
)
