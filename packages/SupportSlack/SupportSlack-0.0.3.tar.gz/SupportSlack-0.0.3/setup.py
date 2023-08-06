import setuptools

with open("README.md","r") as fh:
    long_description=fh.read()

setuptools.setup(
    name="SupportSlack",
    version="0.0.3",
    author="swiftlong",
    descrition="slack的小应用",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/swiftlong/support-slack",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",#使用Python3
        "License :: OSI Approved :: Apache Software License",#开源协议
        "Operating System :: OS Independent",
    ],
)
