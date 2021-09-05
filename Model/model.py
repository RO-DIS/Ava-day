from Model.ga import run_ga

from Model.top_paths import save_top_paths
from globals import enable_GA, enable_get_new_paths

def run_model():
    if enable_GA:
        run_ga()
    if enable_get_new_paths:
        save_top_paths()
