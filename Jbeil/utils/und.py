import os
import numpy as np
import torch

def get_freer_gpu():
    os.system('nvidia-smi -q -d Memory |grep -A4 GPU|grep Free >tmp')
    memory_available = [int(x.split()[2]) for x in open('tmp', 'r').readlines()]
    return np.argmax(memory_available)

print(torch.cuda.is_available())
print(torch.version.cuda)
print(get_freer_gpu())