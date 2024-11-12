from exhaustive_search import ExhaustiveSearch
from greedy_search import GreedySearch
from typing import Dict
import os
import csv
import re

def extract_graph_info(directory_name: str) -> tuple[int, float]:
    vertices_match = re.search(r'(\d+)_vertices', directory_name)
    edges_match = re.search(r'(\d+)_percent', directory_name)
    
    vertices = int(vertices_match.group(1)) if vertices_match else 0
    edge_percent = float(edges_match.group(1)) if edges_match else 0

    if edge_percent == 12:
        edge_percent = 12.5
    return vertices, edge_percent

def main() -> None:
    directory = "graphs"

    solution_dir = "solution"
    
    if not os.path.exists(solution_dir):
        os.makedirs(solution_dir)

    with open(os.path.join(solution_dir, "comparison.csv"), 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Algorithm', 'Vertices', 'Edge Distribution (%)', 'Edges', 'Execution Time (s)', 'Solution Size', 'Operations'])

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
                        solution, execution_time, ops = searcher.process_edge_list_file(file_path)
                        vertices, edge_percent = extract_graph_info(root)

                        writer.writerow([
                            name,
                            vertices,
                            edge_percent,
                            len(searcher.edges),
                            execution_time,
                            len(solution),
                            ops
                        ])

if __name__ == "__main__":
    main()