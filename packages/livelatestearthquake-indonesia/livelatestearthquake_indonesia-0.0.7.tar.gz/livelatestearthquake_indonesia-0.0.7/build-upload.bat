@echo off
rmdir dist /A
py -m build
py -m twine upload --repository pypi dist/*