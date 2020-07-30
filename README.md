# SamplePackage

Void python package deliberately composed along with [this][1] guide  
Intended to be a future reference for creating a clean structured packages  
Contains Windows-specific scripts

### Installation:
1. clone the repo / download the source distribution
2. `cd` to project directory
2. `pip install .`

### Package features:
- *'src-less'* package layout
- packages are declared statically: `packages=[...]` (without `find_packages()`)
- package version is specified statically: `version=...` (only in `setup.py`)
- `README.md` is automatically copied into `long_description`
- distribution contents are declared by `MANIFEST.in` (not by `package_data` argument)
- deps are declared in `setup_requires` (no `requirements.txt`)
- extra deps for testing are specified with `extras_require`. Usage: `pip install samplepackage[test]`
- `setup.py` is protected against unintended imports (prevents issues with editable installs)
- sample `/tests` directory containing tests to check that:
    - `pytest` is able to import the package
    - `module.py` can access `res/test_res.txt`

### Intentions:
- learn how to create clean and maintainable python package
- provide a reference for creating, installing, maintaining, testing and distributing a package in future
- provide a template for future python packages

### Tests:
1. clone the repo / download the source distribution
2. `cd` to project directory
3. `pip install .[test]`

To run tests, there are 3 options:
1. Test local package: `python -m pytest`
2. Test installed package: `pip install .` and `pytest`
3. Test editable install: `pip install -e .` and `pytest`


[1]: https://www.evernote.com/shard/s721/sh/a0745ef6-fe72-3256-ee10-d7fa81b4cc5b/aac5c8537533a06d067254853b04e30a