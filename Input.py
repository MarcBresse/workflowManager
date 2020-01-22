# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 11:24:04 2018

@author: laguema
"""

import os
from WorkflowManager import RelativeDay

        
class InputFile(RelativeDay):
  
    """Input File needed for process to run. Inputs are define by name, format and location."""
    def __init__(self,path,name,Inputformat,Inputdate,Pr_Date,savetime=None):
        
        RelativeDay.__init__(self,Pr_Date)
        
        self.rawname=name
        self.rawpath=path
        self.savetime=savetime
        self.Inputformat = Inputformat
        self.Inputdate= Inputdate
        self.setname()
        self.exist()
   
    def setname(self):
        
        """Define the name using a format indicator in the raw string and a register to transform these based on the ProcessDay"""
        if self.Inputdate:
            register={'Y':getattr(self, self.Inputdate).strftime("%Y"),'m':getattr(self, self.Inputdate).strftime("%m"),'d':getattr(self, self.Inputdate).strftime("%d"),'B':getattr(self, self.Inputdate).strftime("%B"),'y':getattr(self, self.Inputdate).strftime("%y")}
            self.inputname=self.rawname.format(**register)
            self.inputpath=self.rawpath.format(**register)
        else:
            self.inputname=self.rawname
            self.inputpath=self.rawpath

        
        
    def exist(self):
        
        """Return True if input exists"""
        if os.path.exists(self.inputpath):
            
            for files in os.listdir(self.inputpath):
                if files.lower().find(self.inputname.lower())!=-1 and files.split('.')[-1].lower()==self.Inputformat:
                    self.inputname=files
                    
                    return True
        return False
    

