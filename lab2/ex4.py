def compose(notes, moves, start_position):
    song = []
    position = start_position
    song.append(notes[start_position])
    for move in moves:
        position = (position + move) % len(notes)
        song.append(notes[position])
    return song

notes = ["do", "re", "mi", "fa", "sol"]
moves = [1, -3, 4, 2]
start_position = 2

result = compose(notes, moves, start_position)
print(result)

