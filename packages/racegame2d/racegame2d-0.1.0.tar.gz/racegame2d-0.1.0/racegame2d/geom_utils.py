import numpy as np



def get_line_intersection(line0_arr, line1):
    '''
    Given two arrays, check all N line intersections
    of the first array with the line given by the second array.
    '''
    x1_arr = line0_arr[:, 0]
    y1_arr = line0_arr[:, 1]
    x2_arr = line0_arr[:, 2]
    y2_arr = line0_arr[:, 3]
    #
    x3 = line1[0]
    y3 = line1[1]
    x4 = line1[2]
    y4 = line1[3]
    # get the line intersection, t_values
    t_num = (x1_arr - x3) * (y3 - y4) - (y1_arr - y3) * (x3 - x4)
    t_dnum= (x1_arr - x2_arr) * (y3 - y4) - (y1_arr - y2_arr) * (x3 - x4)
    t_arr = t_num / t_dnum
    # get the line intersection, u_values
    u_num = (x1_arr - x3) * (y1_arr - y2_arr) - (y1_arr - y3) * (x1_arr - x2_arr)
    u_dnum= (x1_arr - x2_arr) * (y3 - y4) - (y1_arr - y2_arr) * (x3 - x4)
    u_arr = u_num / u_dnum
    t_cond = np.logical_and(t_arr>= 0.0, t_arr<= 1.0)
    u_cond = np.logical_and(u_arr>=0.0, u_arr<=1.0)
    return t_cond * u_cond


def quad_edge_intersection(quad0_arr, quad1):
    '''
    Check the edge intersection of two quads.
    '''
    # 
    pass

def quad_intersection(quad0_arr, quad1):
    '''
    Compute whether two quads intersect.
    quad0_arr = [(x0, y0, x1, y1, x2, y2, x3, y3), ..., (<len 8>)] in R^{Nx8}
    quad1 = (x0, y0, x1, y1, x2, y2, x3, y3)
    '''
    #
    pass
