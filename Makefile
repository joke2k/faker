test:
	coverage run --source=faker --omit=faker/build_docs.py setup.py test

release:
	check-manifest
	rm -rf build dist
	python setup.py sdist bdist_wheel
	git push --tags
	twine upload dist/*
