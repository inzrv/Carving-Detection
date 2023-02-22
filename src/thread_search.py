import numpy as np
import cv2

def unit_vector(vector):
  return vector / np.linalg.norm(vector)

def angle_between(v1, v2):
  v1_u = unit_vector(v1)
  v2_u = unit_vector(v2)
  return np.arccos(np.clip(np.dot(v1_u, v2_u), -1.0, 1.0))

def get_angles(mesh, rot_axis):
    angles = np.zeros(mesh.normals.shape[0], dtype=np.float32)
    for i in range(mesh.normals.shape[0]):
        normal = mesh.normals[i]
        ang = angle_between(rot_axis, normal)
        angles[i] = np.rad2deg(ang)
    return angles 

def make_polygon_lists(angles):
    polygon_lists = {}
    for i in range(angles.shape[0]):
        ang_int = round(angles[i])
        if polygon_lists.get(ang_int) == None:
            polygon_lists[ang_int] = []
        polygon_lists[ang_int].append(i)
    return polygon_lists

def is_similar(contour_1, contour_2, d_w = 20, d_h = 20):
    _,_,w_1,h_1 = cv2.boundingRect(contour_1)
    _,_,w_2,h_2 = cv2.boundingRect(contour_2)
    return abs(w_1 - w_2) < d_w and abs(h_1 - h_2) < d_h

def find_good_contours(contours, min_size):
    good_contours = []
    for comparable_contour in contours:
        counter = 0
        for contour in contours:
            if is_similar(comparable_contour, contour):
                counter+=1
        if counter >= min_size:
            good_contours.append(comparable_contour)
    return good_contours

def find_contours_on_masks(binary_masks, min_size):
    contours_on_masks = []
    for mask in binary_masks:
        contours, _ = cv2.findContours(mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
        if len(contours) >= min_size:
            contours_on_masks.append(contours)
    return contours_on_masks

def find_thread_contours(contours_on_masks, min_size):
    thread_contours = []
    for contours in contours_on_masks:
        good_contours = find_good_contours(contours, min_size)
        thread_contours.append(good_contours)
    return thread_contours

def find_thread_bounds(thread_contours, start, end):
    thread_start = start
    thread_end = end
    for cnts in thread_contours:
        for contour in cnts:
            x,y,w,h = cv2.boundingRect(contour)
            thread_start = min(thread_start, y)
            thread_end = max(thread_end, y + h)
    return (thread_start, thread_end)


