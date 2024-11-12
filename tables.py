import pandas as pd
import matplotlib.pyplot as plt
import os

output_folder = "solution"
os.makedirs(output_folder, exist_ok=True)

file_path = "solution/comparison.csv"

data = pd.read_csv(file_path)

data_sorted = data.sort_values(by='Vertices')

greedy_data = data_sorted[data_sorted['Algorithm'] == 'greedy']
exhaustive_data = data_sorted[data_sorted['Algorithm'] == 'exhaustive']

greedy_exec_time = greedy_data[['Vertices', 'Edge Distribution (%)', 'Execution Time (s)']]
greedy_exec_time.to_csv(os.path.join(output_folder, 'greedy_execution_time.csv'), index=False)

# CSV for Execution Time vs Vertices and Edge Distribution (Exhaustive Search)
exhaustive_exec_time = exhaustive_data[['Vertices', 'Edge Distribution (%)', 'Execution Time (s)']]
exhaustive_exec_time.to_csv(os.path.join(output_folder, 'exhaustive_execution_time.csv'), index=False)

# CSV for Operations vs Vertices and Edge Distribution (Greedy Search)
greedy_operations = greedy_data[['Vertices', 'Edge Distribution (%)', 'Operations']]
greedy_operations.to_csv(os.path.join(output_folder, 'greedy_operations.csv'), index=False)

# CSV for Operations vs Vertices and Edge Distribution (Exhaustive Search)
exhaustive_operations = exhaustive_data[['Vertices', 'Edge Distribution (%)', 'Operations']]
exhaustive_operations.to_csv(os.path.join(output_folder, 'exhaustive_operations.csv'), index=False)

print("CSV files have been generated and saved in the 'solution' folder.")