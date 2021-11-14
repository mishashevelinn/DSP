def get_segment(img, xy, shape):
    return img[xy[0]:xy[shape[0]], xy[1]:xy[1] + shape[1]]
