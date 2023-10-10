def find_obstructed_seats(matrix):
    obstructed_seats = []
    rows = len(matrix)
    cols = len(matrix[0])

    for row in range(1,rows):
        for col in range(cols):
           if matrix[row][col]<matrix[row-1][col]:
               obstructed_seats.append((row,col))

    return obstructed_seats

# Example usage:
stadium_matrix = [
    [1, 2, 3, 2, 1, 1],
    [2, 4, 4, 3, 7, 2],
    [5, 5, 2, 5, 6, 4],
    [6, 6, 7, 6, 7, 5]
                  ] 

obstructed_seats = find_obstructed_seats(stadium_matrix)
print(obstructed_seats)
