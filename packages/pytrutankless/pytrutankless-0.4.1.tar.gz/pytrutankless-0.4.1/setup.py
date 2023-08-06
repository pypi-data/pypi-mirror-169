import re
from setuptools import setup, find_packages
import pathlib

with open("README.md") as f:
    readme = f.read()

# with open("requirements.txt", encoding="utf-8") as f:
#     install_requires = f.read().splitlines()


with open("pytrutankless/__init__.py", encoding="utf-8") as f:
    version = re.findall(r"__version__ = \"(.+)\"", f.read())[0]

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="pytrutankless",
    version=version,
    description="A Python client library for the TruTankless API",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/colemamd/pytrutankless",
    download_url="https://github.com/CyanBook/pytrutankless/releases/latest",
    author="@colemamd",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    license="MIT",
    install_requires="requirements.txt",
    packages=find_packages(
        exclude=["dist", "*.test", "*.test.*", "test.*", "test"]
    ),
    zip_safe=True,
    project_urls={
        "Source": "https://github.com/colemamd/pytrutankless",
        "Bug Reports": "https://github.com/colemamd/pytrutankless/issues",
        "Release Notes": "https://github.com/colemamd/pytrutankless/releases/)",
    },
)
