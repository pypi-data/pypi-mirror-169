import setuptools

from pathlib import Path

PACKAGE_NAME = "package_b"
DESCRIPTION = ""
URL = ""
AUTHOR = "Jaime"
AUTHOR_EMAIL = "jmartinpe@sia.es"
LICENSE = "UNLICENSED"
REQUIREMENTS = [
    "icdep_package_a"
]

setuptools.setup(
    name=PACKAGE_NAME,
    version="0.0.1",
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    license=LICENSE,
    url=URL,
    packages=setuptools.find_namespace_packages(exclude=["build", "build.*"]),
    include_package_data=True,
    install_requires=REQUIREMENTS,
    classifiers=["Programming Language :: Python :: 3"],
)