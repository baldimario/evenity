.DEFAULT_GOAL := help
SHELL := /bin/bash

include .env

help: ## Show this help
	@echo -e "$$(grep -hE '^\S+:.*##' $(MAKEFILE_LIST) | sed -e 's/:.*##\s*/:/' -e 's/^\(.\+\):\(.*\)/\\x1b[36m\1\\x1b[m:\2/' | column -c2 -t -s :)"

venv: ## activate the virtual environment
	source bin/activate

clean: ## Clean build files
	rm -rf dist && rm -rf src/*.egg-info

build: clean ## Build the python package
	python -m build

staging: ## Deploy on test.pypi.org with twine
	@twine upload -u "$(TWINE_USERNAME)" -p "$(TWINE_PASSWORD)" --repository-url https://test.pypi.org/legacy/ dist/*