from Avaday.Model.ga import run_ga

from Avaday.Model.top_paths import save_top_paths
from Avaday.config import IS_ENABLED_GA, IS_ENABLED_NEW_PATHS

def run_model():
    if IS_ENABLED_GA:
        run_ga()
    if IS_ENABLED_NEW_PATHS:
        save_top_paths()
