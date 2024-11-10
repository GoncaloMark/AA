from exhaustive_search import ExhaustiveSearch
from greedy_search import GreedySearch
from typing import Dict
import os

def main() -> None:
    directory = "graphs"

    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".edgelist"):
                file_path = os.path.join(root, file)
                search: Dict[str, ExhaustiveSearch | GreedySearch] = {
                    "exhaustive": ExhaustiveSearch(),
                    "greedy": GreedySearch(),
                }
                for name, searcher in search.items():
                    print(f"\nRunning {name} search:")
                    searcher.process_edge_list_file(file_path)

if __name__ == "__main__":
    main()