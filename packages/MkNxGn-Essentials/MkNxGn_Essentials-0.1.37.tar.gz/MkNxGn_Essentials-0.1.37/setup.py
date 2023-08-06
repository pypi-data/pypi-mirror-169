import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="MkNxGn_Essentials",
    version="0.1.37",
    author="Mark Cartagena",
    author_email="mark@mknxgn.com",
    description="MkNxGn File Writing, Network Essentials and More - A lot more",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://mknxgn.com/",
    install_requires=['netifaces>=0.10.9', 'six==1.15.0', 'requests>=2.25.1'],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
