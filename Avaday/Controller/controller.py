from Avaday.config import IS_ENABLED_CALCULATIONS

def run_controller():
    if IS_ENABLED_CALCULATIONS:
        from Avaday.Model.model import run_model
        run_model()
    
    from Avaday.View.view import run_view
    run_view()