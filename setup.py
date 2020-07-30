from pathlib import Path
from setuptools import setup

if __name__ != '__main__':
    raise RuntimeError("setup.py should never be imported")

README = Path('./README.md')

setup(
    name="samplepackage",
    version="0.1",
    author="GlebMorgan",
    author_email="glebmorgan@gmail.com",
    description="Sample python package for reference purposes",
    long_description=README.read_text(),
    long_description_content_type="text/markdown",
    url='https://github.com/GlebMorgan/SamplePackage',

    packages=['package'],
    include_package_data=True,

    python_requires='>=3.7.0',
    setup_requires=['tomlkit'],
    extras_require={'test': 'pytest'},

    platforms='Windows',  # values are ;-separated
    classifiers=[
        'Intended Audience :: Education',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development',
    ],
)
