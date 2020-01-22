# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 11:14:42 2018

@author: laguema
"""

import win32com.client as win32
import win32process
import pythoncom
import json
import pandas as pd
import importlib
import sys
import logging
import psutil
import time
from WorkflowManager import (OutputFile,InputFile,LogFile,processfile)

#Creates the log file and sets its format

FORMAT='\n\n%(asctime)s - %(name)s - %(levelname)s - %(message)s'
Formatter=logging.Formatter(FORMAT)
handle=logging.FileHandler(LogFile)
handle.setFormatter(Formatter)
handle.setLevel(logging.DEBUG)
log =logging.getLogger()
log.addHandler(handle)
log.setLevel(logging.DEBUG)


#Defines a process and get information from OutputFile class about it's status and from InputFile the 
#availability of inputs

class Process(OutputFile,InputFile):
    
    """
    Process define by it's triggers and location of its  code. path=string, name = string,
    Pr_Date is reference date of the scheduler
    inputs is a list of dictionaries, with Input object attributes as keys
    freq can be "d" "w" or "m"
    RelativeDayStr defines the relative date to Pr_Date at which process is to be run
        
    """
    def __init__(self,path,name,Pr_Date=pd.to_datetime('today'),inputs=[],Desk='FundOver',RelativeDayStr='LBD',Frequency = None,Continuous = False,Language='Python',hour=0):
        self.path = path
        self.name = name
        self.hour = hour
        self.inputs = inputs
        self.Desk = Desk
        self.Pr_Date=Pr_Date
        self.Language = Language
        self.Continuous = Continuous
        self.RelativeDayStr=RelativeDayStr
        self.Frequency = Frequency
        OutputFile.__init__(self,Pr_Date=self.Pr_Date,processname=self.name,Desk=self.Desk,RelativeDayStr=self.RelativeDayStr)
    
    def __eq__(self, other): 
        if not isinstance(other, Process):
            # don't attempt to compare against unrelated types
            return NotImplemented

        return self.name == other.name and self.Pr_Date == other.Pr_Date
    
    def __hash__(self):
        # necessary for instances to behave sanely in dicts and sets.
        return hash((self.name, self.Pr_Date))
    
    def CreateNew(self):
        """To create a new process (appends process list)"""
        
        with open(processfile) as f:
            
            data = json.load(f)
            
        for Desk in data['Desk']:
       
            if Desk['Name']==self.Desk:
      
                for Process in Desk['Process']:
                    #Checks if process name is already used (cannot have duplicate names)
                    if Process['Name']==self.name and Process['RelativeDayStr']==self.RelativeDayStr:
                  
                        print('Error trying to add new process, name already used')
                        sys.exit() 
                        
                Inputs=[]
                    #Records all input attributes in a dictionnary
                for i in self.inputs:
                    
                    InputFile.__init__(self,i['Path'],i['Name'],i['Format'],i['Date'],self.Pr_Date)
                    Inputs.append({'Path':self.rawpath,'Name':self.rawname,'SaveTime':self.savetime,'Format':self.Inputformat,'Date':self.Inputdate})
                
                    
                Desk['Process'].append({'Path': self.path,'Name': self.name,'Hour': self.hour,'Inputs':Inputs,'RelativeDayStr':self.RelativeDayStr,'Frequency':self.Frequency,'Continuous':self.Continuous,'Language':self.Language})  

                    
                   
           #Saves the appended file     
        with open(processFile,'w') as outfile:
            
            json.dump(data,outfile,indent=4,separators=(',', ': '))
            
    def RemoveProcess(self):
        
        """To remove a process"""
        
        with open(processFile) as f:
            
            data = json.load(f)
            
        for Desk in data['Desk']:
            
            if Desk['Name']==self.Desk:    
                
                for num,process in enumerate(Desk['Process']):
                    
                    if process['Name']==self.name:
                        
                        Desk['Process'].pop(num)  
                        print(self.name)
                        
        with open(processFile,'w') as outfile:
            
            json.dump(data,outfile,indent=4,separators=(',', ': '))
            
    def Conditions(self):
        
        """Checks if the conditions are filled to start"""
        #alreay ran?For Continuous process we don't care about last status
        if self.Continuous==False:
            
            if self.GetResults()[1]!= None:
                
                if self.Frequency==None:
                    return False
                elif self.Frequency > pd.Timestamp.now().hour-pd.to_datetime(self.GetResults()[2]).hour:
                    return False
                    
                
       #Minimum time of day to run?
        if self.hour > pd.Timestamp.now().hour:
   
            return('Time constraint')
            
       
        #Is there missing inputs?
        for input in self.inputs:
            
            InputFile.__init__(self,input['Path'],input['Name'],input['Format'],input['Date'],self.Pr_Date)
            
            #Calls method from InputFile class
            if not self.exist():
                
                if self.Continuous==False:
                    
                    return(f'Missing input {self.inputname}')
                    
                else:
                    
                    return False

        #If all conditions are met  
        return True
        
    def run(self):
        """Run the process"""
        #if try fails it means an error occured during the run of the process
        try:
            if self.Language == 'Python':
                #Triggers a python process
                sys.path.insert(0,self.path)
                
                #Imports file containing code
                mod = importlib.import_module(self.name)
                mod = importlib.reload(mod)
                #Run the code pushing the process date
                getattr(mod,self.name)(getattr(self,self.RelativeDayStr))
                
            elif self.Language=='VBA':
                #if code is excel, create excel instance, load the file and run VBA with process date input
                pythoncom.CoInitialize()
                xl = win32.DispatchEx("Excel.Application")
                t, pid = win32process.GetWindowThreadProcessId(xl.Hwnd)
                xl.Workbooks.Open(Filename=self.path + self.name + '.xlsm')
                xl.Application.Run(self.name +'.xlsm!' +self.name + '.' + self.name,getattr(self,self.RelativeDayStr).strftime('%x %X'))
                psutil.Process(pid).kill()
                time.sleep(10)
            
            return 'Successfully completed'
        
        except Exception as err:
              
            log.debug(f'{err} in {self.name}')
            return err
            
      
  