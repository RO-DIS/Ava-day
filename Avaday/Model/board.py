from Avaday.config import np
from Avaday.Model.config import BOARD_SIZE, snake_ids


def clear_field():
    return np.array([[set() for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)])


field = clear_field()


def add_randomly_visited_cells(snake):
    number_of_randomly_visited_cells = BOARD_SIZE
    for cell in range(number_of_randomly_visited_cells):
        i, j = np.random.randint(low=0, high=BOARD_SIZE - 1, size=2)
        field[i][j].add(snake)


def add_snakes_visits():
    for snake_id in snake_ids:
        add_randomly_visited_cells(snake_id)
