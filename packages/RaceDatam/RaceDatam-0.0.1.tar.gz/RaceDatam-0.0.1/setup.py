from setuptools import setup, find_packages


VERSION = '0.0.1'
DESCRIPTION = 'Britain all Race data'
LONG_DESCRIPTION = 'You can scrape all britain race in excel and csv'

# Setting up
setup(
    name="RaceDatam",
    version=VERSION,
    author="Ahmety21",
    author_email="<ahmetyildirir1@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION ,
    packages=find_packages(),
    install_requires=['bs4', 'pandas', 'requests','datetime'],
    keywords=['python', 'race','data','scraping'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)