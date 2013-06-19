FastCosmics
===========

An optimization of the cosmics.py module. Original available at: http://obswww.unige.ch/~tewes/cosmics_dot_py/

Original cosmics.py description
===============================

cosmics.py is a small and simple python module to detect and clean cosmic ray hits on images (numpy arrays or FITS), using scipy, and based on Pieter van Dokkum's L.A. Cosmic algorithm.

Additional features:

- Automatic recognition of saturated stars, including their full saturation trails.
- Scipy image analysis allows to "label" the actual cosmic ray hits (i.e. group the pixels into local islands). 

Full description available at: http://obswww.unige.ch/~tewes/cosmics_dot_py/cosmics.py_0.4/doc/index.html

Requirements
============

The python libraries necessary to run cosmics are as follows:

- pyfits
- numpy
- scipy

Usage
=====

The functions available are as follows:

1. fromfits(infilename, hdu=0, verbose=True) : Reads a FITS file and returns a 2d numpy array of data.

2. tofits(outfilename, pixelarray, hdr=None, verbose=True) : Takes a 2d numpy array and writes it into a FITS file.

3. subsample(a) : Returns a 2x2 subsampled version of an array a.

4. rebin(a, newshape) : Auxiliary function to rebin an ndarray a.

Optimizations
=============

1. Original code modified to follow PEP8 compliance. Done with the help of the pylint library for python. (WIP)

2. Loops in original code replaced with more optimal numpy array based operations. (WIP)

3. Redundant comments and docstrings moved out of the main module. (WIP) 

Efficiency Achieved
===================

(WIP)