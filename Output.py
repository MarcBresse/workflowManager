# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 11:33:14 2018

@author: laguema
"""
from WorkflowManager import (RelativeDay,LogFile,outputFile,backupfile)
import json
import shutil



class Output(RelativeDay):
    """Generates and defines the log of process completion. Also allows to retrieve log. Logs are 
    structured per day per process name."""
    def __init__(self,Pr_Date,processname,RelativeDayStr,Desk):
        self.Pr_Date = Pr_Date
        self.Desk=Desk
        RelativeDay.__init__(self,Pr_Date)
       
        self.DateRef=getattr(self,RelativeDayStr)
        self.processname = processname
    
    def __eq__(self, other): 
        if not isinstance(other, Output):
            # don't attempt to compare against unrelated types
            return NotImplemented
        #Definition of a unique log is based on process name and date
        return self.processname == other.processname and self.DateRef == other.DateRef
    
    def __hash__(self):
        # necessary for instances to behave sanely in dicts and sets.
        return hash((self.processname, self.DateRef))
    
                
    def GenerateResult(self,Result,tb=None,TS = None):
        #Try statement to handle corrupt output file
        try:
            """Record the result of the run"""
            with open(outputFile) as f:
                self.Output = json.load(f)
            
            for Desk in self.Output['Desk']:
                #sort entries by date and retain only 40 in the log
                Desk['Results'] = sorted(Desk['Results'],key = lambda x: x['Date'])[-40:]
                
                if Desk['Name']==self.Desk:
                        
                    for Results in Desk['Results']:
                        
                        if Results['Date']==self.DateRef.strftime("%Y-%m-%d"):
                        
                            if not any(map(lambda x:True if self.processname==x['Name'] else False,Results['Process'])):  
                    
                                Results['Process'].append({'Name':self.processname})
                                Results['Process'][-1]['Result']='Not Run'
                                Results['Process'][-1]['Traceback']=None
                                Results['Process'][-1]['TimeStamp']=None
                                
                            for Pro in Results['Process']:
                                
                                if Pro['Name']==self.processname:
                                    
                                    Pro['Result']=Result
                                    Pro['Traceback']=tb
                                    Pro['TimeStamp']=TS
                                   
            with open(outputFile,'w') as outfile:
                
                json.dump(self.Output,outfile,indent=4,separators=(',', ': '))
                
            return 
        
        except:
            #Use back up file if output is corrupt
            shutil.copy(backupfile,outputFile)
        
    def GetResults(self,modifylog = True):
        """Get the result for specific day and desk. If query is for informational purpose set modifylog = False 
        to avoid appending to the log the day and task of the query in case it is missing"""
        try:
            
            with open(outputFile) as f:
                self.Output = json.load(f)
        
            for Desk in self.Output['Desk']:
                
                if Desk['Name']==self.Desk:
                        #if start of a new day, 1) Create back up of result file, dump error.out file and creates the day in result file,
                        if not any(map(lambda x:True if self.DateRef.strftime("%Y-%m-%d")==x['Date'] else False,Desk['Results'])):
                            
                            if modifylog == True:
                                
                                shutil.copyfile(outputFile, backupfile)
                                with open(LogFile,'w'):
                                    pass
                                
                                Desk['Results'].append({'Date':self.DateRef.strftime("%Y-%m-%d"),'Process':[{'Name':self.processname}]})
                                Desk['Results'][-1]['Process'][0]['Result']='Not Run'
                                Desk['Results'][-1]['Process'][0]['Traceback']=None
                                Desk['Results'][-1]['Process'][0]['TimeStamp']=None
                                
                                with open(outputFile,'w') as outfile:
                            
                                    json.dump(self.Output,outfile,indent=4,separators=(',', ': '))
                        
                            else:
                                
                                return ('No task performed on that day',None,None)
                
            for Results in Desk['Results']:
                    
                if Results['Date']==self.DateRef.strftime("%Y-%m-%d"):
                    
                    if not any(map(lambda x:True if self.processname==x['Name'] else False,Results['Process'])):
                        
                        if modifylog == True:  
                        
                            Results['Process'].append({'Name':self.processname})
                            Results['Process'][-1]['Result']='Not Run'
                            Results['Process'][-1]['Traceback']=None
                            Results['Process'][-1]['TimeStamp']=None
                            
                            with open(outputFile,'w') as outfile:
                
                                json.dump(self.Output,outfile,indent=4,separators=(',', ': '))
                            
                        else:
                            
                            return ('Not run',None,None)   
                        
                    for pro in Results['Process']:
                        
                        if pro['Name']==self.processname:
                            
                            return (pro['Result'],pro['Traceback'],pro['TimeStamp'])
        except:
           return (None,None,None)
                                        