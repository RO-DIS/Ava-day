import Avaday.Model.board

import Avaday.Model.brain

snake_brains = Avaday.Model.brain.snake_brains

from Avaday.globals import np
from Avaday.Model.brain import symmetric_brain_coordinates, brain_coordinates, clockwise_powers
from Avaday.Model.parameters import board_size, view_directions


def on_board(point):
    return np.all((0 <= point) & (point < board_size))


def visited(point, snake):
    return on_board(point) and (snake in Avaday.Model.board.field[point[0]][point[1]])


def bad(point, snake):
    return not on_board(point) or on_board(point) and visited(point, snake)


def get_bad_indices(point, brain_half, snake):
    visible_coordinates = brain_half + point.T[:, np.newaxis]
    return np.where([bad(point=point, snake=snake) for point in visible_coordinates.T])


def get_all_bad_indices(point, direction, snake):
    left_half = get_bad_indices(point, symmetric_brain_coordinates[direction], snake)
    right_half = get_bad_indices(point, brain_coordinates[direction], snake)
    return np.append(left_half, right_half)


def get_move_direction(point, direction, snake):
    move_direction = np.argmax(
        np.sum(
            snake_brains[snake][get_all_bad_indices(point, direction, snake)], axis=0
        )
    )
    view_direction = move_direction // 2
    return move_direction, view_direction


def get_step_coordinate(view_direction):
    initial_step_coordinates = np.array([[1, 1], [0, 1]])
    return np.dot(
        clockwise_powers[view_direction],
        np.concatenate(
            [
                np.dot(clockwise_powers[i], initial_step_coordinates)
                for i in range(view_directions)
            ],
            axis=1,
        ),
    )


step_coordinates = np.array(
    [
        get_step_coordinate(view_direction=direction)
        for direction in range(view_directions)
    ]
).astype(int)
