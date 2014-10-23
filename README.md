# kampfmitexcel

Several Python script for taking all the text and/or csv files in a folder and making them the sheets of a single excel file.  


## Usage

csv_and_txt_files_to_excel_sheets.py
	>>> execfile('C:\...\csv_and_txt_files_to_excel_sheets.py')
	Where is the data stored?:  C:\...\data\130815
	What do you want to name the excel file?:  130815results
	Your file has been saved in the data folder.

	# creates a file '130815results.xls' located in 'C:\...\data\130815'

csvs2xls.py
	> python csvs2xls.py C:\data\directory outputfilename
	
chi_csvs2xls.py
plot_cvs.py
     # This specifically for formatting results from a CHI potentiostat.
     # Adds a template 'instructions' sheet, used by the plot_cvs.py script.
	> python chi_csvs2xls.py C:\data\directory outputfilename	 
     Your file has been saved in the data folder.

     # Modify the 'instructions' sheet to plot what you want.
	> python plot_cvs.py C:\data\directory\outputfilename.xls	



	