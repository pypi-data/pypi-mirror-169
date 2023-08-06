import setuptools

PACKAGE_NAME = "cdep_package_a"
DESCRIPTION = "Package A of cdep"
URL = ""
AUTHOR = "John Doe"
AUTHOR_EMAIL = "jmartinpe@sia.es"
LICENSE = "UNLICENSED"
REQUIREMENTS = []

setuptools.setup(
    name=PACKAGE_NAME,
    version="0.0.2",
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    license=LICENSE,
    url=URL,
    include_package_data=True,
    packages=setuptools.find_packages(),
    install_requires=REQUIREMENTS,
    classifiers=["Programming Language :: Python :: 3"],
)