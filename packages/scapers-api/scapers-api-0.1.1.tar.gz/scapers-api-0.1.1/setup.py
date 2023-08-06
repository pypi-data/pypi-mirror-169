import sys

import setuptools

__version__ = "0.1.1"

setuptools.setup(
    name="scapers-api",
    version=__version__,
    author="Jarod Daming",
    author_email="jmdaming@gmail.com",
    description="Allows http access to Runescape API Endpoints",
    url="https://gitlab.com/maximized/scapers_api",
    project_url={"Bug Tracker": "https://gitlab.com/maximized/scapers_api/-/issues"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.9",
)

try:
    from semantic_release import setup_hook

    setup_hook(sys.argv)
except ImportError:
    pass
