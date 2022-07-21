# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 06:40:57 2022

@author: Slipknot
"""

import torch
import torch.nn as nn
import torch.nn.functional as F

class NGram(nn.Module):
    def __init__(self, vocab_size, embedding_dim, context_size):
        super(NGram, self).__init__()
        self.embedding_dim = embedding_dim
        self.vocab_size = vocab_size
        self.context_size = context_size
        self.embedding_dim = nn.Embedding(vocab_size, embedding_dim)
        self.fc1 = nn.Linear(context_size * embedding_dim, 128)
        self.fc2 = nn.Linear(128, vocab_size)
        
    def forward(self, x):
        embeds = self.embedding_dim(x).view(1, -1)
        out = F.relu(self.fc1(embeds))
        out = self.fc2(out)
        log_prob = F.log_softmax(out, dim = 1)
        return log_prob