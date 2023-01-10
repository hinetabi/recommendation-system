import torch.nn as nn
import torch


class recModule(nn.Module):
    def __init__(self):
        self.linear = nn.Linear()

        return 0

    def forward(self, x):
        x = self.linear(x)
