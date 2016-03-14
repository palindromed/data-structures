# -*- coding: utf-8 -*-

from setuptools import setup


setup(
    name="data-structures",
    description="Implementation of classic data structures using Python classes",
    version=0.1,
    author="Hannah Krager, Wenjing Qiang, and Michael Stokley",
    author_email="",
    license='MIT',
    py_modules={
        "deque",
        "double_linked_list",
        "linked_list",
        "queue",
        "stack",
    },
    package_dir={'': 'src'},
    install_requires=[],
    extras_require={
        'test': ['pytest', 'tox']
    }
)
