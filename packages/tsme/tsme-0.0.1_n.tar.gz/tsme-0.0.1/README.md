# TSME

A project for estimating differential equations from time series data. 

## To build
Make sure relevant packages are uptodate 
```shell
pip install --upgrade setuptools wheel
``` 

Generate distribution files: 
```shell
python setup.py sdist bdist_wheel
``` 

Local install: 
```shell
pip install -e .
``` 

## To publish
Make sure releveant package is installed and uptodate 
```shell
pip install --upgrade twine
``` 

upload to test repo: 
```shell
python -m twine upload --repository testpypi dist/*
``` 


upload to official repo: 
```shell
python -m twine upload dist/*
``` 


