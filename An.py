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
    pass
