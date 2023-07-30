SHELL := /bin/bash

.PHONY: help pypi-reset

.DEFAULT_GOAL := help

pr: pypi-reset
install: python-install

help:
	@echo "Please use 'make <target>' where <target> is one of the following:"
	@echo "  install    to install all dependencies"
	@echo "  pr         to publish to testpypi"



pypi-reset:
	rm -rf dist && \
	python3 -m build && \
	twine upload dist/*

python-install:
	python3 -m venv venv && \
	. venv/bin/activate && \
	pip install --upgrade pip && \
	pip install -r requirements.txt
