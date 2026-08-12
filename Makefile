.PHONY: lint compile index hybrid-index retrieval-benchmark memory-projection drift test check

lint:
	python3 tools/wiki.py lint

compile:
	python3 tools/wiki.py compile

index:
	python3 tools/wiki.py index

hybrid-index:
	python3 tools/hybrid.py build

retrieval-benchmark: hybrid-index
	python3 tools/hybrid.py benchmark

memory-projection: compile
	python3 tools/build_memory_projection.py

drift:
	python3 tools/check_consumers.py

test:
	python3 -m unittest discover -s tests -v

check: lint test compile
