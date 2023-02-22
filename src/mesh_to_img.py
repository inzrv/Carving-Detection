import numpy as np
from draw import draw_tr

def get_triangle(vector, scale, translation):
    p1, p2, p3 = (vector + translation) * scale
    p1 = np.array(p1[:2], dtype=np.int32)
    p2 = np.array(p2[:2], dtype=np.int32)
    p3 = np.array(p3[:2], dtype=np.int32)
    tr = np.array([p1, p2, p3])
    return tr

def get_img_from_mesh(mesh, scale):
    translation = np.absolute(mesh.min_)
    w, h, _ = (mesh.max_ + translation) * scale
    img = np.zeros((int(h), int(w), 3), dtype=np.uint8)
    for i in range(mesh.vectors.shape[0]):
        tr = get_triangle(mesh.vectors[i], scale, translation)
        img = draw_tr(img, tr, (100,100,100), 1)
    return img

def get_angles_map(mesh, scale, polygon_lists):
    translation = np.absolute(mesh.min_)
    w, h, _ = (mesh.max_ + translation) * scale
    img = np.zeros((int(h), int(w), 3), dtype=np.uint8)
    for ang in polygon_lists.keys():
        b, g, r = np.random.randint(256, size=3)
        color = (int(b), int(g), int(r))
        for i in polygon_lists[ang]:
            tr = get_triangle(mesh.vectors[i], scale, translation)
            img = draw_tr(img, tr, color, 1)
    return img

def get_mask(mesh, phi, scale, polygon_lists):
    translation = np.absolute(mesh.min_)
    w, h, _ = (mesh.max_ + translation) * scale
    img = np.zeros((int(h), int(w), 1), dtype=np.uint8)
    for key in polygon_lists.keys():
        if key == phi:  
            for i in polygon_lists[key]:
                tr = get_triangle(mesh.vectors[i], scale, translation)
                img = draw_tr(img, tr, 255)
    return img