import wgconstants as wgc
import math
import numpy as np

def dirac_soliton_2D():
    step_num = round(wgc.Z_LIMIT/wgc.Z_STEP)            # number of steps
    index_taken = math.floor(step_num/wgc.FRAME_NUM)
    col_vec = np.linspace((-wgc.COL_NUM-1)/2,(wgc.COL_NUM-1)/2,wgc.COL_NUM)
    row_vec = np.linspace((-wgc.ROW_NUM-1)/2,(wgc.ROW_NUM-1)/2,wgc.ROW_NUM)
    nvec2 = np.arange(start = 1, stop = wgc.COL_NUM, step = 1)
    mvec2 = np.arange(start = 1, stop = wgc.ROW_NUM, step = 1)
    ncenter = (wgc.COL_NUM+1)/2;
    mcenter = (wgc.ROW_NUM+1)/2;
    center  = mcenter + ncenter; 
    return col_vec, row_vec, nvec2, mvec2, ncenter, mcenter, center                               

col_vec, row_vec, nvec2, mvec2, ncenter, mcenter, center = dirac_soliton_2D()