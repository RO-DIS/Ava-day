import Avaday.Model.brain as brain
import Avaday.Model.path as path
from Avaday.Model.parameters import top_batch


def save_top_paths():
    """save some number of paths of the best snake in the batch"""
    brain.set_brains(top_batch)
    path.save_snake_paths()
