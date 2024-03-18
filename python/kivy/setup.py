from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='yourapp',
    version='0.1',
    packages=['yourapp'],
    scripts=['yourapp/main.py'],
    install_requires=[
        'kivy',
    ],
    maintainer='Your Name',
    maintainer_email='youremail@example.com',
    description='A simple Kivy application',
    long_description=long_description,
    long_description_content_type="text/markdown",
)
