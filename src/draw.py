from matplotlib import pyplot as plt
import cv2
from mpl_toolkits import mplot3d
import numpy as np

def show_img(img, size=(18, 12)):
    fig, ax = plt.subplots()
    w, h = size
    fig.set_size_inches(w, h)
    ax.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.show()

def plot_mesh(
    your_mesh, 
    size_x=10, 
    size_y=10, 
    dpi=80, 
    filename = None
    ):
    # Create a new plot
    figure = plt.figure(figsize=(size_x, size_y), dpi=dpi)
    #axes = mplot3d.Axes3D(figure, auto_add_to_figure=False)
    axes = mplot3d.Axes3D(figure)
    axes.add_collection3d(mplot3d.art3d.Poly3DCollection(your_mesh.vectors, edgecolor="black"))
    figure.add_axes(axes)
    # Auto scale to the mesh size
    scale = your_mesh.points.flatten()
    axes.auto_scale_xyz(scale, scale, scale)
    # Show or save the plot
    if filename is None:
        plt.show()
    else:
        #matplotlib.use('Agg')
        plt.savefig(filename)

def get_rand_color():
    b,g,r = np.random.randint(0, 255, size=(3, ))
    return (int(b), int(g), int(r)) 

def draw_contours(img, contours, color='rand', thickness=1):
    for contour in contours:
        if color == 'rand':
            cv2.drawContours(img, contour, -1, get_rand_color(), thickness)
        else:
            cv2.drawContours(img, contour, -1, color, thickness)
    return img

def draw_tr(img, triangle, fill_color=(100, 100, 100), border_thickness=0, border_color=(0,0,0)):
    p1, p2, p3 = triangle
    cv2.drawContours(img, [triangle], 0, fill_color, -1)
    if border_thickness != 0:  
        cv2.line(img, p1, p2, border_color, border_thickness)
        cv2.line(img, p2, p3, border_color, border_thickness)
        cv2.line(img, p1, p3, border_color, border_thickness)
    return img 

nice_white= (245, 245, 245)
nice_red = (60, 20, 220)
nice_blue = (225, 105, 65)
nice_green = (50, 205, 154)
nice_pink = (147, 20, 255)