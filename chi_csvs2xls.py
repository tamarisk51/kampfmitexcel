import sys, csv, xlwt, os
cmdargs = str(sys.argv)

def write_row(ws,rowx,row_array):
    """
    Writes the values as either a float or a string, instead of just assuming everything
    is a string.
    """
    for colx, value in enumerate(row_array):
        try:
            float(value)
            type_to_write="Float"
        except ValueError:
            type_to_write="String"
        if type_to_write=="Float":
            ws.write(rowx, colx, float(value))
        elif type_to_write=="String":
            ws.write(rowx, colx, value)

def csvs2xls(directory):
    wb = xlwt.Workbook()
    
    # Add 'instructions' tab
    ws = wb.add_sheet('instructions')
    write_row(ws,0,["#title","'xlim':(0.2,1.4), 'ylim':(-0.00000000001,0.00000000025)"]) 
    write_row(ws,1,["file0","background","'linestyle':':', 'linewidth':3.0"])     
    write_row(ws,2,["file1","1mM analyte"])
    write_row(ws,3,["file2","2mM analyte"]) 
    
    # Write all the csv files in the directory to this workbook.
    for filename in os.listdir(directory):
        if filename.endswith(".csv") or filename.endswith(".txt"):
            ws = wb.add_sheet(os.path.splitext(filename)[0])
            with open('{}\\{}'.format(directory,filename),'rb') as csvfile:
                reader = csv.reader(csvfile, delimiter=',')
                skipped_rows=0
                for rowx, row in enumerate(reader):
                    # Skip blank rows
                    if len(row)<1:
                        skipped_rows+=1
                        continue
                    # Skip text rows we don't want
                    if ("Segment" in row[0]) or \
                       ("Header" in row[0]) or \
                       ("Note" in row[0]) or \
                       ("Ep" in row[0]) or \
                       ("ip" in row[0]) or \
                       ("Ah" in row[0]):
                        skipped_rows+=1
                        continue
                    # Add a blank row before the data
                    if ("Potential" in row[0]):
                        skipped_rows-=1
                    rowx = rowx - skipped_rows
                    write_row(ws,rowx,row)         
    return wb 


if len(sys.argv)==3:
    directory = sys.argv[1]
    xls = csvs2xls(directory)
    xls.save('{}\\{}{}'.format(directory,sys.argv[2],'.xls'))
    print "Your file has been saved in the data folder."
elif len(sys.argv)==2:
    # for when the script is in the same directory as all the data files.
    directory = os.getcwd()
    xls = csvs2xls(directory)
    xls.save('{}\\{}{}'.format(directory,sys.argv[1],'.xls'))
    print "Your file has been saved in the data folder."
else:
    print "Please use this script with the following arguments:  > python csvs2xls.py C:\data\directory outputfilename."


