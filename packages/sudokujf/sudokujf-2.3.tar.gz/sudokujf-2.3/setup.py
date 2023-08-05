import os
from setuptools import setup, find_packages

setup(
    name="sudokujf",
    version="2.3",
    author="Jean-François BOUCHAUDY",
    author_email="jfbouch@wanadoo.fr",
    description=("Un programme en mode texte pour jouer au SUDOKU"),
    keywords="sudoku tui deduction",
    url="http://linux.home/PyPI/sudokujf",
    packages=find_packages(),
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    include_package_data=True,
    licence="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[] 
)
