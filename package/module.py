import os
import sys


print()
print(f"  __name__ = {__name__}")
print(f"  __file__ = {__file__}")
print(f"  cwd = {os.getcwd()}")
print(f"  PYTHONPATH = {os.environ.get('PYTHONPATH', None)}")
print(f"  sys.path = {sys.path}")
print(f"  args = {sys.argv}")


def main():
    print(f"Called {__name__}.py:main()")


def access_resource():
    from pkg_resources import resource_string, resource_filename
    print(f"Called {__name__}.py:access_resource()")

    path = 'res/test_res.txt'
    try:
        print("Resource string: ", resource_string(__name__, path).decode('utf-8'))
        print("Resource filename: ", resource_filename(__name__, path))
    except Exception as e:
        print("Failed to access resources")
        print(f'{e.__class__}: {e}')
    else:
        print("Successfully accesses resources")
