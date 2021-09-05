import model.board
from globals.globals import np, max_path_length, number_of_paths
from model.parameters import board_size, view_directions
from model.steps import bad, step_coordinates, get_move_direction, on_board

unused_coordinates = {(i, j) for i in range(1, board_size - 1) for j in range(1, board_size - 1)}


def get_snake_path(snake=0):
    """generates a path from random point"""
    if not unused_coordinates:
        return np.array([[0, 0], [0, 1]])

    path = np.zeros((2, max_path_length)).astype(int)
    path_length = 1
    path[:, 0] = unused_coordinates.pop()
    view_direction = np.random.randint(low=0, high=4)

    for step in range(max_path_length - 1):
        move_direction, view_direction = get_move_direction(
            point=path[:, step], direction=view_direction, snake=snake
        )
        next_point = path[:, step] + step_coordinates[view_direction][:, move_direction]
        if not bad(next_point, snake=snake):
            path[:, step + 1] = next_point
            path_length += 1
            unused_coordinates.discard((next_point[0], next_point[1]))
            model.board.field[next_point[0]][next_point[1]].add(snake)
        else:
            if on_board(next_point):
                path[:, step + 1] = next_point
                path = path[:, : step + 2]
            else:
                path = path[:, : step + 1]
            break

    return path


def save_snake_paths(snake=0):
    """saves several paths into file"""
    open("./resources/paths/path.csv", "w").close()
    f = open("./resources/paths/path.csv", "a+")
    for i in range(number_of_paths):
        snake_path = get_snake_path(snake).astype(int)
        model.board.field[tuple(snake_path)] = set()
        np.savetxt(fname=f, X=snake_path, delimiter=",", fmt="%i")


def get_snake_path_length(snake):
    """calculates length of a path"""
    path_length = 1
    current_point = np.random.randint(low=0, high=board_size - 1, size=2)
    view_direction = np.random.randint(view_directions)

    for step in range(board_size ** 2):
        move_direction, view_direction = get_move_direction(
            point=current_point, direction=view_direction, snake=snake
        )
        next_point = current_point + step_coordinates[view_direction][:, move_direction]
        if not bad(point=next_point, snake=snake):
            model.board.field[next_point[0]][next_point[1]].add(snake)
            path_length += 1
            current_point = next_point
        else:
            break
    return path_length
