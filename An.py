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
    for line in self.script[scene]:
      if line[:12]=="<<Boardcast:":
        print("[",line[12:(len(line)-2)],"]")
        sleep(2)
      if line[:8]=="<<Speak:":
        print(self.name,">",line[8:(len(line)-2)])
        sleep(1)
      if line[:6]=="[Jump:":
        nextscene=line[6:(len(line)-1)]
        self.status['Properties']['scene']=next
        atscene(next)
      if line=="[End]":
        self.status['Properties']['scene']="Start"
        print("[Connection Lost...]")
        sleep(5)
        atscene("Start")
      if line[:8]=="<<Sleep:":
        unit=line[-3]
        raw=line[8:(len(line)-3)]
        if unit=='s':
          sleep(raw)
        elif unit=='m':
          sleep(raw*60)
        elif unit=='h':
          sleep(raw*3600)
        else:
          sleep(raw)
      if line[:9]=="<<Choice:":
        pass
  def savestatus(self):
    path='Data/status.json'
    with open(status_file,'w') as f:
			json.dump(self.status, f)
