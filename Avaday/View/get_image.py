from pathlib import Path
from PIL import Image

from Avaday.View.config import IMAGE_SIDE, BOARD_SIZE, np

from Avaday.config import ROOT_DIR

def get_cropped_rgb_image_path(path):
    img = Image.open(path).convert('RGB')
    w, h = img.size
    side = min(w,h)
    center_x = w//2
    center_y = h//2
    left_top_x = max(0, center_x-side//2)
    left_top_y = max(0, center_y-side//2)
    img = img.crop((left_top_x, left_top_y, left_top_x + side - 1, left_top_y + side - 1))
    img = img.resize((IMAGE_SIDE, IMAGE_SIDE), Image.ANTIALIAS)

    p = Path(path)
    file_name = p.stem
    Path(f"{ROOT_DIR}/resources/user_images/").mkdir(parents=True, exist_ok=True)
    
    path_to_png = f"{ROOT_DIR}/resources/user_images/{file_name}.png"
    img.save(path_to_png,bitmap_format='png')
    
    return path_to_png


def get_scaled_down_image(path):
    img = Image.open(path).convert('RGB')
    img = np.asarray(img).astype(np.float32)

    factor = IMAGE_SIDE // BOARD_SIZE
    img = img[::factor][:, ::factor]
    img = img[:BOARD_SIZE, :BOARD_SIZE]

    return img