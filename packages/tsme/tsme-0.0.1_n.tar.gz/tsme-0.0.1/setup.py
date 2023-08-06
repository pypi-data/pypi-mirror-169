from setuptools import setup, find_packages


long_description = "The ``tsme`` package provides estimation methods for ODE or PDE systems using timeseries data. It also includes basic time simulation capabilities by wrapping scipy's initial value problem solver, either using finite differences or pseudo-spectral methods for spatial derivatives."

setup(
    name='tsme',
    version='0.0.1',
    url='https://zivgitlab.uni-muenster.de/nonlinear-physics/ag-kamps/tsme',
    license='GPL',
    author='Oliver Mai',
    author_email='oliver.mai@wwu.de',
    install_requires=['numpy', 'matplotlib', 'scipy', 'findiff', 'tabulate', 'tqdm', 'hyperopt', 'optuna', 'nevergrad'],
    scripts=[],
    packages=find_packages(),
    description='A package that provides estimation methods for differential equations of dynamical systems based on timeseries data.',
    long_description=long_description,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
        'Development Status :: 3 - Alpha',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Topic :: Scientific/Engineering :: Physics'
        ])
