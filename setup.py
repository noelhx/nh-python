from setuptools import setup, find_packages

setup(
    name="nhpy-tools",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        # Example dependencies
        "requests",
        "arrow"
    ],
    entry_points={
        "console_scripts": [
            "nhpy-tools=nhpy-tools.cli:main",  # CLI command -> function
        ]
    },
    author="Noel Henderson",
    description="My own python library of tools",
    url="https://github.com/noelhx/nh-python",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)
