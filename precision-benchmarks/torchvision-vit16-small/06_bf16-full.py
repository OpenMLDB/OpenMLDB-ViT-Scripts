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


def train(num_epochs, model, optimizer, train_loader, val_loader, fabric, scheduler):

    for epoch in range(num_epochs):
        train_acc = torchmetrics.Accuracy(task="multiclass", num_classes=10).to(fabric.device)

        model.train()
        for batch_idx, (features, targets) in enumerate(train_loader):
            model.train()

            ### FORWARD AND BACK PROP
            logits = model(features)
            loss = F.cross_entropy(logits, targets)
            fabric.backward(loss)

            ### UPDATE MODEL PARAMETERS
            optimizer.step()
            optimizer.zero_grad()

            ### LOGGING
            if not batch_idx % 300:
                fabric.print(f"Epoch: {epoch+1:04d}/{num_epochs:04d} | Batch {batch_idx:04d}/{len(train_loader):04d} | Loss: {loss:.4f}")

            model.eval()
            with torch.no_grad():
                predicted_labels = torch.argmax(logits, 1)
                train_acc.update(predicted_labels, targets)
        scheduler.step()

        ### MORE LOGGING
        model.eval()
        with torch.no_grad():
            val_acc = torchmetrics.Accuracy(tas