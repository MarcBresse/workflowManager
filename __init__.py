# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 10:25:59 2019

@author: enrac
"""

from Output import Output
from RelativeDay import RelativeDay
from Input import Input
from Process import Process
#Process configuration file lists processes and their attributes 
processFile = 'Processes.json'

#logFile is a daily log that gives the full traceback of errors in chronological order. 
#Resets at midnight.
LogFile = 'error.out'

#Result is the structured log file destined for the GUI. Logs are shown per day per process name.
outputFile = 'Result.json'

#backupfile is the back up of the Result.json file done at midnight. 
backupfile = 'Result_backup.json'
