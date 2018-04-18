# coding: utf-8
import torch
import torch.nn as nn
from models import vgg, googlenet, densenet, inception_v3

class Config(object):
    def __init__(self):
        self.MODEL              = inception_v3.Inception3(374)#googlenet.GoogLeNet()#vgg.VGG('VGG19')#densenet.DenseNet121()#vgg.VGG('VGG19')#googlenet.GoogLeNet()#vgg.VGG('VGG19')
        self.USE_CUDA           = torch.cuda.is_available()
        self.NET_SAVE_PATH      = "./source/trained_net/"
        self.NUM_EPOCHS         = 50
        self.BATCH_SIZE         = 8
        self.TOP_NUM            = 4
        self.NUM_WORKERS        = 4
        self.NUM_CLASSES        = 374
        self.LEARNING_RATE      = 0.001 
        self.PRINT_BATCH        = True
        self.NUM_PRINT_BATCH    = 5

