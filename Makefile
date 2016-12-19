test:
	coverage run --source=faker setup.py test

release:
	rm -rf dist
	python setup.py sdist bdist_wheel
	twine upload dist/*
