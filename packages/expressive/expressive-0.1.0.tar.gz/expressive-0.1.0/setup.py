#!/usr/bin/env python

from setuptools import setup

install_requires = [
    "sympy >= 1.11",
    "numpy >= 1.23",
    "numba >= 0.56",
    "llvmlite >= 0.39.1",
    # mpmath
    # matplotlib
]

packages = [
    "expressive",
]

setup(
    name="expressive",
    version="0.1.0",
    description="A Python library for converting strings into array functions with some confidence",
    url="https://gitlab.com/expressive-py/expressive",
    maintainer="Russell Fordyce",
    license="BSD 3-Clause License",
    keywords="sympy numpy numba",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: BSD License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Scientific/Engineering",
    ],
    packages=packages,
    long_description_content_type="text/markdown",
    long_description=open("README.md").read(),
    python_requires=">=3.7",
    install_requires=install_requires,
    #include_package_data=True,
    zip_safe=False,  # https://setuptools.pypa.io/en/latest/deprecated/zip_safe.html
)
