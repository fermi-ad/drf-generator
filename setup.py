import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="drf-generator",
    version="1.1.0",
    author="Beau Harrison",
    author_email="beau@fnal.gov",
    description="Generates Data Request Format strings",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fermi-controls/drf-generator",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[],
    python_requires='>=3.6',
)
