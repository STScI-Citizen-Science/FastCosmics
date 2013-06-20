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

License
=======

Fast Cosmics is licensed under a 3-clause BSD style license:

Copyright (c) 2013, Space Telescope Science Institute.

All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

- Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
- Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
- Neither the name of Space Telescope Science Institute nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.




