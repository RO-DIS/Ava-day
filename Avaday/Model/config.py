from Avaday.config import np, BOARD_SIZE

epochs = 7
batch_size = 5
number_of_snakes = 10

assert number_of_snakes % 2 == 0
snake_ids = np.arange(number_of_snakes)

# use n+n generation
number_of_parents = 4
number_of_kids = number_of_snakes - number_of_parents

min_weight, max_weight = -5, 5

max_visibility_distance = 5
brain_size = (max_visibility_distance * 2 + 1) * (max_visibility_distance + 1)
default_visibility_distance = 4

min_mutation, max_mutation = -5, 5
mutation_probability = 1 / 6

view_directions = 4
move_directions = 7

np.random.seed(18780293)

weights_size = brain_size * (max_visibility_distance + 1)
mutation_sample_size = int(mutation_probability * weights_size)

# batch from which the top snake's brain is selected
top_batch = 6