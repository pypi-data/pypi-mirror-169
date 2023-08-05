
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="citybrain",
    version="0.0.3",
    author="citybrain.org",
    author_email="allenlikeu@gmail.com",
    description="make it easy to use data network of citybrain.org",
    long_description=long_description,
    long_description_content_type = "text/markdown",
    url="",
    packages=setuptools.find_packages(),
    install_requires=[
        'certifi==2022.9.14',
        'charset-normalizer==2.1.1',
        'idna==3.4',
        'pandas==1.5.0',
        'requests==2.28.1',
        'urllib3==1.26.12'],    
    classifiers=(
        'Development Status :: 4 - Beta', # 3 - Alpha 4 - Beta 5 - Production/Stable
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)