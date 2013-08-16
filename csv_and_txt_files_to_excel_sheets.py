import csv, xlwt, os

def input_from_user(prompt):
    return raw_input(prompt).strip()

def make_an_excel_file_from_all_the_txtfiles_in_the_following_directory(directory):
    wb = xlwt.Workbook()
    for filename in os.listdir(data_folder_path):
        if filename.endswith(".csv") or filename.endswith(".txt"):
            ws = wb.add_sheet(os.path.splitext(filename)[0])
            with open('{}\\{}'.format(data_folder_path,filename),'rb') as csvfile:
                reader = csv.reader(csvfile, delimiter=',')
                for rowx, row in enumerate(reader):
                    for colx, value in enumerate(row):
                        ws.write(rowx, colx, value)
    return wb

if __name__ == '__main__':
    path_to_data = input_from_user("Where is the data stored?:  ")
    xls = make_an_excel_file_from_all_the_txtfiles_in_the_following_directory(path_to_data)
    xls_name = input_from_user('What do you want to name the excel file?:  ')
    xls.save('{}\\{}{}'.format(data_folder_path,xls_name,'.xls'))
    print "Your file has been saved in the data folder."



