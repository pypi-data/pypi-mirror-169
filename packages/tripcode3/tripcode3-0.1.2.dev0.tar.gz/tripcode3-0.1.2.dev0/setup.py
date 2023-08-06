import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="tripcode3",
    version=__import__("tripcode", locals=locals()).__version__,
    description="Yet another tripcode implementation in Python, just works steady",
    keywords=["tripcode", "hash", "imageboard"],
    long_description=open("./README.rst", mode="r", encoding="utf-8").read(),
    long_description_content_type="text/x-rst",
    license="GLWTPL",
    author="JL Connor",
    author_email="AbLaternae@outlook.com",
    url="https://github.com/ablaternae/py-tripcode",
    # download_url="",
    python_requires=">=3",
    py_modules=["tripcode"],
    setup_requires=["wheel"],
    install_requires=["passlib"],
    platforms="any",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: Freeware",
        "License :: OSI Approved :: BSD License",
        "License :: OSI Approved :: Common Public License",
        "Operating System :: POSIX",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Communications :: BBS",
        "Topic :: Communications :: Chat",
        "Topic :: Utilities",
    ],
)
