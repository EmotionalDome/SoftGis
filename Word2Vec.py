# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 06:46:38 2022

@author: Slipknot
"""

import torch
import torch.nn as nn
import torch.nn.functional as F

class Word2Vec(nn.Module):
    def __init__(self, embedding_size, vocab_size):
        super(Word2Vec, self).__init__()
        self.embedding_size = embedding_size
        self.vocab_size 
        self.embeddings = nn.Embedding(vocab_size, embedding_size)
        self.fc = nn.Linear(embedding_size, vocab_size)
        
    def forward(self, x):
        embeds = self.embeddings(x)
        hidden = self.linear(embeds)
        out = F.log_softmax(hidden)
        return out 