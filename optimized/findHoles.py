  def findholes(self, verbose = True):
        """
        Detects "negative cosmics" in the cleanarray and adds them to the mask.
        This is not working yet.
        """
        pass
        
        """
        if verbose == None:
            verbose = self.verbose
        
        if verbose :
            print "Finding holes ..."

        m3 = ndimage.filters.median_filter(self.cleanarray, size=3, mode='mirror')
        h = (m3 - self.cleanarray).clip(min=0.0)
        
        tofits("h.fits", h)
        sys.exit()
        
        # The holes are the peaks in this image that are not stars
    
        #holes = h > 300
        """
        """
        subsam = subsample(self.cleanarray)
        conved = -signal.convolve2d(subsam, laplKernel, mode="same", boundary="symm")
        cliped = conved.clip(min=0.0)
        lplus = rebin2x2(conved)
        
        tofits("lplus.fits", lplus)
        
         m5 = ndimage.filters.median_filter(self.cleanarray, size=5, mode='mirror')
         m5clipped = m5.clip(min=0.00001)
         noise = (1.0/self.gain) * np.sqrt(self.gain*m5clipped + self.readnoise*self.readnoise)
 
         s = lplus / (2.0 * noise) # the 2.0 is from the 2x2 subsampling
         # This s is called sigmap in the original lacosmic.cl
         
         # We remove the large structures (s prime) :
         sp = s - ndimage.filters.median_filter(s, size=5, mode='mirror')
         
         holes = sp > self.sigclip    
        """
        """
        # We have to kick out pixels on saturated stars :
        if self.satstars != None:
             if verbose:
                 print "Masking saturated stars ..."
             holes = np.logical_and(np.logical_not(self.satstars), holes)
        
        if verbose:
            print "%i hole pixels found" % np.sum(holes)
        
        # We update the mask with the holes we have found :
        self.mask = np.logical_or(self.mask, holes)
        """