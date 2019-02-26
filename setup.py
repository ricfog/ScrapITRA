from distutils.core import setup

setup(
    name='ScrapITRA',
    version='0.1.0',
    author='Riccardo Fogliato',
    author_email='rfogliat@andrew.cmu.edu',
    packages=['scrapITRA'],
    scripts=['bin/write_races.py'],
    url='https://github.com/ricfog/ScrapITRA',
    description='Scraping website of ITRA',
    install_requires=[
        "beautifulsoup4",
        "selenium",
    ],
)
