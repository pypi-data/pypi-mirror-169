import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="opencv-tools",
    version="0.2",
    author="Wojciech Jasiński",
    description="Simple tools to help with opencv experimenting.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages('src'),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License"
    ],
    python_requires='>=3.6',
    url='https://github.com/wojtke/opencv-tools',
    py_modules=["opencvtools"],
    package_dir={'': 'src'},
    install_requires=[
        "opencv-python"
    ]
)
