from Avaday.globals import IS_ENABLED_CALCULATIONS

def run_controller():
    from Avaday.Model.model import run_model
    if IS_ENABLED_CALCULATIONS:
        run_model()

    from Avaday.View.view import run_view
    run_view()