"""Packaging."""
from codecs import open
from os.path import abspath, dirname, join
from subprocess import call

from setuptools import Command, find_packages, setup

this_dir = abspath(dirname(__file__))
with open(join(this_dir, "README.md"), encoding="utf-8") as file:
    long_description = file.read()


class RunTests(Command):
    """Run all tests."""

    description = "run tests"
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        """Run all tests!"""
        errno = call(["py.test", "--cov=pyyt", "--cov-report=term-missing"])
        raise SystemExit(errno)


setup(
    name="pyyt-cli",
    version="0.1.3",
    description="Python script to download videos as audio from a given YouTube playlist/video",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/patillacode/pyyt",
    author="Patilla Code",
    author_email="patillacode@gmail.com",
    license="Apache 2.0",
    classifiers=[
        "Intended Audience :: Developers",
        "Topic :: Utilities",
        "License :: Public Domain",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.11",
    ],
    keywords="converter, audio, youtube, download, mp3",
    packages=find_packages(exclude=["docs", "tests*", "downloads", "examples"]),
    install_requires=["pyfiglet", "simple-term-menu", "yt-dlp", "termcolor"],
    extras_require={
        "test": ["coverage", "pytest", "pytest-cov", "mock"],
    },
    entry_points={
        "console_scripts": [
            "pyyt=src.pyyt:main",
        ],
    },
    cmdclass={"test": RunTests},
)
