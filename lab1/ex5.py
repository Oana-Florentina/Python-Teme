def spiral_order(matrix):
    if not matrix:
        return ""

    result = []
    top, bottom, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1

    while top <= bottom and left <= right:
        # Traverse top row
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1

        # Traverse rightmost column
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1

        # Traverse bottom row
        if top <= bottom:  # Check to avoid duplicate traversal
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1

        # Traverse leftmost column
        if left <= right:  # Check to avoid duplicate traversal
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1

    return ''.join(result)

# Example usage
if __name__ == "__main__":
    matrix = [
        ['F', 'I', 'R', 'S'],
        ['N', '_', 'L', 'T'],
        ['O', 'B', 'A', '_'],
        ['H', 'T', 'Y', 'P']
    ]
    
    result = spiral_order(matrix)
    print(result)
