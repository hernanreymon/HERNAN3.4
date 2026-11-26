
# Assessment 3.7: Sorting Algorithms
# Name: REYMON HERNAN

# Full Name
name = "REYMON HERNAN"

# Remove spaces and duplicate letters
unsorted_array = list(dict.fromkeys(name.replace(" ", "")))

# Display Unsorted Array
print("Full Name:", name)
print("Unsorted Array:", unsorted_array)

# Bubble Sort
for i in range(len(unsorted_array)):
    for j in range(0, len(unsorted_array) - i - 1):
        if unsorted_array[j] > unsorted_array[j + 1]:
            unsorted_array[j], unsorted_array[j + 1] = (
                unsorted_array[j + 1],
                unsorted_array[j]
            )

# Display Sorted Array
print("Sorted Array:", unsorted_array)
