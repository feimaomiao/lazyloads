import setuptools
import re

with open('lzl/__init__.py') as fh:
	_f = fh.read()

version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',_f, re.MULTILINE).group(1)
author 	= re.search(r'^__author__\s*=\s*[\'"]([^\'"]*)[\'"]',_f,re.MULTILINE).group(1)    
email  	= re.search(r'^__email__\s*=\s*[\'"]([^\'"]*)[\'"]',_f,re.MULTILINE).group(1)    

with open('README.md', 'r') as fh:
	actual_description= fh.read()


setuptools.setup(
    name="lazyloads", 
    version=version,
    author=author,
    author_email=email,
    description="Python Module to make your life easier",
    long_description=actual_description,
    long_description_content_type="text/markdown",
    url="https://github.com/feimaomiao/lazyloads",
    packages=setuptools.find_packages(exclude=['tests','docs']),
    test_suite='tests',
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
     	"Topic :: Software Development :: Libraries :: Python Modules"
    ],
    keywords='lazy built in function expansion extension other',
    zip_safe=False,
    python_requires='>=3.6',
)