# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 15:59:21 2018

@author: laguema
"""
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import sys
sys.path.append('Z:\\Fund_Oversight\\OVERSIGHT\\Operations\\Tools\\Scheduler\\')
from Process import process
import json



# In[14]:
ProcessFile={'Desk':[{'Name':'FundOver','Process':[]}]}
#ProcessFile={'Desk':[]}

with open(f'Z:\\Fund_Oversight\\OVERSIGHT\\Operations\\Tools\\Scheduler\\Processes.json','w') as outfile:
    json.dump(ProcessFile,outfile,indent=4,separators=(',', ': '))
    
# In[14]:   
inputs=[]

p=process(path='Z:\\Fund_Oversight\\OVERSIGHT\\Operations\\Tools\\Processes\\',name='Errorlog',hour = 25,RelativeDayStr='SD')
p.RemoveProcess()
#p.CreateNew()

# In[14]:   
inputs=[]

p=process(path='Z:\\Fund_Oversight\\OVERSIGHT\\Operations\\Tools\\Processes\\',name='FileGrab',Frequency = 0.5,RelativeDayStr='SD')
p.RemoveProcess()
p.CreateNew()

# In[14]:
p=process(path='Z:\\Fund_Oversight\\OVERSIGHT\\Operations\\Tools\\Processes\\',name='FileGrab',Frequency = 0.5,RelativeDayStr='PLBD')
p.RemoveProcess()
p.CreateNew()


# In[14]:   
inputs=[]

p=process(path='Z:\\Fund_Oversight\\OVERSIGHT\\Operations\\Tools\\Processes\\',name='ScheduleManualUpdate',hour = 25,RelativeDayStr='SD')
p.RemoveProcess()
p.CreateNew()


# In[14]:   

FundRepInput= {'Path':'Z:\\Fund_Oversight\\OVERSIGHT\\Operations\\Tools\\Processes\\', 'Name':'FundRepository','Format':'json','Date':'LBD'}

inputs=[FundRepInput]

p=process(path='Z:\\Fund_Oversight\\OVERSIGHT\\Operations\\Tools\\Processes\\',name='MissingData',inputs=inputs,Frequency = 1)
p.RemoveProcess()
#p.CreateNew()
   
# In[14]:   

JSONInput= {'Path':'Z:\\Fund_Oversight\\OVERSIGHT\\Operations\\Tools\\Scheduler\\', 'Name':'SCDPrice','Format':'json','Date':'LBD'}

inputs=[JSONInput]

p=process(path='Z:\\Fund_Oversight\\OVERSIGHT\\Operations\\Tools\\Processes\\',name='SCDHoldingRec',inputs=inputs,Continuous=True)
p.RemoveProcess()
p.CreateNew()
   

# In[14]:   

SCDTXN= {'Path':'Z:\\Fund_Oversight\\OVERSIGHT\\Operations\\Daily\\{Y}\\{Y}{m}\\{Y}{m}{d}\\Inputs\\', 'Name':'Dist_IN_SCD_{Y}{m}{d}','Format':'xlsx','Date':'LBD'}
SCD={'Path':'Z:\\Fund_Oversight\\OVERSIGHT\\Operations\\Daily\\{Y}\\{Y}{m}\\{Y}{m}{d}\\Inputs\\SCD\\AsiaT1\\','Name':'Holdings_NA_{Y}{m}{d}','Format':'xlsx','Date':'LBD'}
RBCNAV ={'Path':'\\\entsserver84\\tdrive\\AABOR\\PROD\\FundAdmin\\RBCFA\\Archive\\NAV\\Oversight\\', 'Name':'rbc_portnav_MLOVER_{Y}{m}{d}','Format':'txt','Date':'LBD'}
SSNAV ={'Path':'\\\entsserver84\\tdrive\\AABOR\\PROD\\FundAdmin\\SSBFA\\Archive\\NAV\\Oversight\\', 'Name':'SSB_NAV_CANADA_{Y}{m}{d}','Format':'txt','Date':'LBD'}
RBC= {'Path':'Z:\\Fund_Oversight\\OVERSIGHT\\Operations\\Daily\\{Y}\\{Y}{m}\\{Y}{m}{d}\\Inputs\\RBC\\', 'Name':'RBC_Holding_{Y}{m}{d}','Format':'csv','Date':'LBD'}

inputs=[SCDTXN,SCD,SSNAV,RBCNAV,RBC]

p=process(path='Z:\\Fund_Oversight\\OVERSIGHT\\Operations\\Tools\\Processes\\',name='Distributions',inputs=inputs,RelativeDayStr='LBD')
p.RemoveProcess()
p.CreateNew()


# In[14]:   

p=process(path='Z:\\Fund_Oversight\\OVERSIGHT\\Operations\\Tools\\Processes\\',name='ProductionSchedule',hour = 25,Continuous=False,RelativeDayStr='OriginMonth')
p.RemoveProcess()
p.CreateNew()

# In[14]:      
Backup= {'Path':'Z:\\Fund_Oversight\\OVERSIGHT\\Operations\\Tools\\BackUps\\', 'Name':'BackupTool','Format':'xlsx','Date':'LBD'}
        
inputs = [Backup]
p=process(path='Z:\\Fund_Oversight\\OVERSIGHT\\Operations\\Tools\\Processes\\',name='BackupTool',hour = 2,inputs=inputs,RelativeDayStr='LBD')
p.RemoveProcess()
p.CreateNew()

# In[14]:


FX= {'Path':'Z:\\Fund_Oversight\\OVERSIGHT\\Operations\\Daily\\{Y}\\{Y}{m}\\{Y}{m}{d}\\Inputs\\SCD\\', 'Name':'FX_Global_{Y}{m}{d}','Format':'xlsx','Date':'LBD'}
FX_= {'Path':'Z:\\Fund_Oversight\\OVERSIGHT\\Operations\\Daily\\{Y}\\{Y}{m}\\{Y}{m}{d}\\Inputs\\SCD\\', 'Name':'FX_Global_{Y}{m}{d}','Format':'xlsx','Date':'PLBD'}
SCD_={'Path':'Z:\\Fund_Oversight\\OVERSIGHT\\Operations\\Daily\\{Y}\\{Y}{m}\\{Y}{m}{d}\\Inputs\\SCD\\AsiaT1\\','Name':'Holdings_NA_{Y}{m}{d}','Format':'xlsx','Date':'PLBD'}
SCD={'Path':'Z:\\Fund_Oversight\\OVERSIGHT\\Operations\\Daily\\{Y}\\{Y}{m}\\{Y}{m}{d}\\Inputs\\SCD\\AsiaT1\\','Name':'Holdings_NA_{Y}{m}{d}','Format':'xlsx','Date':'LBD'}
SS={'Path':'Z:\\Fund_Oversight\\OVERSIGHT\\Operations\\Daily\\{Y}\\{Y}{m}\\{Y}{m}{d}\\Inputs\\','Name':'SSB Holding Positions_{Y}-{m}-{d}_00-35-00','Format':'csv','Date':'PLBD'}
SS_={'Path':'Z:\\Fund_Oversight\\OVERSIGHT\\Operations\\Daily\\{Y}\\{Y}{m}\\{Y}{m}{d}\\Inputs\\','Name':'SSB Holding Positions_{Y}-{m}-{d}_00-35-00','Format':'csv','Date':'LBD'}
FutureMap ={'Path':'Z:\\Fund_Oversight\\OVERSIGHT\\Operations\\Daily\\{Y}\\{Y}{m}\\{Y}{m}{d}\\Inputs\\SCD\\AsiaT1\\','Name':'SCD Future Transactions','Format':'xlsx','Date':'LBD'}
inputs=[FX,FX_,SCD,SCD_,SS,SS_,FutureMap]

p=process(path='Z:\\Fund_Oversight\\OVERSIGHT\\Operations\\Tools\\Processes\\',name='Futures',inputs=inputs)
p.RemoveProcess()
#p.CreateNew()

# In[14]: 

SCDNAV= {'Path':'Z:\\Fund_Oversight\\OVERSIGHT\\Operations\\Daily\\{Y}\\{Y}{m}\\{Y}{m}{d}\\Inputs\\SCD\\AsiaT1\\', 'Name':'Units_{Y}{m}{d}','Format':'xlsx','Date':'LBD'}
RBCNAV ={'Path':'\\\entsserver84\\tdrive\\AABOR\\PROD\\FundAdmin\\RBCFA\\Archive\\NAV\\Oversight\\', 'Name':'rbc_portnav_MLOVER_{Y}{m}{d}','Format':'txt','Date':'LBD'}
SSNAV ={'Path':'\\\entsserver84\\tdrive\\AABOR\\PROD\\FundAdmin\\SSBFA\\Archive\\NAV\\Oversight\\', 'Name':'SSB_NAV_CANADA_{Y}{m}{d}','Format':'txt','Date':'LBD'}
CITILuxNAV = {'Path':'Z:\\Fund_Oversight\\OVERSIGHT\\Operations\\Daily\\{Y}\\{Y}{m}\\{Y}{m}{d}\\Inputs\\CitiLux\\','Name':'CitiLux_NAV_{Y}{m}{d}','Format':'csv','Date':'LBD'}
RHBNAV = {'Path':'Z:\\Fund_Oversight\\OVERSIGHT\\Operations\\Daily\\{Y}\\{Y}{m}\\{Y}{m}{d}\\Inputs\\RHB\\','Name':'RHB_NAV_{Y}{m}{d}','Format':'csv','Date':'LBD'}
CIMBNAV = {'Path':'Z:\\Fund_Oversight\\OVERSIGHT\\Operations\\Daily\\{Y}\\{Y}{m}\\{Y}{m}{d}\\Inputs\\CIMB\\','Name':'CIMB_NAV_{Y}{m}{d}','Format':'csv','Date':'LBD'}
DBSNAV = {'Path':'Z:\\Fund_Oversight\\OVERSIGHT\\Operations\\Daily\\{Y}\\{Y}{m}\\{Y}{m}{d}\\Inputs\\DBS\\','Name':'DBS_NAV_{Y}{m}{d}','Format':'csv','Date':'LBD'}
SCBNAV = {'Path':'Z:\\Fund_Oversight\\OVERSIGHT\\Operations\\Daily\\{Y}\\{Y}{m}\\{Y}{m}{d}\\Inputs\\SCB\\','Name':'SCB_NAV_{Y}{m}{d}','Format':'csv','Date':'LBD'}
HSBCNAV = {'Path':'Z:\\Fund_Oversight\\OVERSIGHT\\Operations\\Daily\\{Y}\\{Y}{m}\\{Y}{m}{d}\\Inputs\\HSBC\\','Name':'HSBC_NAV_{Y}{m}{d}','Format':'csv','Date':'LBD'}
HSBCHKNAV = {'Path':'Z:\\Fund_Oversight\\OVERSIGHT\\Operations\\Daily\\{Y}\\{Y}{m}\\{Y}{m}{d}\\Inputs\\HSBC_HK_SG\\','Name':'HSBC_HK_SG_NAV_{Y}{m}{d}','Format':'csv','Date':'LBD'}
CITINAV = {'Path':'Z:\\Fund_Oversight\\OVERSIGHT\\Operations\\Daily\\{Y}\\{Y}{m}\\{Y}{m}{d}\\Inputs\\CITI\\','Name':'CITI_NAV_{Y}{m}{d}','Format':'csv','Date':'LBD'}
DEUTNAV = {'Path':'Z:\\Fund_Oversight\\OVERSIGHT\\Operations\\Daily\\{Y}\\{Y}{m}\\{Y}{m}{d}\\Inputs\\DEUT\\','Name':'DEUT_NAV_{Y}{m}{d}','Format':'csv','Date':'LBD'}
BCANAV = {'Path':'Z:\\Fund_Oversight\\OVERSIGHT\\Operations\\Daily\\{Y}\\{Y}{m}\\{Y}{m}{d}\\Inputs\\BCA\\','Name':'BCA_NAV_{Y}{m}{d}','Format':'csv','Date':'LBD'}
BDANNAV = {'Path':'Z:\\Fund_Oversight\\OVERSIGHT\\Operations\\Daily\\{Y}\\{Y}{m}\\{Y}{m}{d}\\Inputs\\BDAN\\','Name':'BDAN_NAV_{Y}{m}{d}','Format':'csv','Date':'LBD'}
BOCNAV = {'Path':'Z:\\Fund_Oversight\\OVERSIGHT\\Operations\\Daily\\{Y}\\{Y}{m}\\{Y}{m}{d}\\Inputs\\BOC\\','Name':'BOC_NAV_{Y}{m}{d}','Format':'csv','Date':'LBD'}
RBCHKNAV= {'Path':'Z:\\Fund_Oversight\\OVERSIGHT\\Operations\\Daily\\{Y}\\{Y}{m}\\{Y}{m}{d}\\Inputs\\RBCHK\\','Name':'RBCHK_NAV_{Y}{m}{d}','Format':'csv','Date':'LBD'}
BMANNAV= {'Path':'Z:\\Fund_Oversight\\OVERSIGHT\\Operations\\Daily\\{Y}\\{Y}{m}\\{Y}{m}{d}\\Inputs\\BMAN\\','Name':'BMAN_NAV_{Y}{m}{d}','Format':'csv','Date':'LBD'}
FXLDN= {'Path':'Z:\\Fund_Oversight\\OVERSIGHT\\Operations\\Daily\\{Y}\\{Y}{m}\\{Y}{m}{d}\\Inputs\\SCD\\', 'Name':'FX_Global_{Y}{m}{d}','Format':'xlsx','Date':'LBD'}
FXIND= {'Path':'Z:\\Fund_Oversight\\OVERSIGHT\\Operations\\Daily\\{Y}\\{Y}{m}\\{Y}{m}{d}\\Inputs\\SCD\\', 'Name':'FX_Indo_{Y}{m}{d}','Format':'xlsx','Date':'LBD'}
FXCWFA= {'Path':'Z:\\Fund_Oversight\\OVERSIGHT\\Operations\\Daily\\{Y}\\{Y}{m}\\{Y}{m}{d}\\Inputs\\SCD\\', 'Name':'FX_CWFA_{Y}{m}{d}','Format':'xlsx','Date':'LBD'}
COMP= {'Path':'Z:\\Fund_Oversight\\OVERSIGHT\\Operations\\Daily\\{Y}\\{Y}{m}\\{Y}{m}{d}\\Inputs\\SCD\\', 'Name':'completness','Format':'txt','Date':'SD'}

# In[14]:


inputs=[SCDNAV,RBCNAV,SSNAV,CITILuxNAV,RHBNAV,CIMBNAV,DBSNAV,SCBNAV,HSBCNAV,HSBCHKNAV,CITINAV,DEUTNAV,BCANAV,BDANNAV,BOCNAV,RBCHKNAV,BMANNAV,FXLDN,FXIND]

p=process(path='Z:\\Fund_Oversight\\OVERSIGHT\\Operations\\Tools\\Processes\\',name='UnitRec',inputs=inputs)
p.RemoveProcess()
p.CreateNew()

p=process(path='Z:\\Fund_Oversight\\OVERSIGHT\\Operations\\Tools\\Processes\\',name='TNARec',inputs=inputs)
p.RemoveProcess()
p.CreateNew()

p=process(path='Z:\\Fund_Oversight\\OVERSIGHT\\Operations\\Tools\\Processes\\',name='TNARec_Class',inputs=inputs)
p.RemoveProcess()
p.CreateNew()

p=process(path='Z:\\Fund_Oversight\\OVERSIGHT\\Operations\\Tools\\Processes\\',name='UnitRec_Country',inputs=inputs)
p.RemoveProcess()
p.CreateNew()



# In[14]:
SCDNAV= {'Path':'Z:\\Fund_Oversight\\OVERSIGHT\\Operations\\Daily\\{Y}\\{Y}{m}\\{Y}{m}{d}\\Inputs\\SCD\\AsiaT1\\', 'Name':'TNA_{Y}{m}{d}','Format':'xlsx','Date':'LBD'}
SCDUnits= {'Path':'Z:\\Fund_Oversight\\OVERSIGHT\\Operations\\Daily\\{Y}\\{Y}{m}\\{Y}{m}{d}\\Inputs\\SCD\\AsiaT1\\', 'Name':'Units_{Y}{m}{d}','Format':'xlsx','Date':'LBD'}
SCF= {'Path':'Z:\\Fund_Oversight\\OVERSIGHT\\Operations\\Daily\\{Y}\\{Y}{m}\\{Y}{m}{d}\\Inputs\\SCD\\AsiaT1\\', 'Name':'SCF_VALID_{Y}{m}{d}','Format':'csv','Date':'LBD'}
MCF= {'Path':'Z:\\Fund_Oversight\\OVERSIGHT\\Operations\\Daily\\{Y}\\{Y}{m}\\{Y}{m}{d}\\Inputs\\SCD\\AsiaT1\\', 'Name':'MCF_VALID_{Y}{m}{d}','Format':'csv','Date':'LBD'}

inputs=[SCDNAV,SCDUnits,FXLDN,FXIND,FXCWFA,SCF,MCF]

p=process(path='Z:\\Fund_Oversight\\OVERSIGHT\\Operations\\Tools\\Processes\\',name='dailySignOff_AsiaT1',inputs=inputs)
p.RemoveProcess()
p.CreateNew()
# In[14]:
p=process(path='Z:\\Fund_Oversight\\OVERSIGHT\\Operations\\Tools\\Processes\\',name='dailySignOff_NA',inputs=inputs)
p.RemoveProcess()
p.CreateNew()

# In[14]:
SCDNAV= {'Path':'Z:\\Fund_Oversight\\OVERSIGHT\\Operations\\Daily\\{Y}\\{Y}{m}\\{Y}{m}{d}\\Inputs\\SCD\\AsiaT\\', 'Name':'TNA_{Y}{m}{d}','Format':'xlsx','Date':'SD'}
SCDUnits= {'Path':'Z:\\Fund_Oversight\\OVERSIGHT\\Operations\\Daily\\{Y}\\{Y}{m}\\{Y}{m}{d}\\Inputs\\SCD\\AsiaT\\', 'Name':'Units_{Y}{m}{d}','Format':'xlsx','Date':'SD'}
SCF= {'Path':'Z:\\Fund_Oversight\\OVERSIGHT\\Operations\\Daily\\{Y}\\{Y}{m}\\{Y}{m}{d}\\Inputs\\SCD\\AsiaT\\', 'Name':'SCF_VALID_{Y}{m}{d}','Format':'csv','Date':'SD'}
MCF= {'Path':'Z:\\Fund_Oversight\\OVERSIGHT\\Operations\\Daily\\{Y}\\{Y}{m}\\{Y}{m}{d}\\Inputs\\SCD\\AsiaT\\', 'Name':'MCF_VALID_{Y}{m}{d}','Format':'csv','Date':'SD'}
FXIND= {'Path':'Z:\\Fund_Oversight\\OVERSIGHT\\Operations\\Daily\\{Y}\\{Y}{m}\\{Y}{m}{d}\\Inputs\\SCD\\', 'Name':'FX_Indo_{Y}{m}{d}','Format':'xlsx','Date':'SD'}
inputs=[SCDNAV,SCDUnits,FXIND,SCF,MCF,COMP]
p=process(path='Z:\\Fund_Oversight\\OVERSIGHT\\Operations\\Tools\\Processes\\',name='dailySignOff_AsiaT',inputs=inputs,RelativeDayStr='SD')
p.RemoveProcess()
p.CreateNew()

# In[14]:

p=process(path='Z:\\Fund_Oversight\\OVERSIGHT\\Operations\\Tools\\Processes\\',name='dailySignOff_Vietnam',RelativeDayStr='SD',hour = 25)
p.RemoveProcess()
p.CreateNew()

# In[14]:
SCDNAV= {'Path':'Z:\\Fund_Oversight\\OVERSIGHT\\Operations\\Daily\\{Y}\\{Y}{m}\\{Y}{m}{d}\\Inputs\\SCD\\FOF\\', 'Name':'TNA_{Y}{m}{d}','Format':'xlsx','Date':'LBD'}
SCDUnits= {'Path':'Z:\\Fund_Oversight\\OVERSIGHT\\Operations\\Daily\\{Y}\\{Y}{m}\\{Y}{m}{d}\\Inputs\\SCD\\FOF\\', 'Name':'Units_{Y}{m}{d}','Format':'xlsx','Date':'LBD'}
SCF= {'Path':'Z:\\Fund_Oversight\\OVERSIGHT\\Operations\\Daily\\{Y}\\{Y}{m}\\{Y}{m}{d}\\Inputs\\SCD\\FOF\\', 'Name':'SCF_VALID_{Y}{m}{d}','Format':'csv','Date':'LBD'}
MCF= {'Path':'Z:\\Fund_Oversight\\OVERSIGHT\\Operations\\Daily\\{Y}\\{Y}{m}\\{Y}{m}{d}\\Inputs\\SCD\\FOF\\', 'Name':'MCF_VALID_{Y}{m}{d}','Format':'csv','Date':'LBD'}
inputs=[SCDNAV,SCDUnits,FXLDN,FXIND,FXCWFA,SCF,MCF]
p=process(path='Z:\\Fund_Oversight\\OVERSIGHT\\Operations\\Tools\\Processes\\',name='dailySignOff_FOF',inputs=inputs,RelativeDayStr='LBD')
p.RemoveProcess()
p.CreateNew()

# In[14]:
Future = {'Path':'Z:\\Fund_Oversight\\OVERSIGHT\\Operations\\Daily\\{Y}\\{Y}{m}\\{Y}{m}{d}\\Futures\\Data\\','Name':'Future_Raw{Y}{m}{d}','Format':'xlsx','Date':'LBD'}
inputs=[Future]
p=process(path='Z:\\Fund_Oversight\\OVERSIGHT\\Operations\\Tools\\Processes\\',name='FutureTemplate',inputs=inputs,Language = 'VBA')
p.RemoveProcess()
#p.CreateNew()

# In[14]:

TNA = {'Path':'Z:\\Fund_Oversight\\OVERSIGHT\\Operations\\Daily\\{Y}\\{Y}{m}\\{Y}{m}{d}\\Inputs\\','Name':'SCD TNA and NAV Price {m}.{d}.{y}','Format':'xlsx','Date':'LBD'}
NAV={'Path':'Z:\\Fund_Oversight\\OVERSIGHT\\Operations\\Daily\\{Y}\\{Y}{m}\\{Y}{m}{d}\\Inputs\\','Name':'SCD Official Distribution per unit ({m}{d}{Y})','Format':'xlsx','Date':'LBD'}
inputs=[TNA,NAV]

p=process(path='Z:\\Fund_Oversight\\OVERSIGHT\\Operations\\Tools\\Processes\\',name='TNA',inputs=inputs)
p.RemoveProcess()
#p.CreateNew()
# In[14]:
p=process(path='Z:\\Fund_Oversight\\OVERSIGHT\\Operations\\Tools\\Smart_Sampling\\',name='testing',hour=9)

p.RemoveProcess()
#p.CreateNew()
# In[14]:
p=process(path='Z:\\Fund_Oversight\\OVERSIGHT\\Operations\\Tools\\Smart_Sampling\\',name='SmartSampling_Main',RelativeDayStr='OriginWeek',hour=9)

p.RemoveProcess()
#p.CreateNew()

# In[16]: 
p=process(path='Z:\\Fund_Oversight\\OVERSIGHT\\Operations\\Tools\\Processes\\',name='NAVACC_files',hour=3)
p.RemoveProcess()
p.CreateNew()

# In[14]:
p=process(path='Z:\\Fund_Oversight\\OVERSIGHT\\Operations\\Tools\\Processes\\',name='SSTXN',hour=9)
p.RemoveProcess()
p.CreateNew()    
# In[14]:  
        
            

BPL= {'Path':'Z:\\Fund_Oversight\\OVERSIGHT\\Operations\\Daily\\{Y}\\{Y}{m}\\{Y}{m}{d}\\Inputs\\', 'Name':'bpl_price_master_{Y}-{m}-{d}','Format':'csv','Date':'LBD'}
BPL_= {'Path':'Z:\\Fund_Oversight\\OVERSIGHT\\Operations\\Daily\\{Y}\\{Y}{m}\\{Y}{m}{d}\\Inputs\\', 'Name':'bpl_price_master_{Y}-{m}-{d}','Format':'csv','Date':'PLBD'}
FX= {'Path':'Z:\\Fund_Oversight\\OVERSIGHT\\Operations\\Daily\\{Y}\\{Y}{m}\\{Y}{m}{d}\\Inputs\\SCD\\', 'Name':'FX_Global_{Y}{m}{d}','Format':'xlsx','Date':'LBD'}
FX_= {'Path':'Z:\\Fund_Oversight\\OVERSIGHT\\Operations\\Daily\\{Y}\\{Y}{m}\\{Y}{m}{d}\\Inputs\\SCD\\', 'Name':'FX_Global_{Y}{m}{d}','Format':'xlsx','Date':'PLBD'}
SCD_={'Path':'Z:\\Fund_Oversight\\OVERSIGHT\\Operations\\Daily\\{Y}\\{Y}{m}\\{Y}{m}{d}\\Inputs\\SCD\\AsiaT1\\','Name':'Holdings_NA_{Y}{m}{d}','Format':'xlsx','Date':'PLBD'}
SCD={'Path':'Z:\\Fund_Oversight\\OVERSIGHT\\Operations\\Daily\\{Y}\\{Y}{m}\\{Y}{m}{d}\\Inputs\\SCD\\AsiaT1\\','Name':'Holdings_NA_{Y}{m}{d}','Format':'xlsx','Date':'LBD'}
FXIndo= {'Path':'Z:\\Fund_Oversight\\OVERSIGHT\\Operations\\Daily\\{Y}\\{Y}{m}\\{Y}{m}{d}\\Inputs\\SCD\\', 'Name':'FX_Indo_{Y}{m}{d}','Format':'xlsx','Date':'LBD'}
FXIndo_= {'Path':'Z:\\Fund_Oversight\\OVERSIGHT\\Operations\\Daily\\{Y}\\{Y}{m}\\{Y}{m}{d}\\Inputs\\SCD\\', 'Name':'FX_Indo_{Y}{m}{d}','Format':'xlsx','Date':'PLBD'}
FXCWFA= {'Path':'Z:\\Fund_Oversight\\OVERSIGHT\\Operations\\Daily\\{Y}\\{Y}{m}\\{Y}{m}{d}\\Inputs\\SCD\\', 'Name':'FX_CWFA_{Y}{m}{d}','Format':'xlsx','Date':'LBD'}
FXCWFA_= {'Path':'Z:\\Fund_Oversight\\OVERSIGHT\\Operations\\Daily\\{Y}\\{Y}{m}\\{Y}{m}{d}\\Inputs\\SCD\\', 'Name':'FX_CWFA_{Y}{m}{d}','Format':'xlsx','Date':'PLBD'}

inputs=[BPL,BPL_,FX,FX_,FXCWFA,FXCWFA_,FXIndo,FXIndo_,SCD,SCD_]

p=process(path='Z:\\Fund_Oversight\\OVERSIGHT\\Operations\\Tools\\Processes\\',name='DTD_AsiaT1',inputs=inputs)
p.RemoveProcess()
p.CreateNew()

# In[15]:  
CIBC= {'Path':'Z:\\Fund_Oversight\\OVERSIGHT\\Operations\\Daily\\{Y}\\{Y}{m}\\{Y}{m}{d}\\Inputs\\', \
                                                                   'Name':'ETF_SameDay_{Y}{m}{d}','Format':'xlsx','Date':'LBD'}

CIBC_= {'Path':'Z:\\Fund_Oversight\\OVERSIGHT\\Operations\\Daily\\{Y}\\{Y}{m}\\{Y}{m}{d}\\Inputs\\', \
                                                                   'Name':'ETF_SameDay_{Y}{m}{d}','Format':'xlsx','Date':'PLBD'}
    
RBC= {'Path':'Z:\\Fund_Oversight\\OVERSIGHT\\Operations\\Daily\\{Y}\\{Y}{m}\\{Y}{m}{d}\\Inputs\\RBC\\', 'Name':'RBC_Holding_{Y}{m}{d}','Format':'csv','Date':'LBD'}
RBC_= {'Path':'Z:\\Fund_Oversight\\OVERSIGHT\\Operations\\Daily\\{Y}\\{Y}{m}\\{Y}{m}{d}\\Inputs\\RBC\\', 'Name':'RBC_Holding_{Y}{m}{d}','Format':'csv','Date':'PLBD'}
BPL= {'Path':'Z:\\Fund_Oversight\\OVERSIGHT\\Operations\\Daily\\{Y}\\{Y}{m}\\{Y}{m}{d}\\Inputs\\', 'Name':'bpl_price_master_{Y}-{m}-{d}','Format':'csv','Date':'LBD'}
BPL_= {'Path':'Z:\\Fund_Oversight\\OVERSIGHT\\Operations\\Daily\\{Y}\\{Y}{m}\\{Y}{m}{d}\\Inputs\\', 'Name':'bpl_price_master_{Y}-{m}-{d}','Format':'csv','Date':'PLBD'}
FX= {'Path':'Z:\\Fund_Oversight\\OVERSIGHT\\Operations\\Daily\\{Y}\\{Y}{m}\\{Y}{m}{d}\\Inputs\\SCD\\', 'Name':'FX_Global_{Y}{m}{d}','Format':'xlsx','Date':'LBD'}
FX_= {'Path':'Z:\\Fund_Oversight\\OVERSIGHT\\Operations\\Daily\\{Y}\\{Y}{m}\\{Y}{m}{d}\\Inputs\\SCD\\', 'Name':'FX_Global_{Y}{m}{d}','Format':'xlsx','Date':'PLBD'}
SCD_={'Path':'Z:\\Fund_Oversight\\OVERSIGHT\\Operations\\Daily\\{Y}\\{Y}{m}\\{Y}{m}{d}\\Inputs\\SCD\\AsiaT1\\','Name':'Holdings_NA_{Y}{m}{d}','Format':'xlsx','Date':'PLBD'}
SCD={'Path':'Z:\\Fund_Oversight\\OVERSIGHT\\Operations\\Daily\\{Y}\\{Y}{m}\\{Y}{m}{d}\\Inputs\\SCD\\AsiaT1\\','Name':'Holdings_NA_{Y}{m}{d}','Format':'xlsx','Date':'LBD'}


inputs=[CIBC,CIBC_,RBC,RBC_,BPL,BPL_,FX,FX_,SCD,SCD_]

p=process(path='Z:\\Fund_Oversight\\OVERSIGHT\\Operations\\Tools\\Processes\\',name='DTD',inputs=inputs)
p.RemoveProcess()
p.CreateNew()


# In[15]:  

BBG= {'Path':'Z:\\Fund_Oversight\\OVERSIGHT\\Operations\\Tools\\Bloomberg\\Output\\', 'Name':'Extract_{m}{d}{Y}','Format':'xlsx','Date':'LBD'}
PyOutput =  {'Path':'Z:\\Fund_Oversight\\OVERSIGHT\\Operations\\Daily\\{Y}\\{Y}{m}\\{Y}{m}{d}\\Performance Validation\\DTD\\', 'Name':'BBG {m}{d}{Y}','Format':'xlsx','Date':'LBD'}
p=process(path='Z:\\Fund_Oversight\\OVERSIGHT\\Operations\\Tools\\Processes\\',name='DTDReport',inputs=[BBG,PyOutput],Language = 'VBA')
p.RemoveProcess()
p.CreateNew()

# In[15]:  

BBG= {'Path':'Z:\\Fund_Oversight\\OVERSIGHT\\Operations\\Tools\\Bloomberg\\Output\\', 'Name':'Extract_AsiaT1_{m}{d}{Y}','Format':'xlsx','Date':'LBD'}
PyOutput =  {'Path':'Z:\\Fund_Oversight\\OVERSIGHT\\Operations\\Daily\\{Y}\\{Y}{m}\\{Y}{m}{d}\\Performance Validation\\DTD\\', 'Name':'BBG_AsiaT1 {m}{d}{Y}','Format':'xlsx','Date':'LBD'}
p=process(path='Z:\\Fund_Oversight\\OVERSIGHT\\Operations\\Tools\\Processes\\',name='DTDReport_AsiaT1',inputs=[BBG,PyOutput],Language = 'VBA')
p.RemoveProcess()
p.CreateNew()


# In[15]:  
p=process(path='Z:\\Fund_Oversight\\OVERSIGHT\\Operations\\Tools\\Smart_Sampling\\',name='BBGIndices',hour=4,Language = 'VBA')
p.RemoveProcess()
p.CreateNew()

# In[15]:  
CIBC= {'Path':'Z:\\Fund_Oversight\\OVERSIGHT\\Operations\\Daily\\{Y}\\{Y}{m}\\{Y}{m}{d}\\Inputs\\', \
                                                                   'Name':'ETF_SameDay_{Y}{m}{d}','Format':'xlsx','Date':'SD'}

CIBC_= {'Path':'Z:\\Fund_Oversight\\OVERSIGHT\\Operations\\Daily\\{Y}\\{Y}{m}\\{Y}{m}{d}\\Inputs\\', \
                                                                   'Name':'ETF_SameDay_{Y}{m}{d}','Format':'xlsx','Date':'LBD'}

Basket= {'Path':'Z:\\Fund_Oversight\\OVERSIGHT\\Operations\\Daily\\{Y}\\{Y}{m}\\{Y}{m}{d}\\Inputs\\', \
                                                                   'Name':'Baskets {Y}{m}{d}','Format':'xls','Date':'SD'}

Basket_= {'Path':'Z:\\Fund_Oversight\\OVERSIGHT\\Operations\\Daily\\{Y}\\{Y}{m}\\{Y}{m}{d}\\Inputs\\', \
                                                                   'Name':'Baskets {Y}{m}{d}','Format':'xls','Date':'LBD'}

TB= {'Path':'Z:\\Fund_Oversight\\OVERSIGHT\\Operations\\Daily\\{Y}\\{Y}{m}\\{Y}{m}{d}\\Inputs\\', \
                                                                   'Name':'Trade_Blotter_File_{m}{d}{y}','Format':'xls','Date':'LBD'}

TB_= {'Path':'Z:\\Fund_Oversight\\OVERSIGHT\\Operations\\Daily\\{Y}\\{Y}{m}\\{Y}{m}{d}\\Inputs\\', \
                                                                   'Name':'Trade_Blotter_File_{m}{d}{y}','Format':'xls','Date':'PLBD'} 

PLF= {'Path':'Z:\\Fund_Oversight\\OVERSIGHT\\Operations\\Daily\\{Y}\\{Y}{m}\\{Y}{m}{d}\\Inputs\\', \
                                                                   'Name':'PLF {Y}{m}{d}','Format':'xlsx','Date':'SD'}

PLF_= {'Path':'Z:\\Fund_Oversight\\OVERSIGHT\\Operations\\Daily\\{Y}\\{Y}{m}\\{Y}{m}{d}\\Inputs\\', \
                                                                   'Name':'PLF {Y}{m}{d}','Format':'xlsx','Date':'LBD'}

inputs=[CIBC,CIBC_,Basket,Basket_,TB,TB_,PLF,PLF_]

p=process(path='Z:\\Fund_Oversight\\OVERSIGHT\\Operations\\Tools\\Processes\\',name='ETF',inputs=inputs,RelativeDayStr='SD')
p.RemoveProcess()
p.CreateNew()


# In[16]: 
p=process(path='Z:\\Fund_Oversight\\OVERSIGHT\\Operations\\Tools\\Processes\\',name='API',hour=9)
p.RemoveProcess()
p.CreateNew()

# In[16]:
RBC= {'Path':'Z:\\Fund_Oversight\\OVERSIGHT\\Operations\\Daily\\{Y}\\{Y}{m}\\{Y}{m}{d}\\Inputs\\RBC\\', 'Name':'RBC_Holding_{Y}{m}{d}','Format':'csv','Date':'LBD'}
RBC_= {'Path':'Z:\\Fund_Oversight\\OVERSIGHT\\Operations\\Daily\\{Y}\\{Y}{m}\\{Y}{m}{d}\\Inputs\\RBC\\', 'Name':'RBC_Holding_{Y}{m}{d}','Format':'csv','Date':'PLBD'}
RBCNAV ={'Path':'\\\entsserver84\\tdrive\\AABOR\\PROD\\FundAdmin\\RBCFA\\Archive\\NAV\\Oversight\\', 'Name':'rbc_portnav_MLOVER_{Y}{m}{d}','Format':'txt','Date':'LBD'}
RBCNAV_ ={'Path':'\\\entsserver84\\tdrive\\AABOR\\PROD\\FundAdmin\\RBCFA\\Archive\\NAV\\Oversight\\', 'Name':'rbc_portnav_MLOVER_{Y}{m}{d}','Format':'txt','Date':'PLBD'}
SSNAV ={'Path':'\\\entsserver84\\tdrive\\AABOR\\PROD\\FundAdmin\\SSBFA\\Archive\\NAV\\Oversight\\', 'Name':'SSB_NAV_CANADA_{Y}{m}{d}','Format':'txt','Date':'LBD'}
SSNAV_ ={'Path':'\\\entsserver84\\tdrive\\AABOR\\PROD\\FundAdmin\\SSBFA\\Archive\\NAV\\Oversight\\', 'Name':'SSB_NAV_CANADA_{Y}{m}{d}','Format':'txt','Date':'PLBD'}
RBCTXN = {'Path':'Z:\\Fund_Oversight\\OVERSIGHT\\Operations\\Daily\\{Y}\\{Y}{m}\\{Y}{m}{d}\\Inputs\\', 'Name':'RBC_Unsett_{d}{m}{y}','Format':'csv','Date':'LBD'}
SSTXN = {'Path':'Z:\\Fund_Oversight\\OVERSIGHT\\Operations\\Daily\\{Y}\\{Y}{m}\\{Y}{m}{d}\\Inputs\\', 'Name':'SSB_CANADA_TXN_{Y}{m}{d}','Format':'txt','Date':'LBD'}
inputs=[RBC,RBC_,RBCNAV,RBCNAV_,SSNAV,SSNAV_,RBCTXN]

p=process(path='Z:\\Fund_Oversight\\OVERSIGHT\\Operations\\Tools\\Processes\\',name='MVAD',inputs=inputs)
p.RemoveProcess()
p.CreateNew()