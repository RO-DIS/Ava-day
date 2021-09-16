# resolution <= 512
BOARD_SIZE = 100
# maximum height of points
board_height = 20
# size of dots
dot_size = 1
# maximum initial speed
shortest_jump = True
# range for jump heights
max_jump_height = 30
# adding speed to make jumps lower
MINIMAL_SPEED_BOOST, MAXIMAL_SPEED_BOOST = 5, 6
# show dots?
IS_VISIBLE_DOTS = False
# show walks?
IS_VISIBLE_WALKS = True
# width of lines on path
LINE_WIDTH = 3
# for picture dots
dot_opaqueness = 1.0
number_of_random_walks = 50
length_of_random_walk = 400
# resolution of jump
time_frames_in_jump = 2
# time delay between drawing lines
line_delay = 0

# distance from origin for viewing pictures
view_height, elevation, azimuth = 110, 90, 0
# 125, 30, -30
# 125, 40, 180

# to watch how path emerges
real_time_path_drawing_enabled = False

# shift all points by this amount
default_shift = BOARD_SIZE // 2

# constants

# gravitational acceleration
g = 9.81
# mass
mass = 3
# side of image
image_side = 512

background_color = 'k'

window_height = 700
window_width = 700

# derived constants

# maximum initial speed of jump

from Avaday.config import ROOT_DIR, np, IMAGE_NAME

# path to image for map
path_to_image = f"{ROOT_DIR}/resources/images/{IMAGE_NAME}.png"

max_initial_speed = np.sqrt(2 * g * max_jump_height)