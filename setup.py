import setuptools

with open('README.md', 'r') as fh:
	actual_description= fh.read()


	setuptools.setup(
	    name="lazyloads", 
	    version="0.0.1",
	    author="Matthew Lam",
	    author_email="lcpmatthew@gmail.com",
	    description="Python Module to make your life easier",
	    long_description=actual_description,
	    long_description_content_type="text/markdown",
	    url="https://github.com/feimaomiao/lazyloads",
	    package_dir = {'':'lzl'},
	    packages=setuptools.find_packages("lzl", exclude=['tests']),
	    classifiers=[
	        "Programming Language :: Python :: 3",
	        "License :: OSI Approved :: MIT License",
	        "Operating System :: OS Independent",
	    ],
	    python_requires='>=3.5',
	)