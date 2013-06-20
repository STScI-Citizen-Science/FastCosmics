"""
This script takes a fits file as input and runs both the 
original cosmics.py module as well as the optimized fast
cosmics module on it. 
Outputs: origClean.fits, origMask.fits, optClean.fits, optMast.fits
"""

import sys
import subprocess
import numpy

sys.path.append("original") # The original cosmics module directory
import cosmics as origCosmics

sys.path.append("optimized") # The optimized cosmics module directory
import cosmics as optCosmics

if sys.argv[1].endswith(".fits"):
	fitsFile=sys.argv[1]; #first argument is the input FITS file
else:
	print "Unrecognized argument. Requires fits file. Eg. \"test.fits\""
	sys.exit(0)
	
def origRemoval(fitsFile):
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

origRemoval(fitsFile);
optRemoval(fitsFile);

