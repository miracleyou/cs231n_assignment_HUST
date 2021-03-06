# coding: utf-8
import torch
import torch.nn as nn
import torchvision.models as models

class Config(object):
    def __init__(self):
        self.MODEL              = models.inception_v3(pretrained=True)
        self.USE_CUDA           = torch.cuda.is_available()
        self.NET_SAVE_PATH      = "./source/trained_net/"
        self.NUM_EPOCHS         = 50
        self.BATCH_SIZE         = 32
        self.TOP_NUM            = 4
        self.NUM_WORKERS        = 4
        self.NUM_CLASSES        = 374
        self.LEARNING_RATE      = 0.001 
        self.PRINT_BATCH        = True
        self.NUM_PRINT_BATCH    = 5

