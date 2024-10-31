import os
from itertools import combinations

class ExhaustiveSearch:
    def __init__(self):
        self.edges = []  
        self.vertices = set()  

    def add_edge(self, u, v):
        """Add an edge to the graph and update vertices."""
        self.edges.append((u, v))
        self.vertices.update([u, v])  

    def is_valid_matching(self, subset):
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

    def brute_force_max_matching(self):
        """Find the maximum matching using brute force."""
        max_matching = []
        
        # Try all possible subsets of edges
        for r in range(len(self.edges) + 1):
            for subset in combinations(self.edges, r):
                if self.is_valid_matching(subset) and len(subset) > len(max_matching):
                    max_matching = subset
        
        return max_matching

def process_edge_list_file(file_path):
    """Read edges from a file and find the maximum matching."""
    search = ExhaustiveSearch() 

    # Read edge lists
    with open(file_path, 'r') as file:
        for line in file:
            u, v, _ = line.strip().split() 
            u, v = int(u), int(v)
            search.add_edge(u, v)

    # Debug vertex number is correct
    n = len(search.vertices)
    print(f"\nProcessing '{file_path}'")
    print(f"Number of vertices inferred: {n}")

    max_matching = search.brute_force_max_matching()
    print("Maximum Matching:", max_matching)

def main():
    directory = "graphs"

    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".edgelist"):
                file_path = os.path.join(root, file)
                process_edge_list_file(file_path)

if __name__ == "__main__":
    main()
