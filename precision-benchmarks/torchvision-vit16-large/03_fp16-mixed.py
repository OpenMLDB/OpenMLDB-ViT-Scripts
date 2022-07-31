import time

import lightning as L
from lightning import Fabric
import torch
import torch.nn.functional as F
from torch.optim.lr_scheduler import ExponentialLR
import torchmetrics
from torchvision import transforms
from torchvision.models import vit_l_16
from torchvision.models import ViT_L_16_Weights

from local_utilities import get_dataloaders_c