.PHONY: test test_k run

test:
	python3 -m pytest -s

test_k:
	python3 -m pytest -vvs -k $(NAME)

run:
	python3 -m keepachangelog_parser CHANGELOG.md

all: test run
