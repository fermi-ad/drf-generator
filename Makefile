drf_generator.tgz : LICENSE README.md setup.py drf_generator/*py
	tar czf $@ $^

install_dev:
	python -m pip install -r requirements_dev.txt

install: install_dev
	python -m pip install --upgrade pip
	python -m pip install -r requirements.txt

lint: install
	python -m flake8

test: install
	python -m pytest

test_full: install
	python -m tox

coverage: install
	python -m pytest --cov-report term-missing

clean:
	for ii in $$(find . -type d -name __pycache__); do \
	  rm -rf $${ii}; \
	done
	for ii in $$(find . -type d -name "*.egg-info"); do \
	  rm -rf $${ii}; \
	done
	rm -rf .mypy_cache
	rm -rf .pytest_cache
	rm -rf .tox
	rm .coverage
