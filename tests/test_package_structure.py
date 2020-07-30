import os
import sys

print()
print(f"  __name__ = {__name__}")
print(f"  __file__ = {__file__}")
print(f"  cwd = {os.getcwd()}")
print(f"  PYTHONPATH = {os.environ.get('PYTHONPATH', None)}")
print(f"  sys.path = {sys.path}")
print(f"  args = {sys.argv}")


def test_package_import():
    try:
        import package
    except ImportError as e:
        print("'import package' - failed")
        print(e)
    else:
        print("'import package' - ok")
        print(f"Package name = {package.__name__}")


def test_pytest_import():
    try:
        import pytest
    except ImportError as e:
        print("'import pytest' - failed")
        print(e)
    else:
        print("'import pytest' - ok")


def test_use_module():
    from package import module
    try:
        module.main()
    except NameError:
        raise AssertionError("Failed to run 'module.main()'")


def test_access_resource():
    from package import module
    module.access_resource()
