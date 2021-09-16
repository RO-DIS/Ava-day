def run_controller():
    from Avaday.View.view import run_view
    run_view()

    # from Avaday.config import IMAGE_NAME, ROOT_DIR
    # from pathlib import Path
    # import pyqtgraph as pg
    # Path(f'{ROOT_DIR}/resources/output_images').mkdir(parents=True, exist_ok=True)
    # d = widget.renderToArray((1000, 1000))
    # pg.makeQImage(d).save(f'{ROOT_DIR}/resources/output_images/{IMAGE_NAME}.png')