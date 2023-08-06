# Copyright 2020 Zurich Instruments AG
# SPDX-License-Identifier: Apache-2.0

import inspect
import os
import sys

import setuptools

requirements = [
    "setuptools>=40.1.0",
    "laboneq",
]


if not hasattr(setuptools, "find_namespace_packages") or not inspect.ismethod(
    setuptools.find_namespace_packages
):
    print(
        "Your setuptools version:'{}' does not support PEP 420 "
        "(find_namespace_packages). Upgrade it to version >='40.1.0' and "
        "repeat install.".format(setuptools.__version__)
    )
    sys.exit(1)


version_path = os.path.abspath(
    os.path.join(
        os.path.join(os.path.join(os.path.dirname(__file__), "laboneq"), "rack"),
        "VERSION.txt",
    )
)
# ~ with open(version_path, "r") as fd:
    # ~ version = fd.read().rstrip()
version = 1

setuptools.setup(
    name="laboneq_rack",
    version=version,
    description="Zurich Instrument tools for quantum information science",
    url="https://gitlab.com/zhinst/qccs",
    author="Zurich Instruments Development Team",
    author_email="info@zhinst.com",
    license="Apache 2.0",
    classifiers=[
        "Environment :: Console",
        "License :: OSI Approved :: Apache Software License",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Scientific/Engineering",
    ],
    keywords="zhinst sdk quantum",
    packages=setuptools.find_namespace_packages(exclude=["test*"]),
    install_requires=requirements,
    include_package_data=True,
    package_data={"laboneq.rack": ["countzero.yml", "countzero_gen2.yml", "neuromancer.yml", "wintermute.yml", "neuromancer_shfqa.yml", "wintermute_shfqa.yml", "seacucumber_gen1.yml", "seacucumber_gen2.yml"]},
    python_requires=">=3.7",
    zip_safe=False,
)
