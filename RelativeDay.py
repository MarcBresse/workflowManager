# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 10:55:01 2019

@author: enrac
"""
from pandas.tseries.offsets import BDay
class RelativeDay:
    
    """Creates a set of dates relative to the reference date"""
    def __init__(self,dayref):
        
        if dayref.weekday()>4:
            
            self.SD = dayref-BDay
           
        else:
            
            self.SD=dayref
        
        self.getdates()
            
    
    def getdates(self):
        
        """position key dates relative to given date : LBD = T-1, PLBD = T-2, PPLBD = T-3, OriginWeek is last monday, OriginMonth is 1st BD of the month"""
        self.LBD = self.SD-BDay
        self.PLBD = self.SD-2*BDay
        self.PPLBD = self.SD-3*BDay
        i=0
        
        while (self.SD-i*BDay).weekday()>(self.SD-(i+1)*BDay).weekday():
            
            i+=1            
            
        self.OriginWeek = self.SD-i*BDay
       
        i=0
        while (self.SD-i*BDay).month==(self.SD-(i+1)*BDay).month:
            i+=1
        self.OriginMonth=self.SD-i*BDay
        
    
    def reversedates(self,RelativeDayStr):
        """Reverse the """
        if getattr(self,RelativeDayStr)==self.LBD:
            self.SD = self.SD + BDay
        elif getattr(self,RelativeDayStr)==self.PLBD:
            self.SD = self.SD + 2* BDay
        elif getattr(self,RelativeDayStr)==self.PPLBD:
            self.SD = self.SD + 3* BDay
            
        self.getdates()