test:
	tox -e py

isort:
	isort -rc --atomic .

release:
	check-manifest
	rm -rf build dist
	python setup.py sdist bdist_wheel
	git push --tags
	twine upload dist/*
