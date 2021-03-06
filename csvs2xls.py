import sys, csv, xlwt, os
cmdargs = str(sys.argv)


def write_in_correct_formate(ws,rowx,colx,value):
    """
    Writes the values as either a float or a string, instead of just assuming everything
    is a string.
    """
    try:
        float(value)
        s=False
    except ValueError:
        s=True
    if s:
        ws.write(rowx, colx, value)
    else:
        ws.write(rowx, colx, float(value))

def csvs2xls(directory):
    wb = xlwt.Workbook()
    for filename in os.listdir(directory):
        if filename.endswith(".csv") or filename.endswith(".txt"):
            ws = wb.add_sheet(os.path.splitext(filename)[0])
            with open('{}\\{}'.format(directory,filename),'rb') as csvfile:
                reader = csv.reader(csvfile, delimiter=',')
                for rowx, row in enumerate(reader):
                     for colx, value in enumerate(row):
                         write_in_correct_formate(ws,rowx,colx,value)
            
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


