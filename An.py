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
  def savestatus(self):
    path='Data/status.json'
    with open('Data/status.js','w') as f:
      json.dump(self.status, f)
  def atscene(self,scene):
    self.status['Properties']['scene']=scene
    self.savestatus()
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
        print("[Connection Exiting...]\n")
        print("Thee End~Thanks for playing!!!")
        sleep(5)
        os._exit(0)
      if line=="[Over]":
      	print("[Connection Lost]\n")
      	sleep(2)
      	print("You Failed...")
      	sleep(3)
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
        rc=line[9:(len(line)-2)]
        a=rc.split(',')
        l=len(a)/2
        text="To choose:\n"
        for i in range(0,l):
          tp=str(i+1)+"-->"+a[i]+'\n'
          text+=tp
        inword=input(text)
        if int(inwords)>0 and int(inword)<=l:
          choice=l+lint(inwords)-1
          sleep(1)
          atscene(choice)
        else:
          print("233,error accrued!!!")
          sleep(3)
          os._exit(0)
  def Start(self):
    self.atscene("Start")

Lifeline=Tales()
Lifeline.Start()
