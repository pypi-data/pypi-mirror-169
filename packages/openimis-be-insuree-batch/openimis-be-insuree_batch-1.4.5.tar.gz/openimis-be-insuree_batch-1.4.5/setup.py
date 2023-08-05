import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), "README.md")) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name="openimis-be-insuree_batch",
    version="1.4.5",
    packages=find_packages(),
    include_package_data=True,
    license="GNU AGPL v3",
    description="The openIMIS Backend Insuree Batch reference module.",
    # long_description=README,
    url="https://openimis.org/",
    author="Eric Darchis",
    author_email="edarchis@bluesquarehub.com",
    install_requires=[
        "django",
        "django-db-signals",
        "djangorestframework",
        "openimis-be-location",
        "openimis-be-insuree",
        "qrcode",
    ],
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 3.1",
        "Framework :: Django :: 3.2",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
