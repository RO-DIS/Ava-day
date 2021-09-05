def run_controller():
    from model.model import run_model

    # enable just for recalculations
    run_model()

    from view.view import run_view
    run_view()