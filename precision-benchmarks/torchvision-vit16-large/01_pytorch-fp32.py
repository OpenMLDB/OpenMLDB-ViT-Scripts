import time

import torch
import torch.nn.functional as F
from torch.optim.lr_scheduler import ExponentialLR
import torchmetrics
from torchvision import transforms
from torchvision.models import vit_l_16
from torchvision.models import ViT_L_16_Weights

from local_u