import Avaday.Model.board
from Avaday.config import ROOT_DIR, np, MAXIMAL_PATH_LENGTH, NUMBER_OF_PATHS
from Avaday.Model.config import BOARD_SIZE, view_directions
from Avaday.Model.steps import bad, step_coordinates, get_move_direction, on_board

unused_coordinates = {(i, j) for i in range(1, BOARD_SIZE - 1) for j in range(1, BOARD_SIZE - 1)}


def get_snake_path(snake=0):
    """generates a path from random point"""
    if not unused_coordinates:
        return np.array([[0, 0], [0, 1]])

    path = np.zeros((2, MAXIMAL_PATH_LENGTH)).astype(int)
    path_length = 1
    path[:, 0] = unused_coordinates.pop()
    view_direction = np.random.randint(low=0, high=4)

    for step in range(MAXIMAL_PATH_LENGTH - 1):
        move_direction, view_direction = get_move_direction(
            point=path[:, step], direction=view_direction, snake=snake
        )
        next_point = path[:, step] + step_coordinates[view_direction][:, move_direction]
        if not bad(next_point, snake=snake):
            path[:, step + 1] = next_point
            path_length += 1
            unused_coordinates.discard((next_point[0], next_point[1]))
            Avaday.Model.board.field[next_point[0]][next_point[1]].add(snake)
        else:
            if on_board(next_point):
                path[:, step + 1] = next_point
                path = path[:, : step + 2]
            else:
                path = path[:, : step + 1]
            break

    return path

from pathlib import Path

def save_snake_paths(snake=0):
    """saves several paths into file"""
    # create the directory
    Path(f"{ROOT_DIR}/resources/paths").mkdir(parents=True,exist_ok=True)
    
    f = open(f"{ROOT_DIR}/resources/paths/path.csv", "a+")
    for i in range(NUMBER_OF_PATHS):
        snake_path = get_snake_path(snake).astype(int)
        Avaday.Model.board.field[tuple(snake_path)] = set()
        np.savetxt(fname=f, X=snake_path, delimiter=",", fmt="%i")


def get_snake_path_length(snake):
    """calculates length of a path"""
    path_length = 1
    current_point = np.random.randint(low=0, high=BOARD_SIZE - 1, size=2)
    view_direction = np.random.randint(view_directions)

    for step in range(BOARD_SIZE ** 2):
        move_direction, view_direction = get_move_direction(
            point=current_point, direction=view_direction, snake=snake
        )
        next_point = current_point + step_coordinates[view_direction][:, move_direction]
        if not bad(point=next_point, snake=snake):
            Avaday.Model.board.field[next_point[0]][next_point[1]].add(snake)
            path_length += 1
            current_point = next_point
        else:
            break
    return path_length
