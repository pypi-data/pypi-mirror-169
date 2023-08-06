"""setup module."""

from pathlib import Path

from setuptools import find_packages, setup

setup(
    name="cosmian_lib_anonymization",
    description="Python library to anonymize csv datasets",
    version="0.1.2",
    url="https://cosmian.com",
    author="Cosmian Tech",
    author_email="tech@cosmian.com",
    license="MIT",
    packages=find_packages(),
    long_description=Path("README.md").read_text(),
    long_description_content_type="text/markdown",
    install_requires=["cryptography", "numpy", "pandas"],
    keywords=["python", "cosmian", "anonymization"],
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
