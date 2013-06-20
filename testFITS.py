"""
This program takes two fits files as arguments and checks for 
differences between them. 
"""
import sys
import subprocess
import numpy
from astropy.io import fits

sys.path.append("original") # The original cosmics module directory
import cosmics as origCosmics

sys.path.append("optimized") # The optimized cosmics module directory
import cosmics as optCosmics
	
if sys.argv[1].endswith(".fits") & sys.argv[2].endswith(".fits"):
	file1=sys.argv[1] 
	file2=sys.argv[2]
else:
	print "Unrecognized argument(s). Requires two fits files."
	sys.exit(0)


fits1=fits.open(file1)
fits2=fits.open(file2)
data1=fits1[0].data
data2=fits2[0].data
print data1
print data2
fits1.close()	

