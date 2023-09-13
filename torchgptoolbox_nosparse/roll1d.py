import torch 

def roll1d(x, n):  
    """
    roll the 1d array by n element, put last n num to front
    """
    return torch.cat((x[-n:], x[:-n]))