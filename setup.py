from setuptools import setup, find_packages

setup(
    name='dataArchiveReport',
    version='0.1.0',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='Returns information about NetCDF files in a data archive.',
    url='https://github.com/scrim-network/dataArchiveReport',
    install_requires=['netCDF4'],
    author='Randy Miller',
    author_email='rsm5139@psu.edu'
)
