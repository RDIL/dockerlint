build: build-packages clean
	pyinstaller -n dockerlint --add-data LICENSE:LICENSE --runtime-hook=mixins/py2-warn-populate.py main.py
	chmod +x dist/dockerlint/dockerlint
	tar cJf dockerlint.tar.xz dist/dockerlint
.PHONY: build

build-packages: clean
	cd linter && python3 setup.py sdist bdist_wheel
	pip3 install --upgrade linter/dist/*.whl
.PHONY: build-packages

clean:
	rm -rf .mypy_cache __pycache__ ./dockerlint linter/__pycache__ mixins/__pycache__ linter/dockerfile_linter_pkg/__pycache__ *.spec dist build linter/dist linter/build linter/*.egg-info dockerlint.tar.xz
.PHONY: clean

install-deps:
	python3 -m pip install --upgrade pyinstaller click colorama
.PHONY: install-deps
