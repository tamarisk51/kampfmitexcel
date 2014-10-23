# -*- coding: utf-8 -*-
"""
Created on Wed Aug 06 11:01:46 2014

@author: James
"""

import ast, xlrd, re, sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm

datafile = 'C:\Users\James\Documents\Research\data\js140731\plotting_test.xls'
pltop={}
options={}
pltinstr = [(1,pltop,'bkgrd'),(2,pltop,'analyte')]
instructions = [('title1',options,pltinstr),('title2',options,pltinstr)]


def apply_options(fig,ax,options):
    """
    See http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.xlim
    or http://matplotlib.org/api/pyplot_summary.html#matplotlib.pyplot.plotting
    
    """
    if 'xlim' in options:
        ax.set_xlim(options['xlim'])
    if 'ylim' in options:
        ax.set_ylim(options['ylim'])
    
def sheet2xyDF(datafile,sheetname,label):
    """"Converts an xls sheet to a x,y formated dataframe"""
    xd = pd.ExcelFile(datafile)
    if type(sheetname)==int:  
        df = xd.parse(xd.sheet_names[sheetname], header=None)
    elif type(sheetname) in [str,unicode] :  
        df = xd.parse(sheetname, header=None)
  
    # drop all the rows with nan (which are just comments)
    # and drop the 'Charge/C' column
    df2 = df.dropna().drop(df.columns[2:],axis=1)
    
    # replace the headers numbers with strings
    newheaders = ['x','y']
    df3 = df2.rename(columns={old: new for old,new in enumerate(newheaders)})[1:]
    oldindex = df3.index.tolist()
    df4 = df3.rename(index={old: new for new,old in enumerate(oldindex)})

    return df4

def pltinstr2cvplot(datafile,title,options,pltinstr):
    """Takes instructions (in the form of a list of (sheet,label) tuples
    and plot them out as a cyclic voltammogram."""
    fig = plt.figure()
    ax = fig.add_subplot(111)
    n_plots = len(pltinstr)
    color_idx,i = np.linspace(0.9,0.1,n_plots+1).tolist()[:-1],0
    for sheet,pltop,label in pltinstr:
        df = sheet2xyDF(datafile,sheet,label)
        ax.plot(df['x'],df['y'],label=label,color=plt.cm.binary(color_idx[i]),
                lw=3,**pltop)
        i+=1
        
    ##  Apply the default formating options
    ax.set_xlabel('Potential/V')
    ax.set_ylabel('Current/A')
    ax.set_title(title)
    ax.legend(loc='upper left')
    
    ## Apply any additional formating options
    apply_options(fig,ax,options)    
    
    fig.savefig('{0}\\{1}.png'.format(datafile.rpartition('\\')[0],title))
    #fig.show()

def instructions2multicvplots(datafile,instructions):
    """Takes in a set of instructions, and plots out each of them
    in a separate window, and saves them to separate files. """
    for title,options,pltinstr in instructions:
        pltinstr2cvplot(datafile,title,options,pltinstr)

#instructions2multicvplots(datafile,instructions)

def xls2multicvplots(datafile):
    """Takes in an xls file with an 'instructions' sheet, and returns 
    the plots described in the instructions."""
    wb = xlrd.open_workbook(datafile)
    ws = wb.sheet_by_name('instructions')
    nrows = ws.nrows
    instructions = []
    this_fig,options,pltinstr = '',{},[]
    pastfirstplt=False
    for i in range(0,nrows):
        cellval = ws.cell_value(i,0)
        if re.match('#',cellval): # you're at a title line
            if pastfirstplt == True:
                try:  
                    # you're probably about the start at fig 2, fig 3, fig 4... 
                    # but you may be at the first line so just *try*
                    instructions.append((this_fig,options,pltinstr))
                except:
                    pass
            this_fig = str(cellval).strip('#')
            pltinstr = []
            pastfirstplt=True
            try:         
                optionsP = ast.literal_eval('{'+ws.cell_value(i,1)+'}')                
                if optionsP != '': 
                    options = dict(optionsP)
                else: 
                    options = {}
            except:
                options = {}
            continue
        elif cellval != '': # you're either at a plot line, or some kind of junk
            try:
                pltop = ast.literal_eval('{'+ws.cell_value(i,2)+'}')  
                if pltop != '':
                    try:
                        pltinstr.append((ws.cell_value(i,0),dict(pltop),ws.cell_value(i,1)))
                    except:
                        continue
                else:
                    try:
                        pltinstr.append((ws.cell_value(i,0),{},ws.cell_value(i,1)))
                    except:
                        continue
            except:
                try:
                    pltinstr.append((ws.cell_value(i,0),{},ws.cell_value(i,1)))
                except:
                    continue
        if i == nrows-1:
            instructions.append((this_fig,options,pltinstr))
            
    instructions2multicvplots(datafile,instructions)

#################################################################
#
#################################################################

if len(sys.argv)==2:
    xls2multicvplots(sys.argv[1])
    print "Your CVs have been plotted."
else:
    print "Please use this script with the following arguments:  > python plot_cvs.py C:\path\to\file.xls "
                      



