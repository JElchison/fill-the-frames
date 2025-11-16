#!/usr/bin/env python3

# https://github.com/JElchison/fill-the-frames

import random


def single_problem():
    horizontal_line_left = random.randint(1, 9)
    horizontal_line_right = random.randint(5, 15)
    vertical_line = random.randint(3, 10)

    print(" ——" * horizontal_line_left, "|", "—— " * horizontal_line_right)
    print("|\n" * vertical_line)

    answer = ""
    left_side = horizontal_line_left * vertical_line
    right_side = horizontal_line_right * vertical_line
    answer += "%d + %d = %d" % (left_side, right_side, left_side + right_side)
    total_width = horizontal_line_left + horizontal_line_right
    answer += "\n%d x %d = %d\n" % (vertical_line, total_width, vertical_line * total_width)
    return answer


if __name__ == "__main__":
    print("Fill the Frames Worksheet\n\n")

    number_of_problems = 5
    answers = []
    for _ in range(number_of_problems):
        answers.append(single_problem())
        print("\n")
    
    print("\f")  # Form feed for new page"
    print("Answers:\n")
    for _ in answers:
        print(_)