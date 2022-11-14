# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 20:40:08 2022

@author: Nick
"""
import os
indir = r'C:\Users\Nick\Documents\Python\Coursera\IBMDataScience\DataScienceCapstone\python_code'
files = os.listdir(indir)

for file in files:

    infile = indir + '\\' + file

    if infile[-3:]=='.py':
    
        with open(infile, 'r+') as fIn:
            outlines = []
            lines = fIn.readlines()
            #lines[4]=lines[4].replace('@author: 1109336', '@author: Nick')
            for ln in lines:            
                ln = ln.replace('1109336','Nick')
                outlines.append(ln)
            fIn.seek(0)
        
            fIn.writelines(outlines)
            fIn.truncate()
            fIn.close()