import wgconstants as wgc
import math
import numpy as np
import plotly.graph_objects as go

def dirac_soliton_2D():
#    step_num = round(wgc.Z_LIMIT/wgc.Z_STEP)                                                # number of steps
#    index_taken = math.floor(step_num/wgc.FRAME_NUM)
    col_vec = np.linspace((-wgc.COL_NUM - 1) / 2, (wgc.COL_NUM - 1) / 2, wgc.COL_NUM)
    row_vec = np.linspace((-wgc.ROW_NUM - 1)/ 2, (wgc.ROW_NUM -1 ) / 2, wgc.ROW_NUM)
    nvec2 = np.arange(start = 1, stop = wgc.COL_NUM, step = 1)
    mvec2 = np.arange(start = 1, stop = wgc.ROW_NUM, step = 1)
    ncenter = (wgc.COL_NUM + 1) / 2;
    mcenter = (wgc.ROW_NUM + 1) / 2;
    center  = mcenter + ncenter; 
    
    # Calculate Dirac Soliton 
    coeff_1 = 2 * wgc.COUPLING_COEF_1 / wgc.BEAMWIDTH / math.sqrt(abs(wgc.SIGMA * wgc.GAMMA))
    coeff_2 = 2 * math.pow(wgc.COUPLING_COEF_1, 2) / math.pow(wgc.BEAMWIDTH, 2) / wgc.SIGMA / math.sqrt(abs(wgc.SIGMA * wgc.GAMMA))
    
    a_n = np.zeros(len(nvec2), dtype = np.complex128)
    for x in range(1, round((wgc.COL_NUM - 1) / 2)):
        a_n[2 * x - 1] = 1j ** (2 * x) * coeff_1 / math.cosh((nvec2[2 * x - 1] - ncenter) / wgc.BEAMWIDTH)
        a_n[2 * x] = 1j ** (2 * x) * coeff_2 / math.cosh((nvec2[2 * x] - ncenter) / wgc.BEAMWIDTH) * math.tanh((nvec2[2 * x] - ncenter) / wgc.BEAMWIDTH)
    
    a_n[wgc.COL_NUM] = 1j ** (wgc.COL_NUM + 1) * coeff_1 / math.cosh((nvec2[wgc.COL_NUM] - ncenter) / wgc.BEAMWIDTH);
    
    a_m = np.zeros(len(mvec2), dtype = np.complex128)
    for x in range(1, round((wgc.ROW_NUM - 1) / 2)):
        a_m[2 * x - 1] = 1j ** (2 * x) * coeff_1 / math.cosh((mvec2[2 * x - 1] - ncenter) / wgc.BEAMWIDTH)
        a_m[2 * x] = 1j ** (2 * x) * coeff_2 / math.cosh((mvec2[2 * x] - ncenter) / wgc.BEAMWIDTH) * math.tanh((mvec2[2 * x] - ncenter) / wgc.BEAMWIDTH)
    
    a_m[wgc.ROW_NUM] = 1j ** (wgc.ROW_NUM + 1) * coeff_1 / math.cosh((mvec2[wgc.ROW_NUM] - ncenter) / wgc.BEAMWIDTH);
    
    return col_vec, row_vec, nvec2, mvec2, ncenter, mcenter, center, coeff_1, coeff_2, a_n                               

col_vec, row_vec, nvec2, mvec2, ncenter, mcenter, center, coeff_1, coeff_2, a_n = dirac_soliton_2D()

fig = go.Figure()
fig.add_trace(go.Scatter(x = nvec2, y = abs(a_n.real)))
fig.write_html("s.html",auto_open=True)

