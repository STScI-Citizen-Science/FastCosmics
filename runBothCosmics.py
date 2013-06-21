"""
This script takes a fits file as input and runs both the 
original cosmics.py module as well as the optimized fast
cosmics module on it. 
Based on the demo.py file by Malte Tewes packaged with the
original cosmics.py module.
Outputs: origClean.fits, origMask.fits, optClean.fits, optMast.fits
"""

import sys
import subprocess
import numpy
import argparse

sys.path.append("original") # The original cosmics module directory
import cosmics as origCosmics

sys.path.append("optimized") # The optimized cosmics module directory
import cosmics as optCosmics

def parse_args():
    '''
    parse the command line arguemnts.
    '''
    parser = argparse.ArgumentParser(
        description = 'Run both versions of comsics.py module on a FITS file')
    parser.add_argument(
        '-file',
        required = True,
        help = 'FITS file input to be used for processing')
    args = parser.parse_args()
    return args

def origRemoval(fitsFile):
	"""
	Runs the original cosmics.py script on the input FITS file.
	Outputs: origClean.fits, origMask.Fits
	"""
	# Read the FITS :
	array, header = origCosmics.fromfits(fitsFile)
	# array is a 2D numpy array

	# Build the object :
	c = origCosmics.cosmicsimage(array, gain=2.2, readnoise=10.0, sigclip = 5.0,
	 sigfrac = 0.3, objlim = 5.0)
	# There are other options, check the manual...

	# Run the full artillery :
	c.run(maxiter = 4)

	# Write the cleaned image into a new FITS file, conserving the original header :
	origCosmics.tofits("origClean.fits", c.cleanarray, header)

	# If you want the mask, here it is :
	origCosmics.tofits("origMask.fits", c.mask, header)
	# (c.mask is a boolean numpy array, that gets converted here to an integer array)

def optRemoval(fitsFile):
	"""
	Runs the optimized cosmics.py script on the input FITS file.
	Outputs: optClean.fits, optMask.Fits
	"""
	# Read the FITS :
	array, header = optCosmics.fromfits(fitsFile)
	# array is a 2D numpy array

	# Build the object :
	c = optCosmics.cosmicsimage(array, gain=2.2, readnoise=10.0, sigclip = 5.0,
	 sigfrac = 0.3, objlim = 5.0)
	# There are other options, check the manual...

	# Run the full artillery :
	c.run(maxiter = 4)

	# Write the cleaned image into a new FITS file, conserving the original header :
	optCosmics.tofits("optClean.fits", c.cleanarray, header)

	# If you want the mask, here it is :
	optCosmics.tofits("optMask.fits", c.mask, header)
	# (c.mask is a boolean numpy array, that gets converted here to an integer array)

args=parse_args() #get the input arguments

#check if input is a fits file
if args.file.endswith(".fits"):
	fitsFile=args.file; #first argument is the input FITS file
else:
	print "Unrecognized argument. Requires fits file. Eg. \"test.fits\""
	sys.exit(0)

origRemoval(fitsFile); #run original script
optRemoval(fitsFile);  #run optimized script

