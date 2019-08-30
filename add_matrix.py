# Given two two-dimensional lists of numbers of the size 2x2 
# two dimensional list is represented as a list of lists:

# [ [2, -2], [5, 3]]

# Calculate the result of adding the two matrices.  The number
# in each position in the resulting matrix should be the sum
# of the numbers in the corresponding addend matrices.  Example:

# [[1, 3], [2, 4]]
#
# and
#
# [[5, 2], [1, 0]]
#
# results in
# 
# [[6, 5], [3, 4]]

first_list = [[1, 3], [2, 4]]
second_list = [[5, 2], [1, 0]]

result = [[], []]

for index, item in enumerate(first_list):
    for nested_index, nested_item in enumerate(item):
        result[index].append(first_list[index][nested_index] +
        second_list[index][nested_index])

print(result)



