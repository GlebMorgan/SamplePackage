import os
import sys

print()
print(f"  __name__ = {__name__}")
print(f"  __file__ = {__file__}")
print(f"  cwd = {os.getcwd()}")
print(f"  PYTHONPATH = {os.environ.get('PYTHONPATH', None)}")
print(f"  sys.path = {sys.path}")
print(f"  args = {sys.argv}")


if __name__ == '__main__':
    print(f"Called {__name__}.py")
    from module import main
    main()
