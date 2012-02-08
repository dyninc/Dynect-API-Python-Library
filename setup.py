import os
from distutils.core import setup

# sync with __init__.py
version = '0.1'

setup(
    name="DynectDNS",
    version=version,
    keywords=["dynect", "api", "dns"],
    long_description=open(os.path.join(os.path.dirname(__file__),"README"), "r").read(),
    description="Dynect REST API wrapper",
    author="dyn.com",
    packages=['dynect'],
)
