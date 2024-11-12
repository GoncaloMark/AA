import os
import time
from collections import defaultdict
from typing import List, Tuple, Dict

class GreedySearch:
    def __init__(self) -> None:
        self.edges = []  
        self.vertices = set()  
        self.operations = 0

    def add_edge(self, u: int, v: int) -> None:
        """Add an edge to the graph and update vertices."""
        self.edges.append((u, v))
        self.vertices.update([u, v])  

    def calculate_degrees(self) -> Dict[int, int]:
        """Calculate the degree of each vertex in the graph."""
        degree = defaultdict(int)
        for u, v in self.edges:
            self.operations += 1
            degree[u] += 1
            degree[v] += 1
        return degree

    def max_matching(self) -> List[Tuple[int, int]]:
        """Find a maximum matching using a greedy heuristic based on vertex degree."""
        degree = self.calculate_degrees()
        
        sorted_edges = sorted(self.edges, key=lambda edge: degree[edge[0]] + degree[edge[1]], reverse=True)
        
        max_matching = []
        matched_vertices = set()

        for u, v in sorted_edges:
            self.operations += 1
            if u not in matched_vertices and v not in matched_vertices:
                max_matching.append((u, v))
                matched_vertices.add(u)
                matched_vertices.add(v)

        return max_matching

    def process_edge_list_file(self, file_path: str) -> Tuple[List[Tuple[int, int]], float]:
        """Read edges from a file and find the maximum matching."""
        # Read edge lists
        with open(file_path, 'r') as file:
            for line in file:
                u, v, _ = line.strip().split() 
                u, v = int(u), int(v)
                self.add_edge(u, v)

        # Debug vertex number is correct
        n = len(self.vertices)
        print(f"\nProcessing '{file_path}'")
        print(f"Number of vertices inferred: {n}")

        start = time.time()
        max_matching = self.max_matching()
        end = time.time()
        execution_time = end - start
        print("Maximum Matching:", max_matching)
        print(f"Time::[{execution_time}s]")

        return (max_matching, execution_time, self.operations)

def main() -> None:
    directory = "graphs"
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".edgelist"):
                file_path = os.path.join(root, file)
                search = GreedySearch()
                search.process_edge_list_file(file_path)

if __name__ == "__main__":
    main()
