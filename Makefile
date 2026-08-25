.PHONY: lint compile index navigation hybrid-index retrieval-benchmark memory-projection drift freshness-check repo-pulse due-reviews test check consult discovery-sync mcp

lint:
	python3 tools/wiki.py lint

compile:
	python3 tools/wiki.py compile

index:
	python3 tools/wiki.py index

navigation:
	python3 tools/wiki.py navigation

hybrid-index:
	python3 tools/hybrid.py build

retrieval-benchmark: hybrid-index
	python3 tools/hybrid.py benchmark

memory-projection: compile
	python3 tools/build_memory_projection.py

drift:
	python3 tools/check_consumers.py

freshness-check:
	python3 tools/freshness.py validate

repo-pulse:
	python3 tools/freshness.py repo-pulse

due-reviews:
	python3 tools/freshness.py due-reviews

consult:
	@test -n "$(QUESTION)" || (echo 'usage: make consult QUESTION="<architecture question>"' >&2; exit 2)
	python3 tools/consult_architecture.py "$(QUESTION)"

discovery-sync:
	python3 tools/sync_discovery.py

mcp:
	python3 tools/mcp_architecture_server.py

test:
	python3 -m unittest discover -s tests -v

check: lint freshness-check compile test
