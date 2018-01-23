from setuptools import setup, find_packages

setup(
    name='dataArchiveReport',
    version='0.5.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='Returns information about NetCDF files in a data archive.',
    url='https://github.com/scrim-network/dataArchiveReport',
    install_requires=['netCDF4', 'numpy'],
    author='Randy Miller',
    author_email='rsm5139@psu.edu'
)
