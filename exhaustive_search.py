import os
from itertools import combinations
import time
from typing import List, Tuple
class ExhaustiveSearch:
    def __init__(self) -> None:
        self.edges = []  
        self.vertices = set()  
        self.operations = 0

    def add_edge(self, u: int, v: int) -> None:
        """Add an edge to the graph and update vertices."""
        self.edges.append((u, v))
        self.vertices.update([u, v])  

    def is_valid_matching(self, subset: List[Tuple[int, int]]) -> bool:
        """Check if the provided subset of edges is a valid matching."""
        matched_vertices = set()
        
        for u, v in subset:
            # If one vertex is already matched, it is invalid
            if u in matched_vertices or v in matched_vertices:
                return False
            
            # Mark as matched
            matched_vertices.add(u)
            matched_vertices.add(v)
        
        return True

    def max_matching(self) -> Tuple[Tuple[int, int], ...]:
        """Find the maximum matching using brute force."""
        max_matching = []
        
        # Try all possible subsets of edges
        for r in range(len(self.edges) + 1):
            for subset in combinations(self.edges, r):
                self.operations += 1
                if self.is_valid_matching(subset) and len(subset) > len(max_matching):
                    max_matching = subset
        
        return max_matching

    def process_edge_list_file(self, file_path: str) -> Tuple[Tuple[Tuple[int, int], ...], float, int]:
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

        start = time.perf_counter()
        max_matching = self.max_matching()
        end = time.perf_counter()
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
                search = ExhaustiveSearch()
                search.process_edge_list_file(file_path)

if __name__ == "__main__":
    main()
