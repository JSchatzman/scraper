"""The setup for scraper."""

from setuptools import setup

setup(
    name='data_structures',
    description='Implementation of Scraper.',
    version=0.1,
    author='Jordan Schatzman',
    author_email='j.schatzman@outlook.com',
    license='MIT',
    # package_dir={''},
    # py_modules=['numpy'],
    extras_require={'test': ['pytest', 'pytest-watch', 'pytest-cov', 'tox'],
                    'additional': ['requests']}
)
