import numpy as np
import sys

def findIdx(F, VIdx):
    '''
    FINDIDX finds desired indices in the ndarray, like F is row * col, and 
    each element in F has index like 0, 1, 2..., want to find out the row & col 
    index of an element

    Inputs:
    F: |F|-by-dim numpy ndarray 
    VIdx: a list of indices

    Output:
    r, c: row/colummn indices in the ndarray
    '''
    mask = np.in1d(F.flatten(),VIdx)
    try:
        nDim = F.shape[1]
    except:
        nDim = 1
    r = np.floor(np.where(mask)[0] / (nDim*1.0) ).astype(int)
    c = np.where(mask)[0] % nDim
    return r,c