import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="LogQS-Client",
    version="0.0.1",
    author="Nathan Margaglio",
    author_email="nmargaglio@carnegierobotics.com",
    description="Log Query System Client",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/carnegierobotics/LogQS-Client",
    project_urls={
        "Bug Tracker": "https://github.com/carnegierobotics/LogQS-Client/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=["lqs-client"],
    python_requires=">=3.9",
)
