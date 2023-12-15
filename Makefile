test:
	tox -e py

flake8:
	flake8 --extend-ignore=E203 faker tests

mypy:
	mypy --install-types --non-interactive --config mypy.ini faker

black:
	black --line-length 120 .

isort:
	isort --atomic .

lint: isort black mypy flake8

generate-stubs: python generate-stubs.py

release: generate-stubs
	check-manifest
	rm -rf build dist
	python setup.py sdist bdist_wheel
	git push --tags
	twine upload dist/*
