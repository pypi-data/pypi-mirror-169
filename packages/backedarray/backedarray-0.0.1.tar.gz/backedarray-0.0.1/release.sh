set -e

rm -rf dist
python -m build
python3 -m twine upload dist/*
