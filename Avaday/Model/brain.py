from Avaday.globals import ROOT_DIR, np
from Avaday.Model.parameters import max_visibility_distance, view_directions, min_weight, max_weight, brain_size, move_directions, \
    snake_ids

clockwise_turn = np.array([[0, -1], [1, 0]])
clockwise_powers = np.array(
    [np.linalg.matrix_power(clockwise_turn, i) for i in range(4)]
)
symmetric_turn = np.array([[1, 0], [0, -1]])


def get_initial_brain_coordinates():
    pos = np.array(
        np.meshgrid(
            np.arange(-max_visibility_distance, max_visibility_distance + 1),
            np.arange(0, max_visibility_distance + 1),
            indexing="ij",
        )
    )
    return np.reshape(pos, (2, pos.shape[1] * pos.shape[2]))


def get_symmetric_brain_coordinates(direction):
    pos = get_initial_brain_coordinates()
    pos = np.dot(symmetric_turn, pos)
    return np.dot(clockwise_powers[direction], pos)


def get_brain_coordinates(direction):
    pos = get_initial_brain_coordinates()
    return np.dot(clockwise_powers[direction], pos)


brain_coordinates = np.array(
    [get_brain_coordinates(direction) for direction in range(view_directions)]
)
symmetric_brain_coordinates = np.array(
    [get_symmetric_brain_coordinates(direction) for direction in range(view_directions)]
)

def set_brains(batch):
    """set the same saved brains to all population"""
    brains = np.loadtxt(
        fname=f'{ROOT_DIR}/resources/brains/{batch:03}.csv', 
        delimiter=','
        ).reshape((brain_size, move_directions))
        
    for i in snake_ids:
        snake_brains[i] = brains


def get_initial_brain_weights():
    return np.random.randint(min_weight, max_weight + 1, (brain_size, move_directions))


def get_cautiousness_coefficients():
    def chebyshev_coefficient(coordinate):
        max_coordinate = np.amax(np.abs(coordinate))
        return 1.0 - max_coordinate / (max_visibility_distance + 1)

    cautiousness = np.apply_along_axis(
        chebyshev_coefficient, 0, get_initial_brain_coordinates()
    )
    # we don't consider weights under head
    head_coordinate = (max_visibility_distance + 1) * max_visibility_distance
    cautiousness.T[head_coordinate] = 0
    # we use symmetric weights and don't want a danger to be counted twice
    cautiousness[:: max_visibility_distance + 1] /= 2
    return cautiousness


def get_cautious_brain_weights():
    cautiousness_coefficients = get_cautiousness_coefficients()
    brain_weights = get_initial_brain_weights()
    return brain_weights * cautiousness_coefficients[:, np.newaxis]

snake_brains = np.array([get_cautious_brain_weights() for snake_id in snake_ids])
