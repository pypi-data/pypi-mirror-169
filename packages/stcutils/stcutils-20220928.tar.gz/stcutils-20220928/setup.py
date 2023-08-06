import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="stcutils",
    version="20220928",
    author="Paul Baumgarten",
    author_email="pbaumgarten@gmail.com",
    description="Provide useful functionality and auto testing data for my computer science students. Designed for Sha Tin College.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/paulbaumgarten/stc-tester",
    packages=setuptools.find_packages(),
    keywords='Sha Tin College',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['requests'],
    python_requires='>=3'
)
