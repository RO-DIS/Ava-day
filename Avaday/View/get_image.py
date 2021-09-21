from pathlib import Path
from PIL import Image

from Avaday.View.config import IMAGE_SIDE, BOARD_SIZE, np

from Avaday.config import ROOT_DIR

def get_image(file_path):
    img = Image.open(file_path)
    w, h = img.size
    side = min(w,h)
    center_x = w//2
    center_y = h//2
    left_top_x = max(0, center_x-side//2)
    left_top_y = max(0, center_y-side//2)
    img = img.crop((left_top_x, left_top_y, left_top_x + side - 1, left_top_y + side - 1))
    img = img.resize((IMAGE_SIDE, IMAGE_SIDE), Image.ANTIALIAS)

    p = Path(file_path)
    file_name = p.stem
    Path(f"{ROOT_DIR}/resources/user_images/").mkdir(parents=True, exist_ok=True)
    
    path_to_png = f"{ROOT_DIR}/resources/user_images/{file_name}.png"
    img.save(path_to_png,bitmap_format='png')

    img = Image.open(path_to_png)
    img = np.asarray(img).astype(np.float32)

    rgb_image = np.zeros((IMAGE_SIDE, IMAGE_SIDE,3))
    print(img.shape)
    for i in range(min(3,img.shape[2])):
        rgb_image[:,:,i] = img[:,:,i]

    img = rgb_image

    factor = IMAGE_SIDE // BOARD_SIZE
    img = img[::factor][:, ::factor]
    img = img[:BOARD_SIZE, :BOARD_SIZE]

    return img