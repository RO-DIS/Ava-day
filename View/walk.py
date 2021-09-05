from globals import np, number_of_paths, ROOT_DIR
from View.parameters import board_size, length_of_random_walk, number_of_random_walks
from View.jump import draw_jump


def on_board(point):
    return np.all((point >= 0) & (point < board_size))


def get_one_step_directions():
    """where a single step can be made"""
    dx = [-1, 0, 1]
    xs, ys = np.meshgrid(dx, dx)
    d_coord = np.transpose(np.array([xs.ravel(), ys.ravel()]))
    d_coord = d_coord[(d_coord[:, 0] != 0) | (d_coord[:, 1] != 0)]
    return d_coord


def draw_walk(walk):
    for i in range(walk.shape[0] - 1):
        draw_jump(*np.ravel([walk[i], walk[i + 1]]))


def draw_random_walk():
    draw_walk(get_random_walk(path_length=length_of_random_walk))


def draw_random_walks():
    """draw several self-avoiding random walks"""
    for i in range(number_of_random_walks):
        draw_random_walk()


def draw_genetic_algorithm_walks():
    """draw walks produced by GA"""
    f = open(f"{ROOT_DIR}/resources/paths/path.csv", "r")
    for i in range(number_of_paths):
        snake_path = np.loadtxt(fname=f, delimiter=",", max_rows=2).astype(int)
        draw_walk(snake_path.T)


one_step_directions = get_one_step_directions()


def get_random_walk(path_length=100):
    path = np.zeros((path_length, 2))
    path[0] = np.random.randint(low=0, high=board_size, size=2)

    def in_path(point):
        return any(np.equal(path, point).all(1))

    def points_on_board(points):
        return np.apply_along_axis(on_board, 1, points)

    def points_not_in_path(points):
        return np.logical_not(np.apply_along_axis(in_path, 1, points))

    for step in range(path_length - 1):
        directions = path[step] + one_step_directions
        directions = directions[
            points_on_board(directions)
            & points_not_in_path(directions)
            ]
        if directions.size != 0:
            path[step + 1] = directions[np.random.randint(len(directions))]
        else:
            path = path[: step + 1]
            break
    return path.astype(int)
