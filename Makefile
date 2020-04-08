build: build-packages clean
	pyinstaller -n dockerlint --add-data LICENSE:LICENSE main.py
	chmod +x dist/dockerlint/dockerlint
.PHONY: build

build-packages: clean
	cd linter && python3 setup.py sdist bdist_wheel
	pip3 install --upgrade linter/dist/*.whl
.PHONY: build-packages

run: build
	dist/dockerlint/dockerlint
.PHONY: run

clean:
	rm -rf .mypy_cache __pycache__ linter/__pycache__ linter/dockerfile_linter_pkg/__pycache__ *.spec dist build linter/dist linter/build linter/*.egg-info
.PHONY: clean

install-deps:
	python3 -m pip install pyinstaller
.PHONY: install-deps
