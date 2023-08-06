from setuptools import setup, find_packages
import os

with open("README.md", "r") as fh:
    long_description = fh.read()
setup(
    name='webvibe',
    packages=find_packages(),
    include_package_data=True,
    version="0.0.1",
    description='Python web-tool !',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='ITSN0B1T4',
    author_email='itsn0b1t4@gmail.com',
    install_requires=['requests', 'lolcat', 'urllib2'],
  
    keywords=["webvibe", "ITSN0B1T4","TOXIC-VIRUS","DEV'S COMMUNITY","hoichoi cracker","zee5 cracker","termux - command","termux","android hacking","mao tool","ALTBALAJI cracker","python cracker","pip cracker","crack account with python", "xenobium", "xenobium cracker pip", "cracking tool", "Mohammad Alamin", "web tools", "ip", "admin finder", "reverse ip", "shared ip", "whios lookup", "geo ip" ," url extractor", "http headers", "site information"],
    classifiers=[
            'Development Status :: 4 - Beta',
            'Intended Audience :: Developers',
            'Topic :: Software Development :: Libraries :: Python Modules',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python :: 2',
            'Operating System :: OS Independent',
            'Environment :: Console',
    ],
    
    license='MIT',
    python_requires='>=2.7'
)