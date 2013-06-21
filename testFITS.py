"""
This program takes two fits files as arguments and checks for 
differences between them. Uses the astropy module to achieve this.
Writes the output to a text file. 
"""
import sys
import subprocess
import numpy
import argparse
from astropy.io import fits

sys.path.append("original") # The original cosmics module directory
import cosmics as origCosmics

sys.path.append("optimized") # The optimized cosmics module directory
import cosmics as optCosmics
		
def parse_args():
    '''
    parse the command line arguemnts.
    '''
    parser = argparse.ArgumentParser(
        description = 'Takes two FITS files and compares them')
    parser.add_argument(
        '-file1',
        '-f1',
        required = True,
        help = 'firstFITS file for comparison')
    parser.add_argument(
    	'-file2',
    	'-f2',
    	required = True,
    	help = 'second FITS file for comparison')
    args = parser.parse_args()
    return args

args=parse_args() #parse input arguments
#check if inputs are of correct format
if args.file1.endswith(".fits") & args.file2.endswith(".fits"):
	file1=args.file1  
	file2=args.file2
else:
	print "Unrecognized argument(s). Requires two fits files."
	sys.exit(0)

#output filename created based on input filenames
diffFileName="diff"+file1[:-5]+file2[:-5]+".txt"

#open fits files for comparison
fits1=fits.open(file1)
fits2=fits.open(file2)
#use astropy's fits sub-module to find and report differences
fitsDiff=fits.FITSDiff(fits1,fits2,ignore_keywords=['*'])
diffFile=open(diffFileName,'w') #open output file
fitsDiff.report(diffFile,0) #write the report	
#close all open files
diffFile.close()			
fits1.close()	
fits2.close()

