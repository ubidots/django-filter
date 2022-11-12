.PHONY: deps, test, clean

deps:
	pip install -r ./requirements/test.txt

test:
	./runtests.py

clean:
	rm -r build dist django_filter.egg-info

build:
	python -m build

publish: build
	python -m twine upload --repository ubidots dist/*