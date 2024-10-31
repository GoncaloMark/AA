import random
import os
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from itertools import combinations
import math

class Generator:
    def __init__(self, seed, min_distance=10):
        self.seed = seed
        self.min_distance = min_distance
        random.seed(self.seed)
        np.random.seed(self.seed)
    
    def generate_point(self, existing_points):
        """Generate a random 2D point with a minimum distance from existing points."""
        while True:
            point = (random.randint(1, 1000), random.randint(1, 1000))
            if all(np.linalg.norm(np.array(point) - np.array(p)) >= self.min_distance for p in existing_points):
                return point
    
    def create_random_graph(self, num_vertices, edge_density):
        """Create a random graph with a specified number of vertices and edge density."""
        vertices = [self.generate_point([]) for _ in range(num_vertices)]
        G = nx.Graph()

        for i, vertex in enumerate(vertices):
            G.add_node(i, pos=vertex)
        
        possible_edges = list(combinations(range(num_vertices), 2))
        
        max_edges = len(possible_edges)
        num_edges = math.ceil(max_edges * edge_density)  

        random.shuffle(possible_edges)

        for edge in possible_edges[:num_edges]:
            G.add_edge(*edge)

        return G

class GraphVisualizer:
    @staticmethod
    def visualize_and_save(G, filename):
        """Visualize and save the graph as an image."""
        pos = nx.get_node_attributes(G, 'pos')
        plt.figure()
        nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=500)
        plt.savefig(f'{filename}.png')
        # plt.show()

class GraphStorage:
    @staticmethod
    def save_graph(G, filename, format='adjlist'):
        """Save the graph in different types of lists."""
        if format == 'adjlist':
            nx.write_adjlist(G, f'{filename}.adjlist')
        elif format == 'edgelist':
            nx.write_edgelist(G, f'{filename}.edgelist')
        elif format == 'incidencelist':
            nodes = list(G.nodes())
            edges = list(G.edges())
            
            incidence = np.zeros((len(nodes), len(edges)), dtype=int)
            
            for edge_idx, (u, v) in enumerate(edges):
                u_idx = nodes.index(u)
                v_idx = nodes.index(v)
                
                incidence[u_idx, edge_idx] = 1
                incidence[v_idx, edge_idx] = 1

            np.savetxt(f'{filename}_incidence.txt', incidence, fmt='%d')
        else:
            raise ValueError(f"Unknown format: {format}")

class Graph:
    def __init__(self, seed):
        self.graph_generator = Generator(seed)
        self.visualizer = GraphVisualizer()
        self.storage = GraphStorage()

    def run(self, vertex_range, edge_densities):
        """Run graph generation for a range of vertices and edge densities."""
        base_folder = "graphs"
        if not os.path.exists(base_folder):
            os.makedirs(base_folder)

        for num_vertices in vertex_range:
            for density in edge_densities:
                folder_name = f'graph_{num_vertices}_vertices_{int(density * 100)}_percent_edges'
                folder_path = os.path.join(base_folder, folder_name)

                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)

                G = self.graph_generator.create_random_graph(num_vertices, density)
                
                base_filename = os.path.join(folder_path, f'graph_{num_vertices}_v_{int(density * 100)}')
                
                self.storage.save_graph(G, base_filename, format='adjlist')
                self.storage.save_graph(G, base_filename, format='edgelist')
                self.storage.save_graph(G, base_filename, format='incidencelist')

                self.visualizer.visualize_and_save(G, f'{base_filename}')

if __name__ == '__main__':
    student_number = 98648
    vertex_range = range(4, 7)  
    edge_densities = [0.125, 0.25, 0.5, 0.75] 
    
    experiment = Graph(student_number)
    experiment.run(vertex_range, edge_densities)
