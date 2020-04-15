build: clean
	cd packages && python3 setup.py sdist bdist_wheel
	python3 -m pip install --upgrade packages/dist/*.whl
.PHONY: build

clean:
	rm -rf .mypy_cache __pycache__ packages/__pycache__ packages/dist packages/build packages/*.egg-info
.PHONY: clean

install-deps:
	python3 -m pip install --upgrade pip setuptools wheel click colorama
.PHONY: install-deps
