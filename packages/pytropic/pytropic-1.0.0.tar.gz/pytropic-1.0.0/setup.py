#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open("README.rst") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read()

requirements = []

setup_requirements = []

test_requirements = ["pytest"]

setup(
    name="pytropic",
    version="1.0.0",
    description="Train and predict string entropy based on character n-grams",
    long_description=readme + "\n\n" + history,
    long_description_content_type="text/x-rst",
    author="Will Fitzgerald",
    author_email="will.fitzgerald@gmail.com",
    url="https://github.com/willf/pytropic",
    packages=find_packages(include=["pytropic"]),
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords="pytropic",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    test_suite="tests",
    tests_require=test_requirements,
    setup_requires=setup_requirements,
)
