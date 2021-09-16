from Avaday.config import IS_ENABLED_CALCULATIONS

def run_controller():
    if IS_ENABLED_CALCULATIONS:
        from Avaday.Model.model import run_model
        run_model()
    
    from Avaday.View.view import run_view
    run_view()

    # from Avaday.config import IMAGE_NAME, ROOT_DIR
    # from pathlib import Path
    # import pyqtgraph as pg
    # Path(f'{ROOT_DIR}/resources/output_images').mkdir(parents=True, exist_ok=True)
    # d = widget.renderToArray((1000, 1000))
    # pg.makeQImage(d).save(f'{ROOT_DIR}/resources/output_images/{IMAGE_NAME}.png')