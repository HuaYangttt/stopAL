"""
Author: Hua Yang
Email: yanghuattt@gmail.com
Date: 10/09/2024
Description: Pipeline for training/evaluating.
"""

import os
import sys
import numpy as np
import random
from tqdm import tqdm
from dataset import get_dataset, get_dataloader




# set seed
def set_seed(seed):
    random.seed(seed)  # Set seed for random
    np.random.seed(seed)  # Set seed for numpy
    # torch.manual_seed(seed)  # Set seed for PyTorch (CPU)
    # torch.cuda.manual_seed(seed)  # Set seed for PyTorch (CUDA)
    # torch.cuda.manual_seed_all(seed)  # If you are using multi-GPU
    # torch.backends.cudnn.deterministic = True  # Ensures deterministic behavior
    # torch.backends.cudnn.benchmark = False  # For reproducibility, turn off




if __name__ == '__main__':
