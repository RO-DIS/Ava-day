import Avaday.Model.board

import Avaday.Model.brain
snake_brains = Avaday.Model.brain.snake_brains

from Avaday.Model.parameters import batch_size, number_of_snakes, snake_ids, number_of_parents, number_of_kids, brain_size, \
    weights_size, mutation_sample_size, min_mutation, max_mutation, epochs
from Avaday.globals import ROOT_DIR, np
from Avaday.Model.path import get_snake_path_length
from pathlib import Path


def run_snakes(iteration):
    """runs snakes once and saves brains of the top snake from each batch
    putting path length into file name"""

    Avaday.Model.board.field = Avaday.Model.board.clear_field()

    top_lengths = crossover()

    Path(f"{ROOT_DIR}/resources/brains").mkdir(parents=True,exist_ok=True)
    if (iteration + 1) % batch_size == 0:
        print(f"{iteration // batch_size}) {top_lengths}")
        save_brains(iteration // batch_size)

    mutation()


def get_parents():
    """calculate pairs for crossover and select the best snakes"""
    path_lengths = np.zeros(number_of_snakes).astype(int)
    for snake in snake_ids:
        path_lengths[snake] = get_snake_path_length(snake)

    top_snakes = np.argsort(-path_lengths)[:number_of_parents]
    top_lengths = path_lengths[top_snakes]

    crossover_probabilities = top_lengths / np.sum(top_lengths)
    pairs = np.random.choice(
        a=top_snakes, p=crossover_probabilities, size=(2, number_of_kids)
    )

    return pairs, top_snakes, top_lengths


def save_brains(batch):
    """save the best snake's brains"""
    np.savetxt(
        fname=f"{ROOT_DIR}/resources/brains/{batch:03}.csv",
        X=snake_brains[0],
        fmt="%.3f",
        delimiter=",",
    )


def crossover():
    """performs crossover on selected snakes"""
    parents, top_snakes, top_lengths = get_parents()

    # move parents' brains to the left
    snake_brains[:number_of_parents] = snake_brains[top_snakes]

    for index, [pa, ma] in enumerate(parents.T):
        swap_genes(pa, ma, index)

    return top_lengths


def swap_genes(pa, ma, parents_index):
    target_snake = parents_index + number_of_parents
    point = np.random.randint(0, brain_size)
    snake_brains[target_snake][point:] = snake_brains[pa][point:]
    snake_brains[target_snake][:point] = snake_brains[ma][:point]


def mutation():
    """performs mutations on all snakes"""
    for snake in snake_ids:
        mutation_indices = np.random.randint(
            low=0, high=weights_size, size=mutation_sample_size
        )
        mutation_values = np.random.randint(
            low=min_mutation, high=max_mutation + 1, size=mutation_sample_size
        )
        cautious_mutation_values = mutation_values * Avaday.Model.brain.get_cautiousness_coefficients()
        snake_brains[snake].ravel()[mutation_indices] += cautious_mutation_values


def run_ga():
    for i in range(epochs * batch_size):
        run_snakes(i)
