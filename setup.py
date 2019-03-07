from setuptools import setup, find_namespace_packages, find_packages

setup(
    name='ScrapITRA',
    version='0.1.0',
    author='Riccardo Fogliato',
    author_email='rfogliat@andrew.cmu.edu',
    packages=find_packages(),
    scripts=['bin/write_races.py'],
    url='https://github.com/ricfog/ScrapITRA',
    description='Scraping website of ITRA',
    install_requires=[
        "beautifulsoup4",
        "selenium",
    ],
)
