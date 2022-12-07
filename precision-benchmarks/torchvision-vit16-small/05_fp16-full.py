import time

import lightning as L
from lightning import Fabric
import torch
import torch.nn.functional as F
from torch.optim.lr_scheduler import ExponentialLR
import torchmetrics
from torchvision import transforms
from torchvision.models import vit_b_16
from torchvision.models import ViT_B_16_Weights

from local_utilities import get_dataloaders_cifar10


def train(num_epochs, m