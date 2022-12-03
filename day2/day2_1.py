# file = open('sample_input_2.txt', 'r')
file = open('input_2.txt', 'r')
lines = file.readlines()

# A, X are rock
# B, Y are papers
# C, Z are scissors
scores = {
    "X": 1,
    "Y": 2,
    "Z": 3,
}


def convert_shape_to_xyz(shape):
    if shape == "A":
        return "X"
    if shape == "B":
        return "Y"
    return "Z"


def get_score_for_round(opponent_shape, my_shape):
    score = scores[my_shape]

    if scores[my_shape] - scores[opponent_shape] == 1 or (my_shape == "X" and opponent_shape == "Z"):
        return score + 6

    if my_shape == opponent_shape:
        return score + 3

    return score


final_score = 0

for line in lines:
    content = line.strip()
    if content != "":
        shapes = content.split(" ")
        opponent_shape_for_current_round = convert_shape_to_xyz(shapes[0])
        my_shape_for_current_round = shapes[1]

        final_score += get_score_for_round(opponent_shape_for_current_round, my_shape_for_current_round)

print("Final score: {}".format(final_score))
