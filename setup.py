from setuptools import setup

from pyngfm import meta


setup(
    name=meta.display_name,
    version=meta.version,
    description=meta.description,
    author=meta.author,
    author_email=meta.author_email,
    url=meta.url,
    license=meta.license,
    packages=[
        meta.library_name,
        "%s.client" % meta.library_name,
        ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: by End-User Class :: Advanced End Users",
        "Programming Language :: Python",
        ],
    )
