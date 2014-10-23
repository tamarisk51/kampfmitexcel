# kampfmitexcel

A Python script for taking all the text and/or csv files in a folder and making them the sheets of a single excel file.  

Two others that are specific to handling the cyclic voltammetry results from CHI potentiostat.

## Usage

csvs2xls.py
###
	> python csvs2xls.py C:\data\directory outputfilename
	 Your file has been saved in the data folder.
  	
chi_csvs2xls.py and plot_cvs.py
###
    # This script is specifically for formatting results from a CHI potentiostat.
	> python chi_csvs2xls.py C:\data\directory outputfilename	 
     Your file has been saved in the data folder.

    # This will also add a template 'instructions' sheet to the file.

    # Modify the 'instructions' sheet to plot what you want.
	> python plot_cvs.py C:\data\directory\outputfilename.xls	
     Your CVs have been plotted.


	
