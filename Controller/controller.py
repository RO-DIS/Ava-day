from globals import enable_calculations

def run_controller():
    from Model.model import run_model
    if enable_calculations:
        run_model()

    from View.view import run_view
    run_view()