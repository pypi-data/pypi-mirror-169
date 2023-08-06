import os
import setuptools

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setuptools.setup(
    name="fin_crawler",
    version="0.0.1",
    author="Tom Huang",
    author_email="cwhuang119@gmail.com",
    description="Financial Data Crawler",
    long_description=read('README.md'),
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
    ],
    install_requires=['requests'],
    python_requires='>=3.9',
)
