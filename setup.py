"""
setup.py for pyDGW - A Python module for Directed Graph Walking

This teaching library implements a basic state machine architecture
using directed graphs. It provides an easy-to-understand framework
for learning about finite state machines and graph traversal.
"""

from setuptools import setup, find_packages

# Read the README file for the long description
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="pyDGW",
    version="1.0.0",
    author="Brig Young",
    author_email="brig@sonophotostudios.com",
    description="A Python module for defining and walking Directed State Graphs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Sonophoto/pyDGW",
    project_urls={
        "Bug Tracker": "https://github.com/Sonophoto/pyDGW/issues",
        "Documentation": "https://github.com/Sonophoto/pyDGW/blob/master/README.md",
        "Source Code": "https://github.com/Sonophoto/pyDGW",
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Education",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Education",
        "Topic :: Scientific/Engineering",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3 :: Only",
        "Operating System :: OS Independent",
    ],
    py_modules=["pyDGW"],
    python_requires=">=3.8",
    keywords="state-machine finite-state-machine directed-graph graph-walking fsm teaching-library education",
    license="BSD-2-Clause",
    platforms=["any"],
)
