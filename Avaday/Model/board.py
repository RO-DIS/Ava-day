from Avaday.globals import np
from Avaday.Model.parameters import board_size, snake_ids


def clear_field():
    return np.array([[set() for _ in range(board_size)] for _ in range(board_size)])


field = clear_field()


def add_randomly_visited_cells(snake):
    number_of_randomly_visited_cells = board_size
    for cell in range(number_of_randomly_visited_cells):
        i, j = np.random.randint(low=0, high=board_size - 1, size=2)
        field[i][j].add(snake)


def add_snakes_visits():
    for snake_id in snake_ids:
        add_randomly_visited_cells(snake_id)
