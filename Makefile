.PHONY: deps, test, clean

deps:
	pip install -r ./requirements/test.txt

test:
	./runtests.py

clean:
	rm -r build dist django_filter.egg-info

build:
	python -m build

code_artifact_login:
	./twine_aws_login.sh

publish: build code_artifact_login
	python -m twine upload --repository codeartifact dist/*

