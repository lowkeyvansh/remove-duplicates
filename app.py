# Example list with duplicates
original_list = [1, 2, 2, 3, 4, 4, 5]

# Using a loop to remove duplicates
unique_list = []
for item in original_list:
    if item not in unique_list:
        unique_list.append(item)

print(unique_list)
