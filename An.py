#!/usr/bin/env python
# coding: utf-8
import os
import json
from time import sleep
import sys   
sys.setrecursionlimit(100000000)
class Tales(object):
  def __init__(self):
    self.status={}
    self.player="SD"
    self.loadstatus()
    self.name="Taylor"
    self.loadscript()
  def loadscript(self):
    path='Data/Tale.json'
    with open(path,'r') as f:
      self.script=json.load(f)
  def loadstatus(self):
    path='Data/status.json'
    if os.path.exists(path):
      with open(path,'r') as f:
        self.status=json.load(f)
    else:
      self.status={'Properties':{'scene':'Start'}}
  def atscene(self,scene):
    pass
