# Re-attempting to generate and save the file

import random

# Generate 100,000 lines of test data
num_lines = 100000
urls = [f"https://example{i}.com/page{i}" for i in range(1, num_lines // 2 + 1)]  # Unique URLs

# Create operations
operations = []
for url in urls:
    operations.append(f"ADD {url}")
    operations.append(f"CONTAINS {url}")

# Shuffle to randomize the order
random.shuffle(operations)

# Define file path
file_path = "bloom_filter_test.txt"

# Write to a file
with open(file_path, "w") as file:
    file.write("\n".join(operations))

file_path