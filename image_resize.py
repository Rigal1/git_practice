from PIL import Image

def get_trans_image_upper_body(image, x_min, x_max, y_min, y_max, image_resize_param):
    width = x_max - x_min
    height = y_max - y_min
    x_max += width * image_resize_param
    x_min -= width * image_resize_param
    y_max += height * 1.3
    y_min -= height * 0.3

    if x_max > image.shape[1]:
        x_max = image.shape[1]
    if x_min < 0:
        x_min = 0
    if y_max > image.shape[0]:
        y_max = image.shape[0]
    if y_min < 0:
        y_min = 0

    x_min, x_max, y_min, y_max = int(x_min), int(x_max), int(y_min), int(y_max)
    return x_min, x_max, y_min, y_max

def get_trans_image_face(image, x_min, x_max, y_min, y_max, image_resize_param):
    width = x_max - x_min
    height = y_max - y_min
    x_max += width * image_resize_param
    x_min -= width * image_resize_param
    y_max += height * image_resize_param
    y_min -= height * image_resize_param

    if x_max > image.shape[1]:
        x_max = image.shape[1]
    if x_min < 0:
        x_min = 0
    if y_max > image.shape[0]:
        y_max = image.shape[0]
    if y_min < 0:
        y_min = 0

    x_min, x_max, y_min, y_max = int(x_min), int(x_max), int(y_min), int(y_max)
    return x_min, x_max, y_min, y_max

def get_trans_image_mugshot(image, x_min, x_max, y_min, y_max, image_resize_param):
    width = x_max - x_min
    height = y_max - y_min
    x_max += width * image_resize_param
    x_min -= width * image_resize_param
    y_max += height * 0.7
    y_min -= height * 0.3

    if x_max > image.shape[1]:
        x_max = image.shape[1]
    if x_min < 0:
        x_min = 0
    if y_max > image.shape[0]:
        y_max = image.shape[0]
    if y_min < 0:
        y_min = 0

    x_min, x_max, y_min, y_max = int(x_min), int(x_max), int(y_min), int(y_max)
    return x_min, x_max, y_min, y_max

def make_square_image(image, xmax, xmin, ymax, ymin, png_flag):
    width = xmax - xmin
    height = ymax - ymin
    if width > height:
        # print("continue")
        return -1
    
    cut_image = resize_square_image(image,xmin, ymin, width, height, png_flag)
    return cut_image

def resize_square_image(image, xmin, ymin, width, height, png_flag):
    get_image = image.copy()
    if png_flag:
        get_image.putalpha(255)
    square_edge = height
    # print(width, height)
    paste_x = ((square_edge - width) // 2) - xmin
    paste_y = -ymin
    if png_flag:
        square_back_image = Image.new("RGBA", (square_edge, square_edge), (255, 255, 255, 255))
    else:
        square_back_image = Image.new("RGB", (square_edge, square_edge), (255, 255, 255))
    # print(paste_x, paste_y)
    square_back_image.paste(get_image, (paste_x, paste_y))
    return square_back_image

"""

def make_square_image_old(image, xmax, xmin, ymax, ymin):
    width = xmax - xmin
    height = ymax - ymin
    #print(width, height)
    resize_long_width_mode = True if width > height else False
    cut_image = resize_square_image_old(image, xmin, ymin, width, height, resize_long_width_mode)
    return cut_image

def resize_square_image_old(image, xmin, ymin, width, height, mode):
    # square_edge, paste_x, paste_y = 0, 0, 0
    get_image = image.copy()
    if png_flag:
        get_image.putalpha(255)
    if mode:
        square_edge = width
        paste_x = -xmin
        paste_y = (square_edge - height) - ymin
    else:
        square_edge = height
        paste_x = ((square_edge - width) // 2) - xmin
        paste_y = -ymin
    
    if png_flag:
        square_back_image = Image.new("RGBA", (square_edge, square_edge), (255, 255, 255, 255))
    else:
        square_back_image = Image.new("RGB", (square_edge, square_edge), (255, 255, 255))
    print(paste_x, paste_y)
    #print(square_back_image.size)
    square_back_image.paste(get_image, (paste_x, paste_y))
    return square_back_image

def cv2pil(image):
    new_image = image.copy()
    if new_image.ndim == 2:
        pass
    elif new_image.shape[2] == 3:
        new_image = cv2.cvtColor(new_image, cv2.COLOR_BGR2RGB)
    elif new_image.shape[3] == 4:
        new_image = cv2.cvtColor(new_image, cv2.COLOR_BGRA2RGBA)
    new_image = Image.fromarray(new_image)
    return new_image

"""