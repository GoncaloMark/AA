import pandas as pd
import matplotlib.pyplot as plt
import os

output_folder = "solution"
os.makedirs(output_folder, exist_ok=True)

file_path = "solution/comparison.csv"

data = pd.read_csv(file_path)

data_sorted = data.sort_values(by='Edges')

greedy_data = data_sorted[data_sorted['Algorithm'] == 'greedy']
exhaustive_data = data_sorted[data_sorted['Algorithm'] == 'exhaustive']

plt.figure(figsize=(10, 6))
plt.plot(greedy_data['Edges'], greedy_data['Execution Time (s)'], color='blue', label='Greedy', marker='o', linestyle='-', alpha=0.6)
plt.plot(exhaustive_data['Edges'], exhaustive_data['Execution Time (s)'], color='red', label='Exhaustive', marker='o', linestyle='-', alpha=0.6)

plt.title('Execution Time vs Number of Edges')
plt.xlabel('Number of Edges')
plt.ylabel('Execution Time (s)')
plt.legend()
plt.grid(True)

plt.xticks(range(1, data_sorted['Edges'].max(), 5))

plt.yscale('log')

plt.savefig(os.path.join(output_folder, 'execution_time_vs_edges_log_sorted.png'))

plt.figure(figsize=(10, 6))
plt.plot(greedy_data['Edges'], greedy_data['Operations'], color='blue', label='Greedy', marker='o', linestyle='-', alpha=0.6)
plt.plot(exhaustive_data['Edges'], exhaustive_data['Operations'], color='red', label='Exhaustive', marker='o', linestyle='-', alpha=0.6)

plt.title('Operations vs Number of Edges')
plt.xlabel('Number of Edges')
plt.ylabel('Operations')
plt.legend()
plt.grid(True)

plt.xticks(range(1, data_sorted['Edges'].max(), 5))

plt.yscale('log')

plt.savefig(os.path.join(output_folder, 'operations_vs_edges_sorted.png'))

merged_data = pd.merge(greedy_data[['Vertices', 'Edge Distribution (%)', 'Solution Size']], exhaustive_data[['Vertices', 'Edge Distribution (%)', 'Solution Size']], on=['Vertices', 'Edge Distribution (%)'], suffixes=('_greedy', '_exhaustive'))
merged_data['Error Rate'] = abs(merged_data['Solution Size_greedy'] - merged_data['Solution Size_exhaustive']) / merged_data['Solution Size_exhaustive'] * 100
vertices_error_rate = merged_data.groupby('Vertices')['Error Rate'].mean().reset_index()
vertices_error_rate_sorted = vertices_error_rate.sort_values(by='Error Rate', ascending=False)
edge_density_error_rate = merged_data.groupby('Edge Distribution (%)')['Error Rate'].mean().reset_index()
edge_density_error_rate_sorted = edge_density_error_rate.sort_values(by='Error Rate', ascending=False)
vertices_error_rate_sorted.to_csv(os.path.join(output_folder, 'vertices_error_rate_comparison.csv'), index=False)
edge_density_error_rate_sorted.to_csv(os.path.join(output_folder, 'edge_density_error_rate_comparison.csv'), index=False)

print("Vertices Error Rate Comparison:")
print(vertices_error_rate_sorted[['Vertices', 'Error Rate']])
print("\nEdge Density Error Rate Comparison:")
print(edge_density_error_rate_sorted[['Edge Distribution (%)', 'Error Rate']])
