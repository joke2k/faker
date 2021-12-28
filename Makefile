test:
	tox -e py

mypy:
	mypy --install-types --non-interactive --config mypy.ini faker

black:
	black --line-length 120 .

isort:
	isort --atomic .

lint: isort black mypy

release:
	check-manifest
	rm -rf build dist
	python setup.py sdist bdist_wheel
	git push --tags
	twine upload dist/*
