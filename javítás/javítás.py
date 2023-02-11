# henger magassága és a sugara bekérése, felszínt és térfogatát kiíratni.
# henger térfogat: V=pí * r2 * m
# henger felszín: F= 2*pí*r(r+m)

import math
class henger:
    def __init__(self, m, r):
        self.m=m
        self.r=r
    def SetMagassaga(self, m):
        self.m=m
    def SetSugara(self,r):
        self.r=r
    def GetMagassag(self):
        return self.m
    def GetSugara(self):
        return self.r
    
    def felszine(self):
        return 2*self.r**2*math.pi+2*self.r*math.pi*self.m
    def terfogata(self):
        return self.r**2*math.pi*self.m
    
hh = henger(5,10)
print(hh.felszine())
print(hh.terfogata())