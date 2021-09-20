from pathlib import Path
from PIL import Image

from Avaday.View.config import IMAGE_SIDE, BOARD_SIZE, np

from Avaday.config import ROOT_DIR

def get_image(file_path):
    img = Image.open(file_path)
    # w, h = img.size
    side = min(img.size)
    img = img.crop((0, 0, side, side))
    img = img.resize((IMAGE_SIDE, IMAGE_SIDE), Image.ANTIALIAS)

    p = Path(file_path)
    file_name = p.stem
    Path(f"{ROOT_DIR}/resources/user_images/").mkdir(parents=True, exist_ok=True)
    
    path_to_png = f"{ROOT_DIR}/resources/user_images/{file_name}.png"
    img.save(path_to_png)

    img = Image.open(f"{ROOT_DIR}/resources/user_images/{file_name}.png")
    img = np.asarray(img).astype(np.float32)

    factor = IMAGE_SIDE // BOARD_SIZE
    img = img[::factor][:, ::factor]
    img = img[:BOARD_SIZE, :BOARD_SIZE]

    return img



