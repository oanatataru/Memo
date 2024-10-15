def play_song(musical_notes, moves, start_pos):
    notes = [musical_notes[start_pos]]

    current_pos = start_pos
    moves_count = len(musical_notes)
    for index in moves:
        current_pos = current_pos + index
        notes.append(musical_notes[current_pos % moves_count])

    return notes


print(play_song(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2))
