from setuptools import setup

setup(
    name="vyos-http-api-tools",
    version="0.1.0",
    author="VyOS maintainers and contributors",
    author_email="maintainers@vyos.net",
    python_requires=">=3.7",
    license="BSD",
    url="http://www.vyos.io",
    packages=["vyos-http-api-tools"],
    description=("A debian wrapper of packages to support the VyOS http api."),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License", 
        "Topic :: Internet :: WWW/HTTP",
    ],
)
