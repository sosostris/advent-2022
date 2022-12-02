# file = open('sample_input_2.txt', 'r')
file = open('input_2.txt', 'r')
lines = file.readlines()

# A is rock
# B is papers
# C is scissors
shape_scores = {
    "A": 1,
    "B": 2,
    "C": 3,
}

# X is lose
# Y is draw
# Z is win
match_scores = {
    "X": 0,
    "Y": 3,
    "Z": 6
}


def get_my_shape(opponent_shape, match_result):
    shapes = list(shape_scores.keys())

    if match_result == "X":
        return shapes[shapes.index(opponent_shape) - 1]

    if match_result == "Z":
        return shapes[(shapes.index(opponent_shape) + 1) % 3]

    return opponent_shape


def get_score_for_round(opponent_shape, match_result):
    my_shape = get_my_shape(opponent_shape, match_result)
    return match_scores[match_result] + shape_scores[my_shape]


final_score = 0

for line in lines:
    content = line.strip()
    if content != "":
        current_round = content.split(" ")
        opponent_shape_for_current_round = current_round[0]
        match_result_for_current_round = current_round[1]

        final_score += get_score_for_round(opponent_shape_for_current_round, match_result_for_current_round)

print("Final score: {}".format(final_score))
