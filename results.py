import pandas as pd
import matplotlib.pyplot as plt
import os

output_folder = "solution"
os.makedirs(output_folder, exist_ok=True)

file_path = "solution/comparison.csv"

data = pd.read_csv(file_path)

# Sort the data by Vertices and Edge Distribution
data_sorted = data.sort_values(by=['Vertices', 'Edge Distribution (%)'])

plt.figure(figsize=(10, 6))

greedy_data = data_sorted[data_sorted['Algorithm'] == 'greedy']
exhaustive_data = data_sorted[data_sorted['Algorithm'] == 'exhaustive']

# Greedy algorithm
greedy_12p5 = data_sorted[(data_sorted['Algorithm'] == 'greedy') & (data_sorted['Edge Distribution (%)'] == 12.5)]
greedy_50p = data_sorted[(data_sorted['Algorithm'] == 'greedy') & (data_sorted['Edge Distribution (%)'] == 50)]
greedy_75p = data_sorted[(data_sorted['Algorithm'] == 'greedy') & (data_sorted['Edge Distribution (%)'] == 75)]

plt.plot(greedy_12p5['Vertices'], greedy_12p5['Execution Time (s)'], color='blue', label='Greedy g_12.5', marker='o', linestyle='-', alpha=0.6)
plt.plot(greedy_50p['Vertices'], greedy_50p['Execution Time (s)'], color='green', label='Greedy g_50', marker='o', linestyle='-', alpha=0.6)
plt.plot(greedy_75p['Vertices'], greedy_75p['Execution Time (s)'], color='orange', label='Greedy g_75', marker='o', linestyle='-', alpha=0.6)

# Exhaustive algorithm
exhaustive_12p5 = data_sorted[(data_sorted['Algorithm'] == 'exhaustive') & (data_sorted['Edge Distribution (%)'] == 12.5)]
exhaustive_50p = data_sorted[(data_sorted['Algorithm'] == 'exhaustive') & (data_sorted['Edge Distribution (%)'] == 50)]
exhaustive_75p = data_sorted[(data_sorted['Algorithm'] == 'exhaustive') & (data_sorted['Edge Distribution (%)'] == 75)]

plt.plot(exhaustive_12p5['Vertices'], exhaustive_12p5['Execution Time (s)'], color='red', label='Exhaustive ex_12.5', marker='o', linestyle='-', alpha=0.6)
plt.plot(exhaustive_50p['Vertices'], exhaustive_50p['Execution Time (s)'], color='black', label='Exhaustive ex_50', marker='o', linestyle='-', alpha=0.6)
plt.plot(exhaustive_75p['Vertices'], exhaustive_75p['Execution Time (s)'], color='brown', label='Exhaustive ex_75', marker='o', linestyle='-', alpha=0.6)

plt.title('Execution Time vs Number of Vertices')
plt.xlabel('Number of Vertices')
plt.ylabel('Execution Time (s)')
plt.legend()
plt.grid(True)

plt.yscale('log')

plt.savefig(os.path.join(output_folder, 'execution_time_vs_vertices_log_sorted.png'))

# Create a line plot with Vertices on the X-axis and each algorithm/edge distribution as a line
plt.figure(figsize=(10, 6))

# Greedy algorithm
plt.plot(greedy_12p5['Vertices'], greedy_12p5['Operations'], color='blue', label='Greedy g_12.5', marker='o', linestyle='-', alpha=0.6)
plt.plot(greedy_50p['Vertices'], greedy_50p['Operations'], color='green', label='Greedy g_50', marker='o', linestyle='-', alpha=0.6)
plt.plot(greedy_75p['Vertices'], greedy_75p['Operations'], color='orange', label='Greedy g_75', marker='o', linestyle='-', alpha=0.6)

# Exhaustive algorithm
plt.plot(exhaustive_12p5['Vertices'], exhaustive_12p5['Operations'], color='red', label='Exhaustive ex_12.5', marker='o', linestyle='-', alpha=0.6)
plt.plot(exhaustive_50p['Vertices'], exhaustive_50p['Operations'], color='black', label='Exhaustive ex_50', marker='o', linestyle='-', alpha=0.6)
plt.plot(exhaustive_75p['Vertices'], exhaustive_75p['Operations'], color='brown', label='Exhaustive ex_75', marker='o', linestyle='-', alpha=0.6)

plt.title('Operations vs Number of Vertices')
plt.xlabel('Number of Vertices')
plt.ylabel('Operations')
plt.legend()
plt.grid(True)

plt.yscale('log')

plt.savefig(os.path.join(output_folder, 'operations_vs_vertices_sorted.png'))

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
