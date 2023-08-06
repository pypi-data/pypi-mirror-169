import os
from setuptools import setup, find_packages

this_dir = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_dir, "README.md"), "r") as file:
    readme = file.read()

setup(
    name="toolrunner",
    version="1.0.0",
    author="LLCZ00",
    description="Quick tool automation",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/LLCZ00/Toolrunner",
    license="Apache 2.0",
    keywords="malware analysis automation",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Topic :: Utilities",
    ],
    python_requires=">=3.9",
    zip_safe=False,
    install_requires=[],
    packages=find_packages()
)