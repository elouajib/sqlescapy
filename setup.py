import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sqlescapy",
    version="1.0.1",
    author="Imad ElOuajib",
    author_email="elouajib.im@gmail.com",
    description="Python module to escape SQL special characters and quotes in strings",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/elouajib/sqlescapy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=2.7',
)
