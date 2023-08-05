import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="eisenradio_apk",  # project name /folder
    version="2.0",
    author="René Horn",
    author_email="rene_horn@gmx.net",
    description="Eisenradio apk installer for Android mobiles",
    long_description=long_description,
    license='MIT',
    long_description_content_type="text/markdown",
    url="",
    include_package_data=True,
    packages=setuptools.find_packages(),
        install_requires=[
        ''
    ],
    classifiers=[
    # How mature is this project? Common values are
    # https://packaging.python.org/guides/distributing-packages-using-setuptools/
    #   3 - Alpha
    #   4 - Beta
    #   5 - Production/Stable
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable",
        "Topic :: Multimedia :: Sound/Audio :: Capture/Recording",
    ],
    python_requires='>=3.6',
)
