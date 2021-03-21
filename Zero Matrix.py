"""
6. Zero Matrix (bytebybyte)
Question: Given a boolean matrix, update it so that if any cell is true, all the cells in that
row and column are true.

Example:

[true , false, false]    [true, true , true ]
[false, false, false] -> [true, false, false]
[false, false, false]    [true, false, false]

"""

def sol(arr):
    row_set = set()
    col_set = set()

    for row_index in range(len(arr)):
        for col_index in range(len(arr[row_index])):
            if arr[row_index][col_index] == True:
                row_set.add(row_index)
                col_set.add(col_index)

    for row_index in range(len(arr)):
        for col_index in range(len(arr[row_index])):
            if row_index in row_set:
                arr[row_index][col_index] = True
            if col_index in col_set:
                arr[row_index][col_index] = True

    return arr

"""
Steps:
1. Make row and columns set where I would keep track of columns and rows that will be true
2. Iterate through the matrix and use the row and columns set to keep track.
3. Re-iterate through the matrix again and use the row and columns set to turn to true.

"""
