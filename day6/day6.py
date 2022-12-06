def find_start_signal(message: str, k: int) -> int:
    character_counts = {}

    for index, character in enumerate(message):
        if len(character_counts) == k:
            return index

        character_counts[character] = character_counts.get(character, 0) + 1

        if index >= k:
            character_to_remove = message[index - k]
            character_counts[character_to_remove] -= 1
            if character_counts[character_to_remove] == 0:
                character_counts.pop(character_to_remove)


def solve(k) -> None:
    # file = open('sample_input_6.txt', 'r')
    file = open('input_6.txt', 'r')
    lines = file.readlines()

    start_signal = find_start_signal(lines[0], k)
    print(f"start signal is: {start_signal}")


solve(14)
