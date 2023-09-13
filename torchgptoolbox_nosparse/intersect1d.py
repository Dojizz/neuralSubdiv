import torch 

def intersect1d(tensor1, tensor2):
    '''
    intersect1d return intersected elements between tensor1 and tensor2
    return 1d array
    '''
    aux = torch.cat((tensor1, tensor2),dim=0)
    aux = aux.sort()[0]
    return aux[:-1][(aux[1:] == aux[:-1]).data]