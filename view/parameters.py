# resolution <= 512
board_size = 100
# maximum height of points
board_height = 20
# size of dots
dot_size = 1
# maximum initial speed
shortest_jump = True
# range for jump heights
max_jump_height = 30
# adding speed to make jumps lower
min_speed_boost, max_speed_boost = 5, 6
# show dots
are_visible_dots = True
# width of lines on path
line_width = 3
# for picture dots
dot_opaqueness = 1.0
number_of_random_walks = 50
length_of_random_walk = 400
# resolution of jump
time_frames_in_jump = 2
# time delay between drawing lines
line_delay = 0

# distance from origin for viewing pictures
view_height, elevation, azimuth = 125, 90, 0

# 125, 30, -30
# 125, 40, 180

# to watch how path emerges
real_time_path_drawing_enabled = False

# shift all points by this amount
default_shift = board_size // 2

# constants

# gravitational acceleration
g = 9.81
# mass
mass = 3
# side of image
image_side = 512

from globals.globals import np
from main import image_name

# derived constants

# maximum initial speed of jump
max_initial_speed = np.sqrt(2 * g * max_jump_height)
# path to image for map

path_to_image = f"./resources/images/{image_name}.png"

background_color = 'k'

window_height = 700
window_width = 700