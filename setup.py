# -*- coding: utf-8 -*-
"""Setup script."""


from setuptools import setup, find_packages
from os import path


setup(
    name='nbdev_light',  # Required

    version='0.0.1',  # Required

    description='Set of tools that help develop in notebooks',  # Optional

    packages=find_packages(),

    python_requires='>=3.6',

    install_requires=[],  # Optional

    entry_points={  # Optional
        'console_scripts': [
            'nbsync=nbdev_light.nbsync:main',
            'nbclean=nbdev_light.nbclean:main',
        ],
    },
)
