from setuptools import setup, find_packages

setup(
	name='src',
	version="0.0.1",
	description="DVC",
	long_description="DVC_DEMO",
	author="naveen",
	author_email="naveenkrishnan840@gmail.com",
	url="https://github.com/naveenkrishnan840/DVC-ML-DEMO-AIOPS",
	packages=['src'],
	python_requires = ">=3.7",
	install_requires=[
		"dvc", "pandas", "scikit-learn"
	],
)