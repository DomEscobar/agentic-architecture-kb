.PHONY: lint compile index test check

lint:
	python3 tools/wiki.py lint

compile:
	python3 tools/wiki.py compile

index:
	python3 tools/wiki.py index

test:
	python3 -m unittest discover -s tests -v

check: lint test compile
