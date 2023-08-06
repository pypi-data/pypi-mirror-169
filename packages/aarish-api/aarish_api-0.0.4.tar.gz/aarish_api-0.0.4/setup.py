from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

VERSION = '0.0.4'
DESCRIPTION = 'Library with function for face recognition'
LONG_DESCRIPTION = 'A package that allows you to use the state of the art pretrained FaceNet model for calculating distance between two faces with just one function call literally !  '

# Setting up
setup(
    name="aarish_api",
    version=VERSION,
    author="Aarish Technologies Inc.",
    author_email="<sayantan@aarishtech.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['requests'],
    keywords=['python', 'Computer Vision', 'Recognition', 'FaceNet'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)