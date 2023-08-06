#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

import os
from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=6.0', ]
setup_requirements = ['pytest-runner', ]
test_requirements = ['pytest', ]

def get_version_from_package() -> str:
    path = os.path.join(os.path.dirname(__file__), "sky_wiremock/__init__.py")
    path = os.path.normpath(os.path.abspath(path))
    with open(path) as f:
        for line in f:
            if line.startswith("__version__"):
                token, version = line.split(" = ", 1)
                version = version.replace("'", "").strip()
                return version

setup(
    author="Marco Masetti",
    author_email='marco.masetti@sky.uk',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description="Python HTTP client for wiremock",
    entry_points={
        'console_scripts': [
            'sky_wiremock=sky_wiremock.cli:main',
        ],
    },
    install_requires=requirements,
    license="BSD license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='sky_wiremock',
    name='sky_wiremock',
#     packages=find_packages(include=['sky_wiremock']),
    packages=['sky_wiremock'],
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/grubert65/sky_wiremock',
    version=get_version_from_package(),
    zip_safe=False,
)
