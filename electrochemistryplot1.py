'''
## Usage

> python electrochemistryplot1.py C:\data\directory filename.txt
{creates matplotlib plot of the CV or CA contained therein}

##############
The accptable experiment types (exptype) are:
    CA, chronoamperometry
    CV, cyclic voltametry
    ...

'''
import sys, csv
import matplotlib.pyplot as plt

def getData(directory,filename):
    '''(str, str) -> list, list
    Open the file of the given filename in the given directory.
    Put the potential (or time) and current values into their respective lists.
    Returns the two lists.
    '''
    exptype = 'CV'
    with open('{}\\{}'.format(directory,filename),'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        reached_header = False
        xa=[]
        ya=[]
        for rowx, row in enumerate(reader):
            for colx, value in enumerate(row):
                if reached_header==False and value=='Potential/V':  #or Time/s, in the case of CAs
                    reached_header=True
                    break
                # where do you determine the exptype?
                if value!='' and value.find('Segment')==-1 and reached_header==True:
                    #then start putting data into arrays.
                    if colx==0:  # it's a potential (or time)
                        xa.append(float(value))
                    if colx==1:  # it's a current
                        ya.append(float(value))
    return xa, ya, exptype 

def getXlabel(exptype):
    if exptype=='CV':
        xlabel = 'Potential (V)'
    if exptype=='CA':
        xlabel = 'Time (s)'
    return xlabel
    

if len(sys.argv)==3:
    directory = sys.argv[1]
    filename = sys.argv[2]
    xa, ya, exptype = getData(directory,filename)
    plt.plot(xa,ya)
    plt.xlabel(getXlabel(exptype))
    plt.ylabel('Current (A)')
    plt.show()
else:
    print "Please use this script with the following arguments:  > python electrochemistryplot1.py C:\data\directory filename.txt"

