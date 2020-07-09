build: clean
	python3 setup.py sdist bdist_wheel
.PHONY: build

install: build
	python3 -m pip install --upgrade dist/*.whl
.PHONY: install

clean:
	rm -rf .mypy_cache __pycache__ packages/__pycache__ packages/dist packages/build packages/*.egg-info
.PHONY: clean
