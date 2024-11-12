.PHONY: graphs exsearch greedysearch plots tables all

graphs:
	python3 graph.py

exsearch:
	python3 exhaustive_search.py

greedysearch:
	python3 greedy_search.py

plots:
	python3 results.py

tables:
	python3 tables.py

all:
	python3 main.py
