'''
Based on the Stackoverflow question "python: creating excel workbook and dumping csv files as worksheets".
'''

import csv
import xlwt 
import os
from argparse import ArgumentParser
import sys

def get_nice_name(csvfile):
    csvfile = csvfile.replace('-','').replace('_','')
    csvfile = csvfile[0:30].encode("utf-8")
    return csvfile

def create_xls(directory, xls_file_name):
    wb = xlwt.Workbook()
    for filename in os.listdir(directory):
        if filename.endswith(".csv"):
            niceName = get_nice_name(os.path.splitext(filename)[0])
            try:
                ws = wb.add_sheet(niceName)
            except:
                print "Unable to add sheet with name: %s" %niceName
                break
            path_file = os.path.join(directory, filename)
            reader = csv.reader(path_file, delimiter=',')
            for rowx, row in enumerate(reader):
                for colx, value in enumerate(row):
                    try:
                        float(value)
                        s=False
                    except ValueError:
                        s=True
                    if s:
                        ws.write(rowx, colx, value)
                    else:
                        ws.write(rowx, colx, float(value))

    wb.save('{}\\{}{}'.format(folder_name,xls_file_name,'.xls'))
    absolut_path = os.path.abspath(folder_name)
    return os.path.join(absolut_path, xls_file_name)

if __name__ == '__main__':

    # arguments parser stuf
    parser = ArgumentParser()
    parser.add_argument("-f", "--folder", dest="folder_name", required=True,
                        help="folder where CSVs files are")
    parser.add_argument("-n", "--name", dest="xls_file_name", required=True,
                        help="name of the xls result file")
    args = parser.parse_args()
    folder_name = args.folder_name

    # TODO: integrate that validator snippets in ArgumentParser
    if not os.path.isdir(folder_name):
        print "the argument is not a folder"
        parser.print_help()
        sys.exit(0)

    xls_name = args.xls_file_name

    # other
    result_path = create_xls(folder_name, xls_name)
    print "Your file has been saved in the data folder %s" %(result_path)



